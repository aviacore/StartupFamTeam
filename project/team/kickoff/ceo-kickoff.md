# CEO — Kickoff

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Изменение цвета фона</title>
    <style>
        body {
            transition: background-color 0.5s;
        }
        .button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #008CBA;
            color: white;
            border: none;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div style="text-align: center; margin-top: 20%;">
        <button class="button" onclick="changeBackgroundColor()">Изменить цвет фона</button>
    </div>

    <script>
        function changeBackgroundColor() {
            const colors = ['#FF5733', '#33FF57', '#3357FF', '#F533FF', '#FF33A6'];
            const randomColor = colors[Math.floor(Math.random() * colors.length)];
            document.body.style.backgroundColor = randomColor;
        }
    </script>
</body>
</html>