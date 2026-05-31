# Developer — Kickoff

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prospect Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            transition: background-color 0.3s;
        }
        .button-container {
            margin: 20px 0;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
        
        @media print {
            * {
                -webkit-print-color-adjust: exact !important; /* Chrome, Safari */
                color-adjust: exact !important;  /*Firefox*/
            }
            body {
                background-color: white !important;
                color: black;
            }
            button {
                display: none;
            }
        }
        
        @media (max-width: 600px) {
            h1 {
                font-size: 24px;
            }
            p {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>

    <h1>Welcome to the Prospect Page</h1>
    <p>This is an example of a prospect page with a button to open more information.</p>

    <div class="button-container">
        <button onclick="changeBackgroundColor()">Открыть проспект</button>
    </div>

    <script>
        function changeBackgroundColor() {
            document.body.style.backgroundColor = 
                document.body.style.backgroundColor === 'lightcoral' ? '' : 'lightcoral';
        }
    </script>

</body>
</html>