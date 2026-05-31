"""
CraftStack Server v0.7 — with Agent Router + multi-provider + model tiers
Zero-dependency: stdlib only.
Usage: pythonw server.py [port]
"""

import os, sys, json, time, mimetypes, threading, urllib.request, urllib.error, re
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, TimeoutError
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

PIPELINE_TIMEOUT = 600  # max total pipeline seconds
AI_TIMEOUT = 20         # seconds per provider call (fast fail = fast fallback)
ASK_TIMEOUT = 60        # max seconds waiting for user input

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(HERE, 'project', '.craftstack', 'state.json')
TASK_PATH = os.path.join(HERE, 'project', '.craftstack', 'task.txt')
AGENTS_PATH = os.path.join(HERE, 'project', '.craftstack', 'agents.json')
CONFIG_PATH = os.path.join(HERE, 'project', '.craftstack', 'config.json')
MODE_PATH = os.path.join(HERE, 'project', '.craftstack', 'mode.json')
ROUTING_PATH = os.path.join(HERE, 'project', '.craftstack', 'routing.json')
MODES_DIR = os.path.join(HERE, '.opencode', 'modes')
PROJECT_DIR = os.path.join(HERE, 'project')
RESEARCH_PATH = os.path.join(PROJECT_DIR, '.craftstack', 'research.md')

sse_queues = set()
state_lock = threading.Lock()

DEFAULT_ROUTING = {
    'ceo': 'openai',
    'pm': 'openrouter',
    'cto': 'openai',
    'developer': 'openai',
    'designer': 'openrouter',
    'marketer': 'github',
    'qa': 'github',
    'analyst': 'github',
    'researcher': 'github'
}

API_ENDPOINTS = {
    "deepseek": "https://api.deepseek.com/v1/chat/completions",
    "openai": "https://api.openai.com/v1/chat/completions",
    "gemini": "https://generativelanguage.googleapis.com/v1beta/models/",
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "github": "https://models.inference.ai.azure.com/chat/completions",
    "mistral": "https://api.mistral.ai/v1/chat/completions",
    "anthropic": "https://api.anthropic.com/v1/messages",
    "xai": "https://api.x.ai/v1/chat/completions",
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "together": "https://api.together.xyz/v1/chat/completions",
    "perplexity": "https://api.perplexity.ai/chat/completions"
}

API_MODELS_FAST = {
    "deepseek": "deepseek-chat",
    "openai": "gpt-4o-mini",
    "gemini": "gemini-2.5-flash",
    "openrouter": "openrouter/auto",
    "github": "gpt-4o-mini",
    "mistral": "mistral-small-latest",
    "anthropic": "claude-sonnet-4-6",
    "xai": "grok-4.3",
    "groq": "llama-3.1-8b-instant",
    "together": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "perplexity": "sonar-pro"
}

API_MODELS_BEST = {
    "openai": "gpt-4o",
    "deepseek": "deepseek-chat",
    "gemini": "gemini-2.5-pro",
    "openrouter": "openrouter/auto",
    "github": "gpt-4o",
    "mistral": "mistral-large-latest",
    "anthropic": "claude-sonnet-4-6",
    "xai": "grok-4.3",
    "groq": "llama-3.3-70b-versatile",
    "together": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "perplexity": "sonar-pro"
}

AGENT_TIER = {
    'ceo': 'best',
    'cto': 'best',
    'developer': 'best',
    'designer': 'best',
    'pm': 'fast',
    'marketer': 'fast',
    'qa': 'fast',
    'analyst': 'fast',
    'researcher': 'fast'
}

def default_state():
    return {
        "currentAgent": "-",
        "status": "idle",
        "phase": "idle",
        "task": "",
        "progress": {},
        "provider_status": {},
        "log": [
            {"time": time.strftime("%H:%M"), "agent": "system", "text": "CraftStack AI server started"}
        ]
    }

def update_provider_status(provider, status):
    """Track provider health in state (ok/error/timeout/nobill). No deadlock: read_state/write_state handle locking."""
    try:
        s = read_state()
        s.setdefault('provider_status', {})[provider] = status
        write_state(s)
    except:
        pass

def read_state():
    with state_lock:
        try:
            with open(STATE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return default_state()

def write_state(s):
    with state_lock:
        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        with open(STATE_PATH, 'w', encoding='utf-8') as f:
            json.dump(s, f, ensure_ascii=False, indent=2)
        data = json.dumps(s, ensure_ascii=False)
    for q in list(sse_queues):
        try:
            q.append(data)
        except:
            sse_queues.discard(q)

def read_config():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"api_key": "", "provider": "deepseek", "api_keys": {}, "agent_routing": {}}

def write_config(c):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(c, f, ensure_ascii=False, indent=2)

