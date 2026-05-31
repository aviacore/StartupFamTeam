# CraftStack — AI Agent Workbench

Лёгкая среда для работы с AI-агентами через OpenCode. Web-дашборд + Python-сервер без зависимостей.

## Быстрый старт

```
start.bat
```

Откроет dashboard на http://127.0.0.1:8765/dashboard.html

## Структура

```
server.py              — HTTP-сервер (REST API + SSE, порт 8765)
dashboard.html         — основная панель (канбан + агенты + провайдеры)
monitor.html           — монитор пайплайна (live SSE)
start.bat              — лаунчер
.opencode/modes/       — 8 режимов агентов
project/               — артефакты (код, планы, отчёты)
docs/                  — документация
```

## Агенты

CEO → PM → CTO → Developer → Designer → Marketer → QA → Analyst

## Pipeline

1. Пользователь пишет задачу в dashboard → POST /api/task
2. Assistant (OpenCode) выполняет задачу через режимы агентов
3. Результат — в `project/`, статус — в `state.json`
4. Monitor показывает прогресс через SSE

## Запуск без start.bat

```cmd
python server.py 8765
```
