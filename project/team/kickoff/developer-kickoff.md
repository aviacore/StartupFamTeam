# Developer — Kickoff

<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CraftStack — AI Agent Workbench</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            text-align: center;
            width: 100%;
        }

        main {
            padding: 20px;
            max-width: 800px;
        }

        button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 10px 0;
            cursor: pointer;
            font-size: 16px;
        }

        @media print {
            button {
                display: none;
            }
        }

        @media (max-width: 600px) {
            main {
                width: 95%;
                padding: 10px;
            }

            header {
                font-size: 18px;
            }

            button {
                width: 100%;
                padding: 15px;
            }
        }
    </style>
</head>

<body>
    <header>
        CraftStack — AI Agent Workbench
    </header>

    <main>
        <h1>Добро пожаловать в CraftStack</h1>
        <p>Эта платформа предоставляет легкий интерфейс для использования и управления ИИ-агентами в рамках рабочих процессов. Мы предлагаем простоту и мощные инструменты для твоего бизнеса.</p>
        <button onclick="window.open('prospect.pdf')">Открыть проспект</button>
    </main>
</body>

</html>