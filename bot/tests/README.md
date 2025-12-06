# Тесты для Telegram бота

## Установка зависимостей

```bash
pip install -r ../requirements.txt
```

## Запуск тестов

Из корневой директории проекта:

```bash
# Все тесты бота
pytest bot/tests/

# Конкретный файл тестов
pytest bot/tests/test_bot.py

# Конкретный тест
pytest bot/tests/test_bot.py::test_start_command
```

## Структура тестов

- `test_bot.py` - тесты обработчиков команд бота

## Примечания

Тесты используют моки для изоляции от реального Telegram API и не требуют реального токена бота.

