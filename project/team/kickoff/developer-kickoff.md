# Developer — Kickoff

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CraftStack Project</title>
    <style>
        /* Base styling */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        header {
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
        }

        main {
            padding: 20px;
        }

        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        /* Responsive layout */
        @media (max-width: 600px) {
            main {
                padding: 10px;
            }

            button {
                width: 100%;
                box-sizing: border-box;
            }
        }

        /* Print styling */
        @media print {
            header, button {
                display: none;
            }

            main {
                border-top: 1px solid #000;
                margin-top: 20px;
            }
        }
    </style>
</head>

<body>
    <header>
        <h1>CraftStack — AI Agent Workbench</h1>
    </header>
    <main>
        <h2>Проектный проспект</h2>
        <p>Описание проекта и его целей...</p>
        <button onclick="window.print()">Открыть проспект</button>
    </main>
</body>

</html>