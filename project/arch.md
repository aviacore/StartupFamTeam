# Архитектура — Пятнашки

## Стек
- **HTML5** — структура
- **CSS3** — стили, анимации, адаптивность
- **Vanilla JS** — вся логика (никаких зависимостей)
- **LocalStorage** — таблица рекордов

## Структура файлов
```
project/src/
  index.html    — весь фронтенд в одном файле (HTML + CSS + JS)
```

## Архитектура приложения

### HTML-структура
```
.app                     — контейнер
  .header                — заголовок + счётчик ходов + таймер
  .board                 — поле 4×4
    .tile (×16)          — фишки
  .controls              — кнопки
    #newGame             — новая игра
    #bestScore           — лучший результат
```

### JS-модули (функции в одном файле)
```
initGame()               — создание поля
shuffle()                — перемешивание (Fisher-Yates)
moveTile(index)          — движение фишки
checkWin()               — проверка победы
startTimer() / stopTimer()
saveScore() / loadScores()
toggleTheme()            — смена темы
```

### Поток данных
```
Пользователь → клик по фишке → moveTile()
  → проверка соседства с пустой → swap
  → анимация CSS → checkWin()
  → если победа → stopTimer → saveScore → confetti
```

### Дизайн
- Тёмная тема (#0a0a1a фон, фишки с градиентами)
- Glassmorphism для фишек
- CSS transitions для движения
- Адаптивность через CSS Grid + media queries
