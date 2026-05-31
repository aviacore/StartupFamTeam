# Designer — Kickoff

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CraftStack • Регистрация</title>
    <style>
        /* --- reset & base --- */
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: #0b0d12;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            color: #e3e9f2;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 1.5rem;
            background-image: radial-gradient(ellipse at 30% 20%, rgba(38, 120, 220, 0.12) 0%, transparent 55%),
                              radial-gradient(ellipse at 80% 80%, rgba(168, 85, 247, 0.08) 0%, transparent 55%);
        }
        /* --- card container --- */
        .register-wrapper {
            max-width: 1120px;
            width: 100%;
            background: #13171f;
            border-radius: 3rem 3rem 2rem 2rem;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8), inset 0 1px 1px rgba(255,255,255,0.04);
            backdrop-filter: blur(2px);
            padding: 2.5rem 2.5rem 2.8rem;
            border: 1px solid #2a3040;
        }
        /* --- title area --- */
        .header-grid {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 1.2rem 1.5rem;
            margin-bottom: 2.5rem;
            border-bottom: 1px solid #232a38;
            padding-bottom: 1.5rem;
        }
        .logo {
            display: flex;
            align-items: center;
            gap: 0.4rem 1rem;
            flex-wrap: wrap;
        }
        .logo-icon {
            background: linear-gradient(145deg, #1f78ff, #a855f7);
            width: 42px;
            height: 42px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.8rem;
            color: #0b0d12;
            box-shadow: 0 6px 14px rgba(31, 120, 255, 0.25);
        }
        .logo-text {
            font-weight: 600;
            font-size: 1.6rem;
            letter-spacing: -0.02em;
            background: linear-gradient(to right, #d6e2ff, #c4b5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .badge {
            background: #1e2636;
            border-radius: 60px;
            padding: 0.25rem 1rem 0.3rem 0.9rem;
            font-size: 0.75rem;
            color: #7e8ba8;
            border: 1px solid #2f3a4e;
            letter-spacing: 0.02em;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }
        .badge::before {
            content: "⚡";
            font-size: 0.9rem;
        }

        /* --- two columns: form / comparison table --- */
        .columns {
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 2rem 2.5rem;
            align-items: start;
        }
        @media (max-width: 780px) {
            .columns { grid-template-columns: 1fr; }
            .register-wrapper { padding: 1.8rem 1.2rem; }
        }
        /* --- left: form --- */
        .form-section h2 {
            font-size: 1.3rem;
            font-weight: 500;
            margin-bottom: 0.1rem;
            letter-spacing: -0.01em;
        }
        .form-sub {
            color: #7d8aa8;
            font-size: 0.9rem;
            margin-bottom: 1.6rem;
            border-left: 3px solid #1f78ff;
            padding-left: 0.75rem;
        }
        .form-group {
            margin-bottom: 1.3rem;
        }
        .form-group label {
            display: block;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: #919ebe;
            margin-bottom: 0.25rem;
        }
        .input-icon {
            position: relative;
        }
        .input-icon .icon {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #6a7b9a;
            font-size: 1.2rem;
            pointer-events: none;
        }
        .input-icon input {
            width: 100%;
            background: #19202c;
            border: 1px solid #2c3549;
            border-radius: 18px;
            padding: 0.9rem 1rem 0.9rem 2.8rem;
            font-size: 0.95rem;
            color: #eef3fc;
            transition: all 0.2s;
            outline: none;
        }
        .input-icon input:focus {
            border-color: #1f78ff;
            box-shadow: 0 0 0 3px rgba(31, 120, 255, 0.15);
            background: #151d2b;
        }
        .input-icon input::placeholder {
            color: #495b78;
            font-weight: 300;
        }
        .double {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin: 1.5rem 0 1.2rem;
        }
        .checkbox-group input[type="checkbox"] {
            width: 20px;
            height: 20px;
            accent-color: #1f78ff;
            border-radius: 6px;
            cursor: pointer;
        }
        .checkbox-group label {
            color: #b4c1dd;
            font-size: 0.9rem;
        }
        .btn-primary {
            background: linear-gradient(145deg, #1f78ff, #2460cc);
            border: none;
            padding: 0.9rem 1rem;
            border-radius: 60px;
            font-weight: 600;
            font-size: 1rem;
            color: white;
            width: 100%;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 6px 16px rgba(31, 120, 255, 0.2);
            letter-spacing: 0.01em;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6rem;
        }
        .btn-primary:hover {
            background: linear-gradient(145deg, #2670e8, #1f5dc0);
            transform: scale(1.01);
            box-shadow: 0 10px 22px rgba(31, 120, 255, 0.3);
        }
        .btn-primary:active { transform: scale(0.97); }
        .legal-note {
            font-size: 0.7rem;
            color: #4f6080;
            text-align: center;
            margin-top: 1rem;
            line-height: 1.4;
        }

        /* --- right: comparison table + benefits --- */
        .comparison h3 {
            font-weight: 500;
            font-size: 1.1rem;
            margin-bottom: 0.75rem;
            display: flex;
            gap: 0.6rem;
            align-items: center;
        }
        .comparison h3 span {
            background: #1b2333;
            padding: 0.2rem 0.8rem;
            border-radius: 40px;
            font-size: 0.7rem;
            color: #8296c2;
        }
        .table-wrap {
            overflow-x: auto;
            border-radius: 20px;
            border: 1px solid #283040;
            background: #10161f;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            min-width: 340px;
        }
        th {
            text-align: left;
            padding: 0.9rem 1rem 0.7rem 1rem;
            background: #151d2b;
            font-weight: 500;
            color: #bcccff;
            border-bottom: 1px solid #263046;
        }
        td {
            padding: 0.7rem 1rem;
            border-bottom: 1px solid #1e2639;
        }
        tr:last-child td { border-bottom: none; }
        .highlight-row {
            background: #1b253b;
        }
        .highlight-row td {
            color: #dbe5ff;
            font-weight: 500;
        }
        .check { color: #4ade80; font-weight: 600; }
        .cross { color: #f87171; font-weight: 400; }
        .muted { color: #5f7092; }
        .tag {
            background: #1f78ff22;
            border-radius: 40px;
            padding: 0.1rem 0.6rem;
            font-size: 0.7rem;
            color: #7b9aff;
            border: 1px solid #1f78ff33;
            margin-left: 0.3rem;
        }
        .feature-icons {
            margin-top: 1.5rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1.2rem 0.8rem;
            background: #10161f;
            border-radius: 28px;
            padding: 1.2rem 1.5rem;
            border: 1px solid #262f44;
        }
        .feature-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.8rem;
            color: #b5c4e0;
        }
        .feature-item .fi {
            font-size: 1.3rem;
        }

        /* --- print css (pdf) --- */
        @media print {
            body {
                background: white !important;
                padding: 0.2in;
                color: #111;
            }
            .register-wrapper {
                box-shadow: none;
                border: 1px solid #ccc;
                background: white;
                border-radius: 12px;
                padding: 1.2rem;
                max-width: 100%;
            }
            .logo-text {
                -webkit-text-fill-color: #0b1a33;
                background: none;
                color: #0b1a33;
            }
            .badge { background: #eef3fc; color: #1f3a6b; border-color: #aaa; }
            .header-grid { border-bottom-color: #ccc; }
            .input-icon input {
                background: #f5f7fc;
                border-color: #bcc6db;
                color: #121b2e;
            }
            .input-icon .icon { color: #4a618a; }
            .btn-primary {
                background: #1f3a6b;
                box-shadow: none;
                color: white;
            }
            .table-wrap { border-color: #b5c2db; }
            th { background: #e1e7f5; color: #0b1a33; }
            td { border-bottom-color: #d4dbea; }
            .highlight-row { background: #eaf0fd; }
            .check { color: #1a7a2e; }
            .cross { color: #b13e3e; }
            .feature-icons, .comparison h3 span { background: #eef3fa; border-color: #bcc6d6; }
            .register-wrapper { box-shadow: none; }
            .legal-note { color: #3f4f6b; }
            .logo-icon { background: #1f3a6b; color: white; }
            .checkbox-group label { color: #222; }
        }
    </style>
</head>
<body>
    <div class="register-wrapper">
        <!-- header -->
        <div class="header-grid">
            <div class="logo">
                <div class="logo-icon">⚙</div>
                <span class="logo-text">CraftStack</span>
                <span class="badge">beta · v0.7</span>
            </div>
            <div style="font-size:0.85rem; color:#6b7fa0;">
                <span>✧ AI agent workbench</span>
            </div>
        </div>

        <div class="columns">
            <!-- left: FORM -->
            <div class="form-section">
                <h2>✱ Регистрация</h2>
                <div class="form-sub">Создайте аккаунт для работы с AI-агентами</div>
                <form id="registerForm" onsubmit="event.preventDefault(); alert('✅ Заявка принята! (демо)');">
                    <div class="form-group">
                        <label>Имя / ник</label>
                        <div class="input-icon">
                            <span class="icon">👤</span>
                            <input type="text" placeholder="например, CEO Иван" required>
                        </div>
                    </div>
                    <div class="double">
                        <div class="form-group">
                            <label>Email</label>
                            <div class="input-icon">
                                <span class="icon">✉</span>
                                <input type="email" placeholder="you@startup.ru" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <label>Роль</label>
                            <div class="input-icon">
                                <span class="icon">🎯</span>
                                <input type="text" placeholder="CEO / founder" value="CEO" required>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Пароль</label>
                        <div class="input-icon">
                            <span class="icon">🔑</span>
                            <input type="password" placeholder="минимум 8 символов" required>
                        </div>
                    </div>
                    <div class="checkbox-group">
                        <input type="checkbox" id="agree" checked>
                        <label for="agree">Принимаю условия — лёгкая AI-оркестрация без тяжелых зависимостей</label>
                    </div>
                    <button class="btn-primary" type="submit">
                        <span>✦</span> Запустить воркбенч
                    </button>
                    <div class="legal-note">
                        Без БД · файловая система · порт 8765 · SSE / REST
                    </div>
                </form>
            </div>

            <!-- right: comparison table + features -->
            <div class="comparison">
                <h3>
                    ⚡ Почему CraftStack?
                    <span>vs Paperclip</span>
                </h3>
                <div class="table-wrap">
                    <table>
                        <thead>
                            <tr>
                                <th>Возможность</th>
                                <th>CraftStack</th>
                                <th>Paperclip</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="highlight-row">
                                <td>🧠 Архитектура</td>
                                <td><span class="check">✔</span> Файловая, zero-dep</td>
                                <td><span class="cross">✘</span> Тяжёлая, БД + контейнеры</td>
                            </tr>
                            <tr>
                                <td>⚙️ Агент-моды</td>
                                <td><span class="check">✔</span> 8 встроенных ролей</td>
                                <td><span class="muted">ограниченно</span></td>
                            </tr>
                            <tr class="highlight-row">
                                <td>💾 Хранение</td>
                                <td><span class="check">✔</span> JSON / .md, без БД</td>
                                <td><span class="cross">✘</span> Postgres + Redis</td>
                            </tr>
                            <tr>
                                <td>🚀 CPU-only</td>
                                <td><span class="check">✔</span> Работает на i5 / m7</td>
                                <td><span class="cross">✘</span> Требует GPU</td>
                            </tr>
                            <tr class="highlight-row">
                                <td>🔌 Live-обновления</td>
                                <td><span class="check">✔</span> SSE + fallback</td>
                                <td><span class="muted">WebSocket</span></td>
                            </tr>
                            <tr>
                                <td>💵 Стоимость</td>
                                <td><span class="check">✔</span> Бесплатно, DeepSeek API</td>
                                <td><span class="cross">✘</span> Платная инфраструктура</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- feature row with icons -->
                <div class="feature-icons">
                    <span class="feature-item"><span class="fi">📁</span> pipeline → файлы</span>
                    <span class="feature-item"><span class="fi">🧩</span> 8 agent modes</span>
                    <span class="feature-item"><span class="fi">⚡</span> SSE live</span>
                    <span class="feature-item"><span class="fi">🖥</span> pythonw.exe</span>
                    <span class="feature-item"><span class="fi">🔌</span> no GPU need</span>
                </div>
                <div style="margin-top: 0.8rem; background: #131a28; border-radius: 30px; padding: 0.6rem 1.2rem; font-size:0.75rem; border:1px solid #263047; color:#95a9d0;">
                    <span>🗸 DeepSeek V4 Flash primary · CEO ставит задачу · ассистент исполняет</span>
                </div>
            </div>
        </div>
        <!-- small extra note: hardware facts -->
        <div style="margin-top: 1.8rem; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; font-size: 0.7rem; color: #4b5f7a; border-top: 1px solid #202838; padding-top: 1rem;">
            <span>🖥 i5-10400 / Core m7-6Y75 · 16GB RAM</span>
            <span>📄 AGENTS.md + CONTEXT.md</span>
            <span>🧪 порт 8765</span>
        </div>
    </div>
</body>
</html>