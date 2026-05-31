# Формат результатов

## Где хранятся

```
project/
├── results/
│   ├── 01-designer.md        — результат дизайнера
│   ├── 02-marketer.md        — результат маркетолога
│   └── 03-developer.md       — результат разработчика
├── result.md                 — финальный итог (CEO фаза 2)
└── log.json                  — машиночитаемый лог для дашборда
```

## Формат файла подзадачи (`project/results/01-designer.md`)

```markdown
## Подзадача 1: Дизайн лендинга
**Агент:** designer
**Провайдер:** deepseek (V4 Flash)
**Статус:** done
**Время:** 12.3s

## Результат

[текст результата от агента]
```

## Формат итога (`project/result.md`)

```markdown
# Итоговый результат

**Задача:** Сделать лендинг для стартапа
**Статус:** done
**Выполнено:** 3/3 подзадачи
**Время:** 45.2s

## Сводка

[CEO собирает ключевые выводы из всех подзадач]

## Детали

### 1. Дизайн лендинга
Агент: designer · Провайдер: deepseek · 12.3s · ✅

[краткое содержание]

### 2. Текст для лендинга
Агент: marketer · Провайдер: openai · 8.1s · ✅

[краткое содержание]

### 3. Вёрстка лендинга
Агент: developer · Провайдер: github · 24.8s · ✅

[краткое содержание]
```

## Формат лога (`project/log.json`)

```json
{
  "task": "Сделать лендинг для стартапа",
  "started": "2026-05-30T12:00:00",
  "phases": [
    { "phase": "analysis", "provider": "deepseek", "status": "ok", "duration": 5.2 },
    { "phase": "routing", "provider": null, "status": "ok", "duration": 0.001 },
    { "phase": "execution", "subtasks": [
      { "id": "01", "agent": "designer", "provider": "deepseek", "status": "ok", "duration": 12.3 },
      { "id": "02", "agent": "marketer", "provider": "openai", "status": "ok", "duration": 8.1 },
      { "id": "03", "agent": "developer", "provider": "github", "status": "ok", "duration": 24.8 }
    ]},
    { "phase": "synthesis", "provider": "deepseek", "status": "ok", "duration": 10.0 }
  ],
  "total_duration": 45.2,
  "status": "done"
}
```

## Где смотреть

**Результаты агентов** — на их карточках в `agents.html`. Каждая карточка показывает:
- Статус (ожидает / выполняется / done / error)
- Провайдер и время выполнения
- Результат (сворачиваемый блок)
- Навыки и роль

**На дашборде** — только статус-карта (сводка) и лог. Детальные результаты не засоряют эфир.

**Итоговый результат (CEO)** — `project/result.md`, ссылка на дашборде.
