# Тесты для Content Planner API

## Установка зависимостей

```bash
pip install -r ../requirements.txt
```

## Запуск тестов

Из корневой директории проекта:

```bash
# Все тесты
pytest

# Только тесты API
pytest planner/tests/

# С покрытием кода
pytest planner/tests/ --cov=app --cov-report=html

# Конкретный файл тестов
pytest planner/tests/test_posts.py

# Конкретный тест
pytest planner/tests/test_posts.py::test_create_post
```

## Структура тестов

- `test_auth.py` - тесты модуля аутентификации
- `test_session.py` - тесты создания сессии
- `test_posts.py` - тесты CRUD операций с постами
- `test_comments.py` - тесты работы с комментариями
- `test_calendar.py` - тесты календаря
- `conftest.py` - общие фикстуры для тестов