def read_routing():
    try:
        with open(ROUTING_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def write_routing(r):
    os.makedirs(os.path.dirname(ROUTING_PATH), exist_ok=True)
    with open(ROUTING_PATH, 'w', encoding='utf-8') as f:
        json.dump(r, f, ensure_ascii=False, indent=2)

def read_agents():
    try:
        with open(AGENTS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def write_agents(a):
    os.makedirs(os.path.dirname(AGENTS_PATH), exist_ok=True)
    with open(AGENTS_PATH, 'w', encoding='utf-8') as f:
        json.dump(a, f, ensure_ascii=False, indent=2)

def read_mode():
    try:
        with open(MODE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def write_mode(m):
    os.makedirs(os.path.dirname(MODE_PATH), exist_ok=True)
    with open(MODE_PATH, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, indent=2)

def load_mode(slug):
    path = os.path.join(MODES_DIR, f'{slug}.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def add_log(agent, text):
    s = read_state()
    if 'log' not in s:
        s['log'] = []
    s['log'].append({"time": time.strftime("%H:%M"), "agent": agent, "text": text})
    write_state(s)

def set_progress(agent_slug, status, provider=None):
    s = read_state()
    if 'progress' not in s:
        s['progress'] = {}
    s['progress'][agent_slug] = {"status": status}
    if provider:
        s['progress'][agent_slug]['provider'] = provider
    s['currentAgent'] = agent_slug
    write_state(s)

def add_chat_message(role, text):
    """Add a message to chat log. role: 'system'|'assistant'|'user'."""
    s = read_state()
    if 'chat' not in s:
        s['chat'] = []
    s['chat'].append({"role": role, "text": text, "ts": time.time()})
    write_state(s)

def ask_user(question, timeout=ASK_TIMEOUT):
    """Pipeline asks user a question and waits for answer.
    Returns the answer text, or None if timed out.
    """
    add_chat_message('assistant', question)
    s = read_state()
    s['pending_question'] = question
    s['status'] = 'waiting_input'
    s['phase'] = 'waiting_input'
    write_state(s)
    add_log('system', '⏳ Waiting for user answer...')
    deadline = time.time() + timeout
    answer = None
    while time.time() < deadline:
        s2 = read_state()
        if s2.get('pending_answer'):
            answer = s2['pending_answer']
            s2['pending_answer'] = ''
            s2['pending_question'] = ''
            s2['status'] = 'running'
            s2['phase'] = 'execution'
            write_state(s2)
            add_chat_message('user', answer)
            add_log('system', f'✍️ User answered: {answer[:100]}')
            break
        time.sleep(1)
    if answer is None:
        s = read_state()
        s['pending_question'] = ''
        s['pending_answer'] = ''
        s['status'] = 'running'
        write_state(s)
        add_log('system', '⏰ User answer timeout, continuing...')
    return answer

def call_ai(messages, api_key, provider='deepseek', max_tokens=8192, tier='fast'):
    models = API_MODELS_BEST if tier == 'best' else API_MODELS_FAST
    model = models.get(provider, 'deepseek-chat')
    endpoint = API_ENDPOINTS.get(provider, API_ENDPOINTS['deepseek'])

    if provider == 'gemini':
        gemini_contents = []
        for msg in messages:
            role = 'user' if msg['role'] == 'user' else 'model'
            gemini_contents.append({"role": role, "parts": [{"text": msg['content']}]})
        data = json.dumps({"contents": gemini_contents}).encode('utf-8')
        url = f"{endpoint}{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
    elif provider == 'anthropic':
        anthro_messages = [{"role": m["role"], "content": m["content"]} for m in messages]
        data = json.dumps({
            "model": model,
            "max_tokens": 8192,
            "messages": anthro_messages
        }).encode('utf-8')
        url = endpoint
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01"
        }
    else:
        data = json.dumps({
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens
        }).encode('utf-8')
        url = endpoint
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "CraftStack/1.0"
        }

    req = urllib.request.Request(url, data=data, headers=headers)
    resp = urllib.request.urlopen(req, timeout=AI_TIMEOUT)
    result = json.loads(resp.read().decode('utf-8'))

    if provider == 'gemini':
        return result['candidates'][0]['content']['parts'][0]['text']
    elif provider == 'anthropic':
        return result['content'][0]['text']
    return result['choices'][0]['message']['content']

def get_provider_for_agent(slug, routing, config):
    """Determine which provider to use for a given agent."""
    if slug in routing:
        return routing[slug].get('provider', DEFAULT_ROUTING.get(slug, 'deepseek'))
    agent_routing = config.get('agent_routing', {})
    if slug in agent_routing:
        return agent_routing[slug].get('preferred', DEFAULT_ROUTING.get(slug, 'deepseek'))
    return DEFAULT_ROUTING.get(slug, config.get('provider', 'deepseek'))

def get_key_for_provider(provider, config):
    """Get the API key for a given provider."""
    api_keys = config.get('api_keys', {})
    if provider in api_keys and api_keys[provider]:
        return api_keys[provider]
    return config.get('api_key', '')

def select_agents_for_task(task_text):
    """Auto-select agents based on task keywords (fallback if AI router unavailable)."""
    t = task_text.lower()
    scores = {
        'ceo': ['стратеги', 'бизнес', 'план', 'vision', 'mission', 'стартап', 'инвест', 'pitch', 'product'],
        'pm': ['требовани', 'задач', 'sprint', 'spec', 'roadmap', 'бэклог', 'user story', 'deadline'],
        'cto': ['архитектур', 'технолог', 'стек', 'выбор', 'infrastructure', 'data model', 'систем'],
        'developer': ['код', 'code', 'программир', 'разработк', 'frontend', 'backend', 'api', 'prototype', 'реализаци'],
        'designer': ['дизайн', 'ui', 'ux', 'визуал', 'бренд', 'brand', 'css', 'responsive', 'interface'],
        'marketer': ['маркетинг', 'реклам', 'landing', 'go-to-market', 'gtm', 'seo', 'копирайтинг', 'продвижени'],
        'qa': ['тест', 'bug', 'quality', 'qa', 'e2e', 'performance', 'надежност'],
        'analyst': ['анализ', 'аналитик', 'metric', 'kpi', 'юнит-экономик', 'unit economics', 'forecast', 'отчет']
    }
    selected = set()
    for slug, keywords in scores.items():
        for kw in keywords:
            if kw in t:
                selected.add(slug)
                break
    if not selected:
        return ['ceo']
    return list(selected)

ceo_agents_desc = {
    'ceo': 'Стратегия, синтез результатов команды',
    'pm': 'Задачи, требования, спринты, распределение',
    'cto': 'Архитектура, выбор технологического стека',
    'developer': 'Фулстек-разработка, прототипы, код',
    'designer': 'UI/UX дизайн, визуал, брендинг',
    'marketer': 'Маркетинг, копирайтинг, GTM-стратегия',
    'qa': 'Тестирование, баги, качество',
    'analyst': 'Юнит-экономика, метрики, аналитика',
    'researcher': 'Веб-поиск, сбор фактов, анализ рынка и конкурентов'
}

def ceo_analyze_task(task_text, config):
    """Call CEO via API to break task into sub-tasks with dependencies."""
    routing = read_routing()
    provider = get_provider_for_agent('ceo', routing, config)
    api_key = get_key_for_provider(provider, config)
    if not api_key:
        add_log('ceo', '⚠️ No API key for CEO analysis, fallback to keywords')
        return None

    agents_list = '\n'.join(f'- {k}: {v}' for k, v in ceo_agents_desc.items())
    system_prompt = (
        "Ты CEO в AI-агентной системе. Твоя задача: проанализировать запрос пользователя "
        "и разбить его на подзадачи для других AI-агентов.\n\n"
        "Доступные агенты:\n" + agents_list +
        "\n\nПравила:\n"
        "1. Разбей задачу на 2-5 подзадач. Не мельчи.\n"
        "2. Для каждой подзадачи укажи id (строка), agent (slug из списка выше), "
        "description (что сделать), depends_on (массив id подзадач, от которых зависит; [] если нет).\n"
        "3. CEO не назначай — он выполнит синтез в конце автоматически.\n"
        "4. Если нужны внешние данные (конкуренты, рынок, технологии) — добавь researcher первой подзадачей.\n"
        "5. Остальные агенты должны зависеть от researcher (depends_on: ['1']), чтобы не галлюцинировали.\n"
        "6. Если задача техническая и простая (одна HTML-страница, один файл, одна функция) — "
        "назначь ТОЛЬКО developer с одной подзадачей и всё. Без researcher, pm, cto, designer, marketer, qa.\n"
        "7. Если задача не техническая — верни одну подзадачу для подходящего агента.\n"
        "8. Ответь строго JSON, без лишнего текста:\n"
        '{"subtasks": [{"id": "1", "agent": "developer", "description": "...", "depends_on": []}]}'
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Задача:\n{task_text}\n\nРазбей на подзадачи."}
    ]

    try:
        add_log('ceo', f'🔍 CEO analyzing task via {provider} (best model)...')
        response = call_ai(messages, api_key, provider, tier='best')
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            subtasks = result.get('subtasks', [])
            valid_agents = set(ceo_agents_desc.keys())
            for st in subtasks:
                if st.get('agent') not in valid_agents:
                    st['agent'] = 'developer'
                if 'depends_on' not in st:
                    st['depends_on'] = []
            if subtasks:
                add_log('ceo', f'📋 Task broken into {len(subtasks)} sub-tasks')
                for st in subtasks:
                    deps = ', '.join(st['depends_on']) if st['depends_on'] else '—'
                    add_log('ceo', f'  {st["id"]}: {st["agent"]} ← {deps}')
                return subtasks
    except Exception as e:
        add_log('ceo', f'⚠️ CEO analysis failed: {str(e)[:100]}, fallback to keywords')

    return None

def router_agent(task_text, config):
    """Call PM via API to analyze task and determine which agents + providers to use."""
    config_data = read_config()
    routing = read_routing()
    pm_provider = get_provider_for_agent('pm', routing, config_data)
    api_key = get_key_for_provider(pm_provider, config_data)
    if not api_key:
        return select_agents_for_task(task_text), {}

    available_agents = {
        'ceo': 'Стратегия, бизнес-модель, синтез результатов команды',
        'pm': 'Задачи, требования, спринты, анализ задачи и распределение',
        'cto': 'Архитектура, выбор технологического стека',
        'developer': 'Фулстек-разработка, прототипы, код',
        'designer': 'UI/UX дизайн, визуал, брендинг',
        'marketer': 'Маркетинг, копирайтинг, GTM-стратегия',
        'qa': 'Тестирование, баги, качество',
        'analyst': 'Юнит-экономика, метрики, аналитика'
    }

    system_prompt = (
        "Ты PM (Project Manager) в AI-агентной системе. "
        "Твоя задача: проанализировать задачу пользователя и определить, "
        "какие AI-агенты нужны для её выполнения, и через какой API-провайдер "
        "запускать каждого агента.\n\n"
        "Доступные агенты и их специализация:\n"
        + '\n'.join(f'- {k}: {v}' for k, v in available_agents.items()) +
        "\n\nДоступные провайдеры API: "
        "deepseek (DeepSeek V4 Flash — бесплатный, быстрый, хорош для анализа и текста), "
        "openai (GPT-4o-mini — сильнее, лучше для кода и архитектуры), "
        "gemini (Google Gemini Pro), "
        "mistral (Mistral AI), "
        "openrouter, github.\n\n"
        "Правила:\n"
        "1. Выбери агентов, чья экспертиза реально нужна для задачи. Не включай всех подряд.\n"
        "2. Для каждого выбранного агента назначь провайдера:\n"
        "   - deepseek — базовый, быстрый, для текста и анализа\n"
        "   - openai — для кода, архитектуры, стратегии\n"
        "   - gemini — для креатива, дизайна (если квота позволяет)\n"
        "3. CEO всегда включается последним для синтеза всех результатов.\n"
        "4. Ответ дай строго в формате JSON, без лишнего текста:\n"
        '{\n'
        '  "agents": ["slug1", "slug2", ...],\n'
        '  "routing": {"slug1": "provider1", "slug2": "provider2", ...}\n'
        '}\n\n'
        "Если задача не требует агентов — верни {\"agents\": [\"ceo\"], \"routing\": {\"ceo\": \"deepseek\"}}"
    )

    user_prompt = f"Задача пользователя:\n{task_text}\n\nОпредели нужных агентов и провайдеров. Ответь JSON."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        add_log('router', f'Calling {pm_provider} API for agent routing (best model)...')
        response = call_ai(messages, api_key, pm_provider, tier='best')
        add_log('router', 'Router analysis received')

        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            agents = result.get('agents', [])
            routing_result = result.get('routing', {})
            valid_agents = [a for a in agents if a in available_agents]
            if 'ceo' not in valid_agents:
                valid_agents.append('ceo')
            if not valid_agents:
                valid_agents = ['ceo']
            add_log('router', f'Selected agents: {", ".join(valid_agents)}')
            return valid_agents, routing_result
    except Exception as e:
        add_log('router', f'⚠️ Router error, fallback to keywords: {str(e)[:100]}')

    return select_agents_for_task(task_text), {}

def web_search(query, max_results=5):
    """Search Wikipedia for real data on a topic. Returns formatted text.
    Zero-dependency: uses stdlib urllib + free Wikipedia API (no key needed).
    """
    import urllib.parse
    try:
        search_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srlimit={max_results}&format=json&srsearch={urllib.parse.quote(query)}'
        req = urllib.request.Request(search_url, headers={'User-Agent': 'CraftStack/1.0 (research agent; +https://github.com/craftstack)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for item in data.get('query', {}).get('search', []):
                title = item.get('title', '')
                snippet = re.sub(r'<.*?>', '', item.get('snippet', ''))
                page_id = item.get('pageid', '')
                extract_url = f'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&pageids={page_id}'
                try:
                    req2 = urllib.request.Request(extract_url, headers={'User-Agent': 'CraftStack/1.0'})
                    with urllib.request.urlopen(req2, timeout=10) as ext_resp:
                        ext_data = json.loads(ext_resp.read().decode('utf-8'))
                        pages_data = ext_data.get('query', {}).get('pages', {})
                        extract = ''
                        for pid, page_data in pages_data.items():
                            extract = page_data.get('extract', '')
                            if extract:
                                extract = extract[:1000] + ('...' if len(extract) > 1000 else '')
                except:
                    extract = snippet
                results.append({'title': title, 'snippet': snippet, 'extract': extract, 'url': f'https://en.wikipedia.org/wiki/{urllib.parse.quote(title)}'})
    except Exception as e:
        return f'[Web search error: {str(e)[:100]}]'

    if not results:
        return '[No results found]'

    output = f'## Wikipedia search results for: {query}\n\n'
    for r in results:
        output += f'### [{r["title"]}]({r["url"]})\n'
        output += f'{r["extract"] or r["snippet"]}\n\n'
    return output

def strip_markdown_fences(text):
    """Extract code from markdown code fences if present, otherwise return text as-is."""
    m = re.search(r'```(?:\w+)?\n(.*?)\n```', text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return text.strip()

def build_provider_chain(primary, config, tier='fast'):
    """Build ordered list of (provider, model_tier) to try.
    For 'best' tier: primary+badass → same primary+fast → other best → other fast.
    For 'fast' tier: primary+fast → other fast.
    """
    priority = ['deepseek', 'openrouter', 'github', 'groq', 'openai', 'gemini', 'mistral', 'anthropic', 'xai', 'together', 'perplexity']
    api_keys = config.get('api_keys', {})
    chain = []
    seen = set()
    def add(prov, t):
        key = prov + ':' + t
        if key not in seen:
            seen.add(key)
            chain.append((prov, t))
    if primary:
        if tier == 'best':
            add(primary, 'best')
        add(primary, 'fast')
    if tier == 'best':
        for p in priority:
            if p != primary and api_keys.get(p):
                add(p, 'best')
                add(p, 'fast')
    else:
        for p in priority:
            if p != primary and api_keys.get(p):
                add(p, 'fast')
    for p, key in api_keys.items():
        k = p + ':fast'
        if k not in seen and key:
            chain.append((p, 'fast')); seen.add(k)
    return chain if chain else [(primary or 'deepseek', 'fast')]

def read_project_context():
    """Read key project files to understand what CraftStack really is.
    Returns formatted text with project facts.
    """
    parts = []
    agents_path = os.path.join(HERE, 'AGENTS.md')
    if os.path.exists(agents_path):
        with open(agents_path, 'r', encoding='utf-8') as f:
            parts.append(f'## AGENTS.md (project overview)\n{f.read()[:3000]}')
    context_path = os.path.join(HERE, 'CONTEXT.md')
    if os.path.exists(context_path):
        with open(context_path, 'r', encoding='utf-8') as f:
            parts.append(f'## CONTEXT.md (full context)\n{f.read()[:3000]}')
    server_path = os.path.join(HERE, 'server.py')
    if os.path.exists(server_path):
        with open(server_path, 'r', encoding='utf-8') as f:
            header = f.read()[:500]
            parts.append(f'## server.py (header)\n{header}')
    structure = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        rel = os.path.relpath(root, PROJECT_DIR)
        if rel == '.':
            for f in files[:10]:
                structure.append(f'  {f}')
        else:
            structure.append(f'{rel}/')
            for f in files[:3]:
                structure.append(f'  {f}')
    parts.append(f'## Project structure\n{chr(10).join(structure[:20])}')
    return '\n\n---\n\n'.join(parts)

def github_search(query, max_results=3):
    """Search GitHub repositories. No key needed for basic search."""
    import urllib.parse
    try:
        url = f'https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&per_page={max_results}&sort=stars'
        req = urllib.request.Request(url, headers={'User-Agent': 'CraftStack/1.0', 'Accept': 'application/vnd.github.v3+json'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('items', [])
            if not items:
                return '[No GitHub results found]'
            output = f'## GitHub search results for: {query}\n\n'
            for r in items[:max_results]:
                desc = (r.get('description') or '')[:200]
                stars = r.get('stargazers_count', 0)
                lang = r.get('language') or 'N/A'
                url = r.get('html_url', '')
                output += f'- [{r["name"]}]({url}) — {desc} (⭐{stars}, {lang})\n'
            return output
    except Exception as e:
        return f'[GitHub search error: {str(e)[:100]}]'

def run_agent(slug, task_text, shared_context, idx, total, is_short, ts, requested_files, config, routing, existing_content=None):
    """Execute a single agent, trying fallback providers on failure."""
    mode = load_mode(slug)
    if not mode:
        add_log(slug, f'⚠️ Mode file not found for {slug}')
        return '', False

    agent_name = mode.get('name', slug)
    role_def = mode.get('roleDefinition', f'You are {agent_name}.')
    primary_provider = get_provider_for_agent(slug, routing, config)
    agent_tier = AGENT_TIER.get(slug, 'fast')
    providers_to_try = build_provider_chain(primary_provider, config, tier=agent_tier)

    if is_short and idx != 0:
        team_dir = os.path.join(PROJECT_DIR, 'team', 'kickoff')
        os.makedirs(team_dir, exist_ok=True)
        greeting = f"Привет! Я {agent_name}. Получил твоё сообщение. Рад работать вместе! 🤝"
        response_path = os.path.join(team_dir, f'{slug}-response.md')
        with open(response_path, 'w', encoding='utf-8') as f:
            f.write(f"# {agent_name} — Response\n\n{greeting}")
        add_log(slug, f'Response saved (no API call)')
        set_progress(slug, 'done', provider=primary_provider)
        return f"\n### {agent_name}\n{greeting}", True

    file_context = ''
    if existing_content:
        file_context = "\n\nСуществующие файлы проекта, которые нужно доработать:\n"
        for fn, content in existing_content.items():
            file_context += f"\n--- {fn} ---\n{content}\n"

    # Build prompts — force agents to output FINAL ARTIFACT, not instructions
    if is_short:
        system_prompt = role_def + "\n\nTask: " + task_text
        user_prompt = "ОТВЕТЬ НА ЗАДАЧУ. Твой ответ — это конечный результат. Не пиши инструкции или планы. Просто сделай."
    elif idx == 0:
        system_prompt = role_def + "\n\nTask: " + task_text + file_context
        user_prompt = (
            "ТЫ СОЗДАЁШЬ КОНЕЧНЫЙ АРТЕФАКТ. НЕ ПИШИ ИНСТРУКЦИИ ИЛИ ПЛАНЫ.\n\n"
            "Правила:\n"
            "- Твой ответ — ЭТО И ЕСТЬ ГОТОВЫЙ ПРОДУКТ. Код, HTML, Markdown — что угодно, но готовое.\n"
            "- НИКАКИХ объяснений вида «я создал файл», «вот код», «проверь», «доработан HTML». НИЧЕГО, КРОМЕ АРТЕФАКТА.\n"
            "- Если делаешь HTML — ответ начинается с <!DOCTYPE html> и заканчивается </html>. Без Markdown-обёртки.\n"
            "- Если делаешь JS — только код, без Markdown-фence.\n"
            "- Не пиши «```html» или «```». Пиши чистый код.\n"
            "- НЕ ИСПОЛЬЗУЙ Markdown-форматирование в ответе. Только чистый текст результата."
        )
    else:
        system_prompt = (
            role_def +
            "\n\n---\nОбщая задача: " + task_text +
            file_context +
            "\n\nРезультаты работы предыдущих агентов команды:\n" + shared_context +
            "\n\n---\nТвоя задача: изучи результаты предыдущих агентов и создай ИТОГОВЫЙ результат. "
            "Не повторяй уже написанное — добавляй новую ценность."
        )
        user_prompt = (
            "Вот что уже сделали коллеги:\n" + shared_context +
            "\n\nТеперь твоя очередь. Твой ОТВЕТ — это конечный продукт/артефакт. "
            "Не пиши «я создал бы...» или «вот код для генерации...». Напиши САМ АРТЕФАКТ. "
            "Если нужно создать HTML — создай HTML. Если Markdown — создай Markdown. ДЕЛАЙ, не объясняй."
        )

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

    # Researcher injects real data from multiple sources
    if slug == 'researcher':
        add_log(slug, '🔍 Searching multiple sources for real data...')
        search_query = task_text[:100]
        parts = []
        project_facts = read_project_context()
        parts.append(f'## Our project facts (GROUND TRUTH — base all comparisons on this)\n{project_facts}')
        wiki = web_search(search_query)
        parts.append(f'\n\n{wiki}')
        gh = github_search('paperclip')
        parts.append(f'\n\n{gh}')
        research_context = '\n\n---\n\n'.join(parts)
        messages.insert(1, {"role": "system", "content": f"REAL DATA — use ONLY these facts as basis. DO NOT hallucinate or invent.\n\n{research_context}"})
        add_log(slug, '✅ Multi-source research injected')
        try:
            os.makedirs(os.path.dirname(RESEARCH_PATH), exist_ok=True)
            with open(RESEARCH_PATH, 'w', encoding='utf-8') as f:
                f.write(research_context)
        except:
            pass

    elif slug != 'researcher' and os.path.exists(RESEARCH_PATH):
        try:
            with open(RESEARCH_PATH, 'r', encoding='utf-8') as f:
                research_text = f.read()
            if research_text.strip():
                messages.insert(1, {"role": "system", "content": f"GROUND TRUTH research data (base your work ONLY on these facts):\n\n{research_text}"})
                add_log(slug, '📚 Research context loaded')
        except:
            pass

    last_error = ''
    for provider, model_tier in providers_to_try:
        api_key = get_key_for_provider(provider, config)
        if not api_key:
            add_log(slug, f'⏭️ No key for {provider}, skip')
            continue

        models_map = API_MODELS_BEST if model_tier == 'best' else API_MODELS_FAST
        model_name = models_map.get(provider, 'deepseek-chat')
        set_progress(slug, 'running', provider=provider)
        add_log(slug, f'Starting as {agent_name} via {provider} ({model_name})...')

        try:
            add_log(slug, f'Calling {provider} ({model_name})...')
            response = call_ai(messages, api_key, provider, tier=model_tier)
            add_log(slug, f'✅ {agent_name} completed via {provider} ({model_name})')

            # Strip Markdown fences if present
            clean_response = strip_markdown_fences(response)

            if is_short:
                team_dir = os.path.join(PROJECT_DIR, 'team', 'kickoff')
                os.makedirs(team_dir, exist_ok=True)
                output_path = os.path.join(team_dir, f'{slug}-kickoff.md')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {agent_name} — Kickoff\n\n{clean_response}")
                add_log(slug, f'Kickoff saved')
            else:
                output_dir = os.path.join(PROJECT_DIR, slug)
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, f'{slug}-{ts}.md')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {agent_name} — Output\n\n{clean_response}")
                add_log(slug, f'Result saved')

            # Always write HTML output to project/output.html
            is_html = '<html' in clean_response.lower() or '<!doctype' in clean_response.lower()
            ext = '.html' if is_html else '.md'
            root_name = f'output{ext}'
            root_path = os.path.join(PROJECT_DIR, root_name)
            with open(root_path, 'w', encoding='utf-8') as f:
                f.write(clean_response)
            add_log(slug, f'✅ Wrote final {root_name} to project root')

            set_progress(slug, 'done', provider=provider)
            update_provider_status(provider, 'ok')
            return f"\n\n### {agent_name} (via {provider})\n{response}", True

        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            last_error = f'HTTP {e.code}: {body[:200]}'
            err_lower = last_error.lower()
            if 'credit' in err_lower or 'balance' in err_lower or 'billing' in err_lower or 'quota' in err_lower or 'exceeded' in err_lower:
                update_provider_status(provider, 'nobill')
            else:
                update_provider_status(provider, 'error')
            add_log(slug, f'❌ {provider} error, trying next: {last_error}')
        except Exception as e:
            last_error = str(e)[:200]
            err_lower = last_error.lower()
            if 'timed out' in err_lower or 'timeout' in err_lower:
                update_provider_status(provider, 'timeout')
            else:
                update_provider_status(provider, 'error')
            add_log(slug, f'❌ {provider} failed, trying next: {last_error}')

    # All providers failed
    add_log(slug, f'⚠️ All providers failed for {slug}. Last: {last_error}')
    set_progress(slug, 'error', provider=providers_to_try[0][0] if providers_to_try else 'unknown')
    return '', False

def set_phase(phase):
    s = read_state()
    s['phase'] = phase
    s['status'] = 'running'
    write_state(s)

def build_execution_graph(subtasks_or_agents):
    """Build level-based execution graph.
    Input: list of sub-tasks with 'id', 'agent', 'depends_on'
           OR list of agent slugs (backward compat).
    Returns: list of levels, each level is a list of {id, agent, description}.
    """
    if all(isinstance(x, str) for x in subtasks_or_agents):
        return [{"level": i, "tasks": [{"id": str(i), "agent": x, "description": x}]} for i, x in enumerate(subtasks_or_agents)]

    tasks = list(subtasks_or_agents)
    levels = []
    assigned = set()
    remaining = list(tasks)

    while remaining:
        level_tasks = []
        still_remaining = []
        for t in remaining:
            deps = set(t.get('depends_on', []))
            if deps.issubset(assigned):
                level_tasks.append(t)
            else:
                still_remaining.append(t)
        if not level_tasks:
            for t in still_remaining:
                level_tasks.append(t)
                assigned.add(t['id'])
            break
        for t in level_tasks:
            assigned.add(t['id'])
        levels.append({"level": len(levels), "tasks": [{"id": t['id'], "agent": t['agent'], "description": t.get('description', '')} for t in level_tasks]})
        remaining = still_remaining

    return levels

def run_pipeline(task_text, agents, is_short, routing, subtasks=None):
    """Execute the full pipeline: ANALYSIS→ROUTING→EXECUTION→SYNTHESIS."""
    ts = time.strftime("%Y%m%d-%H%M%S")
    config = read_config()
    routing = read_routing()
    existing_content = {}
    requested_files = []
    try:
        # ──────────────────────────────────────────────
        # PHASE 1: ANALYSIS
        # ──────────────────────────────────────────────
        set_phase('analysis')
        add_log('system', '📋 Phase 1/4: ANALYSIS — CEO breaks down task')

        if subtasks is None and not is_short:
            result = ceo_analyze_task(task_text, config)
            if result:
                subtasks = result
                add_log('ceo', f'✅ CEO analysis: {len(subtasks)} sub-tasks, {len(agents)} agent(s)')
            else:
                add_log('system', '⚠️ CEO analysis failed, using flat agent list')

        # Confirmation via chat
        add_log('system', '⏳ Waiting for user confirmation...')
        confirm = ask_user(
            "Вот план пайплайна. Подтверждаешь?\n\n"
            f"Задача: {task_text[:200]}...\n"
            f"Агенты: {', '.join(agents)}\n"
            f"Режим: {'Простой' if is_short else 'Сложный'}\n"
            f"Подзадачи: {len(subtasks) if subtasks else '—'}\n\n"
            "Ответь «да» или «go» для запуска, или напиши замечания."
        )
        if confirm and confirm.lower() not in ('да', 'go', 'yes', 'ok', 'старт', 'start', 'y'):
            add_log('system', f'🛑 Pipeline cancelled by user: {confirm[:100]}')
            s = read_state()
            s['status'] = 'idle'
            s['phase'] = 'idle'
            write_state(s)
            return

        # ──────────────────────────────────────────────
        # PHASE 2: ROUTING
        # ──────────────────────────────────────────────
        set_phase('routing')
        add_log('system', '📍 Phase 2/4: ROUTING')

        s = read_state()
        s['pipeline_routing'] = {slug: get_provider_for_agent(slug, routing, config) for slug in agents}
        s['agents'] = agents
        write_state(s)

        for slug in agents:
            prov = get_provider_for_agent(slug, routing, config)
            tier = AGENT_TIER.get(slug, 'fast')
            add_log('system', f'  {slug} → {prov} ({tier})')

        # Build execution graph
        graph_input = subtasks if subtasks else agents
        levels = build_execution_graph(graph_input)
        s = read_state()
        s['graph'] = levels
        write_state(s)
        add_log('system', f'📊 Execution graph: {len(levels)} level(s)')
        for lev in levels:
            descs = ', '.join(f'{t["agent"]}:{t["id"]}' for t in lev['tasks'])
            add_log('system', f'  Level {lev["level"]}: {descs}')

        # ──────────────────────────────────────────────
        # PHASE 3: EXECUTION
        # ──────────────────────────────────────────────
        set_phase('execution')
        add_log('system', '⚙️ Phase 3/4: EXECUTION')

        for level in levels:
            tasks = level['tasks']
            slugs = [t['agent'] for t in tasks]
            add_log('system', f'▶️ Level {level["level"]}: {", ".join(slugs)}')

            executor = ThreadPoolExecutor(max_workers=min(len(tasks), 4))
            futures = {}
            for task in tasks:
                slug = task['agent']
                future = executor.submit(
                    run_agent, slug, task_text, '', 0, len(tasks),
                    is_short, ts, requested_files, config, routing, existing_content
                )
                futures[future] = slug

            deadline = time.time() + PIPELINE_TIMEOUT
            remaining = set(futures)
            while remaining and time.time() < deadline:
                done, remaining = wait(remaining, timeout=min(5, deadline - time.time()))
                for future in done:
                    slug = futures[future]
                    try:
                        result, success = future.result(timeout=1)
                        if success and result:
                            existing_content[slug] = result
                    except TimeoutError:
                        pass
                    except Exception as e:
                        add_log(slug, f'❌ Execution error: {str(e)[:200]}')
                        import traceback
                        add_log(slug, traceback.format_exc()[:200])
            if remaining:
                add_log('system', f'⏰ PIPELINE TIMEOUT — {len(remaining)} agent(s) cancelled')
                for future in remaining:
                    future.cancel()
            executor.shutdown(wait=False)

        # ──────────────────────────────────────────────
        # PHASE 4: SYNTHESIS (CEO compiles all results)
        # ──────────────────────────────────────────────
        set_phase('synthesis')
        add_log('system', '🏛️ Phase 4/4: SYNTHESIS (CEO)')

        shared = '\n\n'.join(existing_content.values()) if existing_content else ''
        if shared:
            result, _ = run_agent(
                'ceo', task_text, shared, 0, 1, is_short, ts,
                requested_files, config, routing, existing_content
            )
            if result:
                add_log('system', '✅ CEO synthesis complete')

        s = read_state()
        s['status'] = 'done'
        s['phase'] = 'done'
        write_state(s)
        add_log('system', '✅ Pipeline complete!')
        add_chat_message('system', '✅ Пайплайн завершён!\n📄 Результат: project/output.html')
    except Exception as e:
        add_log('system', f'💥 Pipeline crashed: {str(e)[:200]}')
        import traceback
        for line in traceback.format_exc().splitlines()[:10]:
            add_log('system', line[:200])
        s = read_state()
        s['status'] = 'idle'
        s['phase'] = 'idle'
        s['error'] = str(e)[:200]
        write_state(s)


def _background_route(task_text, initial_agents):
    """Run AI router in background to not block task submission."""
    config = read_config()
    try:
        router_agents, router_routing = router_agent(task_text, config)
        if not initial_agents:
            initial_agents = router_agents
        routing = read_routing()
        if router_routing:
            for slug, prov in router_routing.items():
                if slug not in routing:
                    routing[slug] = {"provider": prov}
            write_routing(routing)
        write_agents(initial_agents)
        s = read_state()
        s['agents'] = initial_agents
        write_state(s)
        add_log('system', f'🤖 Router: agents ready ({", ".join(initial_agents)})')
    except Exception as e:
        add_log('system', f'⚠️ Background routing failed: {str(e)[:100]}')


# ═══════════════════════════════════════════════
# HTTP HANDLER
# ═══════════════════════════════════════════════

class Handler(BaseHTTPRequestHandler):

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/':
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>CraftStack Server</h1><p>Running. <a href="/dashboard.html">Dashboard</a></p>')
            return

        # SSE endpoint
        if path == '/api/sse':
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'text/event-stream; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            q = []
            sse_queues.add(q)
            try:
                s = read_state()
                self.wfile.write(f'data: {json.dumps(s, ensure_ascii=False)}\n\n'.encode('utf-8'))
                self.wfile.flush()
                while True:
                    if q:
                        data = q.pop(0)
                        self.wfile.write(f'data: {data}\n\n'.encode('utf-8'))
                        self.wfile.flush()
                    else:
                        # Check for file changes
                        if os.path.exists(STATE_PATH):
                            mtime = os.stat(STATE_PATH).st_mtime
                            if mtime > getattr(self, '_last_mtime', 0):
                                self._last_mtime = mtime
                                s = read_state()
                                self.wfile.write(f'data: {json.dumps(s, ensure_ascii=False)}\n\n'.encode('utf-8'))
                                self.wfile.flush()
                        time.sleep(0.5)
            except (BrokenPipeError, ConnectionResetError):
                pass
            finally:
                sse_queues.discard(q)
            return

        if path == '/api/state':
            s = read_state()
            s['routing'] = read_routing()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(s, ensure_ascii=False, default=str).encode('utf-8'))
            return

        if path == '/api/task':
            task_text = ''
            if os.path.exists(TASK_PATH):
                with open(TASK_PATH, 'r', encoding='utf-8') as f:
                    task_text = f.read()
            agents = read_agents()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"task": task_text, "agents": agents}, ensure_ascii=False).encode())
            return

        if path == '/api/config':
            c = read_config()
            routing = read_routing()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({
                "provider": c.get('provider', 'deepseek'),
                "has_key": bool(c.get('api_key')),
                "api_keys": {k: bool(v) for k, v in c.get('api_keys', {}).items()},
                "routing": routing
            }, ensure_ascii=False).encode())
            return

        if path == '/api/routing':
            routing = read_routing()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(routing, ensure_ascii=False).encode())
            return

        if path == '/api/agents':
            agents = read_agents()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"agents": agents}, ensure_ascii=False).encode())
            return

        if path == '/api/results':
            results = {}
            for slug in os.listdir(PROJECT_DIR):
                slug_dir = os.path.join(PROJECT_DIR, slug)
                if os.path.isdir(slug_dir) and not slug.startswith('.'):
                    files = [f for f in os.listdir(slug_dir) if f.endswith('.md') or f.endswith('.html')]
                    if files:
                        files.sort(reverse=True)
                        latest = files[0]
                        with open(os.path.join(slug_dir, latest), 'r', encoding='utf-8') as f:
                            content = f.read()
                        results[slug] = {"file": latest, "content": content[:5000]}
            # Add root output files
            for fname in ['output.html', 'output.md']:
                fpath = os.path.join(PROJECT_DIR, fname)
                if os.path.exists(fpath):
                    with open(fpath, 'r', encoding='utf-8') as f:
                        results['__root__'] = {"file": fname, "content": f.read()[:5000]}
                    break
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(results, ensure_ascii=False).encode())
            return

        if path == '/api/log':
            s = read_state()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"log": s.get('log', [])}, ensure_ascii=False).encode())
            return

        if path == '/api/chat':
            s = read_state()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({
                "chat": s.get('chat', []),
                "pending_question": s.get('pending_question', '')
            }, ensure_ascii=False).encode())
            return

        if path == '/api/graph':
            s = read_state()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"graph": s.get('graph', [])}, ensure_ascii=False).encode())
            return

        if path == '/api/files':
            files = []
            for root, dirs, fnames in os.walk(PROJECT_DIR):
                for fname in fnames:
                    fpath = os.path.join(root, fname)
                    rel = os.path.relpath(fpath, PROJECT_DIR)
                    if not rel.startswith('.') and not rel.startswith('team') and not rel.startswith('__'):
                        files.append({"path": rel, "name": fname, "size": os.path.getsize(fpath)})
            files.sort(key=lambda x: x['name'])
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(files, ensure_ascii=False).encode())
            return

        if path == '/api/providers/list':
            config_data = read_config()
            api_keys = config_data.get('api_keys', {})
            providers = []
            for pid, key in api_keys.items():
                if key:
                    providers.append({"id": pid, "has_key": True})
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"providers": providers}, ensure_ascii=False).encode())
            return

        # Agent mode files
        if path.startswith('/api/agent-mode/'):
            slug = path.split('/')[-1]
            mode_path = os.path.join(MODES_DIR, f'{slug}.json')
            if os.path.exists(mode_path):
                with open(mode_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
            else:
                content = {"slug": slug, "name": slug.capitalize(), "roleDefinition": ""}
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(content, ensure_ascii=False).encode())
            return

        # Static files
        file_path = os.path.join(HERE, path.lstrip('/'))
        if os.path.exists(file_path) and os.path.isfile(file_path):
            ext = os.path.splitext(file_path)[1]
            ct = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', f'{ct}; charset=utf-8' if 'text' in ct else ct)
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
            return

        self.send_response(404)
        self._cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'{"error":"Not found"}')

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length else '{}'
        data = json.loads(body) if body else {}

        if path == '/api/task':
            task_text = data.get('task', '').strip()
            agents = data.get('agents', [])
            if task_text:
                os.makedirs(os.path.dirname(TASK_PATH), exist_ok=True)
                with open(TASK_PATH, 'w', encoding='utf-8') as f:
                    f.write(task_text)
            if agents:
                write_agents(agents)
            else:
                write_agents([])
            s = read_state()
            s['task'] = task_text
            s['status'] = 'waiting'
            s['phase'] = 'waiting'
            s['agents'] = agents
            s['progress'] = {}
            s['provider_status'] = {}
            s['graph'] = []
            s['currentAgent'] = '-'
            s['error'] = ''
            s['chat'] = []
            s['pending_question'] = ''
            s['log'] = [{"time": time.strftime("%H:%M"), "agent": "system", "text": f"📝 New task: {task_text[:60]}..."}]
            write_state(s)
            threading.Thread(target=_background_route, args=(task_text, agents,), daemon=True).start()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True, "agents": agents}, ensure_ascii=False).encode())
            return

        if path == '/api/start':
            s = read_state()
            is_short = data.get('mode', 'complex') == 'simple'
            task_text = s.get('task', '')
            agents = read_agents()
            if not task_text:
                self.send_response(200)
                self._cors()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": "No task"}).encode())
                return
            if not agents:
                agents = ['ceo']  # fallback if router hasn't finished yet
                write_agents(agents)
            # Clear stale state from previous run
            s['progress'] = {}
            s['provider_status'] = {}
            s['graph'] = []
            s['pipeline_routing'] = {}
            s['chat'] = []
            s['pending_question'] = ''
            s['pending_answer'] = ''
            s['currentAgent'] = '-'
            s['error'] = ''
            s['log'] = [{"time": time.strftime("%H:%M"), "agent": "system", "text": "Pipeline started"}]
            s['status'] = 'running'
            s['phase'] = 'analysis'
            write_state(s)
            add_log('system', f'🚀 Pipeline started ({"simple" if is_short else "complex"} mode)')
            threading.Thread(target=run_pipeline, args=(task_text, agents, is_short, {}), daemon=True).start()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True}).encode())
            return

        if path == '/api/clear':
            s = read_state()
            s['status'] = 'idle'
            s['phase'] = 'idle'
            s['task'] = ''
            s['agents'] = []
            s['currentAgent'] = '-'
            s['progress'] = {}
            s['error'] = ''
            s['log'] = []
            s['chat'] = []
            s['graph'] = []
            s['pipeline_routing'] = {}
            s['pending_question'] = ''
            write_state(s)
            if os.path.exists(TASK_PATH):
                with open(TASK_PATH, 'w', encoding='utf-8') as f:
                    f.write('')
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        if path == '/api/agents':
            agent_list = data.get('agents', [])
            write_agents(agent_list)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        if path == '/api/routing':
            r = data.get('routing', {})
            write_routing(r)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        if path == '/api/mode':
            mode_data = data.get('mode', {})
            write_mode(mode_data)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        if path == '/api/answer':
            answer = data.get('answer', '').strip()
            if answer:
                s = read_state()
                s['pending_answer'] = answer
                write_state(s)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": bool(answer)}).encode())
            return

        if path == '/api/key':
            key = data.get('key', '').strip()
            provider = data.get('provider', 'deepseek')
            if key:
                c = read_config()
                if 'api_keys' not in c:
                    c['api_keys'] = {}
                c['api_keys'][provider] = key
                write_config(c)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": bool(key)}).encode())
            return

        if path == '/api/providers/test':
            provider = data.get('provider', 'deepseek')
            config = read_config()
            api_key = get_key_for_provider(provider, config)
            if not api_key:
                self.send_response(200)
                self._cors()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": "No key", "provider": provider}).encode())
                return
            test_messages = [
                {"role": "user", "content": "Say exactly: OK from PROVIDER " + provider}
            ]
            try:
                t0 = time.time()
                response = call_ai(test_messages, api_key, provider, max_tokens=256)
                elapsed = round(time.time() - t0, 2)
                self.send_response(200)
                self._cors()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "provider": provider, "response": response[:200], "elapsed": elapsed}).encode())
            except urllib.error.HTTPError as e:
                body = e.read().decode('utf-8', errors='replace')
                err = f"HTTP {e.code}: {body[:200]}"
                if 'credit' in err.lower() or 'balance' in err.lower() or 'billing' in err.lower() or 'quota' in err.lower() or 'exceeded' in err.lower():
                    status = 'nobill'
                else:
                    status = 'error'
                self.send_response(200)
                self._cors()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "provider": provider, "error": err, "status": status}).encode())
            except Exception as e:
                self.send_response(200)
                self._cors()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "provider": provider, "error": str(e)[:200]}).encode())
            return

        if path == '/api/providers/check-all':
            config = read_config()
            api_keys = config.get('api_keys', {})
            results = {}
            for provider, key in api_keys.items():
                if not key:
                    results[provider] = {'ok': False, 'error': 'No key'}
                    continue
                try:
                    test_messages = [{"role": "user", "content": "Say exactly: ok"}]
                    t0 = time.time()
                    call_ai(test_messages, key, provider, max_tokens=256)
                    elapsed = round(time.time() - t0, 2)
                    results[provider] = {'ok': True, 'elapsed': elapsed}
                except urllib.error.HTTPError as e:
                    body = e.read().decode('utf-8', errors='replace')
                    err = f"HTTP {e.code}: {body[:200]}"
                    if 'credit' in err.lower() or 'balance' in err.lower() or 'billing' in err.lower() or 'quota' in err.lower() or 'exceeded' in err.lower():
                        results[provider] = {'ok': False, 'error': err, 'status': 'nobill'}
                    else:
                        results[provider] = {'ok': False, 'error': err}
                except Exception as e:
                    results[provider] = {'ok': False, 'error': str(e)[:200]}
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"results": results}).encode())
            return

        if path == '/api/explorer':
            try:
                os.startfile(PROJECT_DIR)
            except:
                pass
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        # Save mode file
        if path.startswith('/api/agent-mode/'):
            slug = path.split('/')[-1]
            mode_path = os.path.join(MODES_DIR, f'{slug}.json')
            os.makedirs(os.path.dirname(mode_path), exist_ok=True)
            with open(mode_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        self.send_response(404)
        self._cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'{"error":"Not found"}')

    def log_message(self, format, *args):
        pass  # Suppress HTTP logs


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    if not os.path.exists(STATE_PATH):
        write_state(default_state())
    elif not os.path.exists(ROUTING_PATH):
        write_routing({})
    # Reset stale pipeline state on boot
    s = read_state()
    if s.get('status') in ('running', 'waiting', 'waiting_input', 'done'):
        s['status'] = 'idle'
        s['phase'] = 'idle'
        s['currentAgent'] = '-'
        s['task'] = ''
        s['error'] = ''
        write_state(s)
    server = ThreadingHTTPServer(('', port), Handler)
    print(f'CraftStack server on http://127.0.0.1:{port}')
    try:
        server.serve_forever()
    except OSError:
        pass

if __name__ == '__main__':
    main()
