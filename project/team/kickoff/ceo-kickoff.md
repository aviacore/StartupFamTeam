# CEO — Kickoff

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Крестики-нолики с самообучением</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: Arial, sans-serif;
        }
        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 5px;
            margin-top: 20px;
        }
        .cell {
            width: 100px;
            height: 100px;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2em;
            cursor: pointer;
        }
        .cell.taken {
            cursor: not-allowed;
        }
        #status {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Крестики-нолики с самообучением</h1>
    <div class="board" id="board">
        <div class="cell" data-index="0"></div>
        <div class="cell" data-index="1"></div>
        <div class="cell" data-index="2"></div>
        <div class="cell" data-index="3"></div>
        <div class="cell" data-index="4"></div>
        <div class="cell" data-index="5"></div>
        <div class="cell" data-index="6"></div>
        <div class="cell" data-index="7"></div>
        <div class="cell" data-index="8"></div>
    </div>
    <div id="status">Ваш ход</div>

    <script>
        const boardElement = document.getElementById('board');
        const statusElement = document.getElementById('status');

        let board = ['', '', '', '', '', '', '', '', ''];
        let currentPlayer = 'X';
        let gameActive = true;

        const winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];

        boardElement.addEventListener('click', function(event) {
            const index = event.target.getAttribute('data-index');
            if (index !== null && board[index] === '' && gameActive) {
                board[index] = currentPlayer;
                event.target.textContent = currentPlayer;
                event.target.classList.add('taken');
                if (checkWinner()) {
                    statusElement.textContent = `Игрок ${currentPlayer} победил!`;
                    gameActive = false;
                } else if (board.includes('')) {
                    changePlayer();
                    computerMove();
                } else {
                    statusElement.textContent = 'Ничья!';
                    gameActive = false;
                }
            }
        });

        function checkWinner() {
            return winningConditions.some(condition => {
                return condition.every(index => board[index] === currentPlayer);
            });
        }

        function changePlayer() {
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            statusElement.textContent = `Ваш ход (${currentPlayer})`;
        }

        function computerMove() {
            let emptyIndices = board.map((cell, index) => cell === '' ? index : null).filter(index => index !== null);
            let randomIndex = emptyIndices[Math.floor(Math.random() * emptyIndices.length)];
            board[randomIndex] = currentPlayer;
            document.querySelector(`.cell[data-index='${randomIndex}']`).textContent = currentPlayer;
            document.querySelector(`.cell[data-index='${randomIndex}']`).classList.add('taken');
            
            if (checkWinner()) {
                statusElement.textContent = `Игрок ${currentPlayer} победил!`;
                gameActive = false;
            } else if (!board.includes('')) {
                statusElement.textContent = 'Ничья!';
                gameActive = false;
            } else {
                changePlayer();
            }
        }
    </script>
</body>
</html>