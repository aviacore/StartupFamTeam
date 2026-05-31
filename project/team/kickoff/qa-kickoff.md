# QA — Kickoff

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Регистрация</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      max-width: 480px;
      margin: 60px auto;
      padding: 0 20px;
      background: #f5f5f5;
    }
    .card {
      background: white;
      border-radius: 12px;
      padding: 32px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      margin-bottom: 28px;
      color: #1a1a1a;
    }
    label {
      display: block;
      margin-bottom: 6px;
      font-weight: 500;
      color: #333;
    }
    input {
      width: 100%;
      padding: 10px 14px;
      margin-bottom: 16px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 15px;
      box-sizing: border-box;
      transition: border-color 0.2s;
    }
    input:focus {
      outline: none;
      border-color: #4A90D9;
      box-shadow: 0 0 0 2px rgba(74,144,217,0.2);
    }
    .error {
      color: #d32f2f;
      font-size: 13px;
      margin: -12px 0 12px 0;
      display: none;
    }
    button {
      width: 100%;
      padding: 12px;
      background: #4A90D9;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }
    button:hover {
      background: #357ABD;
    }
    .success {
      text-align: center;
      color: #2e7d32;
      font-weight: 500;
      padding: 12px;
      background: #e8f5e9;
      border-radius: 8px;
      display: none;
      margin-top: 16px;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Регистрация</h1>
    <form id="regForm">
      <label for="name">Имя</label>
      <input type="text" id="name" name="name" required placeholder="Введите имя">

      <label for="email">Email</label>
      <input type="email" id="email" name="email" required placeholder="example@mail.com">
      <div class="error" id="emailError">Неверный формат email</div>

      <label for="password">Пароль</label>
      <input type="password" id="password" name="password" required minlength="6" placeholder="Минимум 6 символов">

      <label for="confirm">Подтверждение пароля</label>
      <input type="password" id="confirm" name="confirm" required placeholder="Повторите пароль">
      <div class="error" id="passError">Пароли не совпадают</div>

      <button type="submit">Зарегистрироваться</button>
    </form>
    <div class="success" id="successMsg">✅ Регистрация прошла успешно!</div>
  </div>

  <script>
    const form = document.getElementById('regForm');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmInput = document.getElementById('confirm');
    const emailError = document.getElementById('emailError');
    const passError = document.getElementById('passError');
    const successMsg = document.getElementById('successMsg');

    function validateEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    emailInput.addEventListener('input', () => {
      if (emailInput.value && !validateEmail(emailInput.value)) {
        emailError.style.display = 'block';
      } else {
        emailError.style.display = 'none';
      }
    });

    form.addEventListener('submit', function(e) {
      e.preventDefault();

      // Сброс ошибок
      emailError.style.display = 'none';
      passError.style.display = 'none';
      successMsg.style.display = 'none';

      // Валидация email
      if (!validateEmail(emailInput.value)) {
        emailError.style.display = 'block';
        emailInput.focus();
        return;
      }

      // Проверка совпадения паролей
      if (passwordInput.value !== confirmInput.value) {
        passError.style.display = 'block';
        confirmInput.focus();
        return;
      }

      // Успех
      successMsg.style.display = 'block';
      form.reset();
    });
  </script>
</body>
</html>