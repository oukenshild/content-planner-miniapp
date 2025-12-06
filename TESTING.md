# Инструкция по тестированию

## Установка зависимостей

Перед запуском тестов необходимо установить тестовые зависимости:

```bash
# Для API
pip install -r planner/requirements.txt

# Для бота
pip install -r bot/requirements.txt
```

Или установить все сразу:

```bash
pip install -r planner/requirements.txt
pip install -r bot/requirements.txt
```

## Запуск тестов

### Вариант 1: Использование скрипта

```bash
python run_tests.py
```

### Вариант 2: Прямой запуск через pytest

```bash
# Все тесты
pytest

# Только тесты API
pytest planner/tests/ -v

# Только тесты бота
pytest bot/tests/ -v

# С покрытием кода
pytest --cov=planner/app --cov=bot --cov-report=html
```

### Вариант 3: Запуск конкретных тестов

```bash
# Конкретный файл
pytest planner/tests/test_posts.py -v

# Конкретный тест
pytest planner/tests/test_posts.py::test_create_post -v
```

## Структура тестов

### Тесты API (planner/tests/)

- **test_auth.py** - тесты модуля аутентификации (verify_init_data)
- **test_session.py** - тесты создания сессии через Telegram WebApp
- **test_posts.py** - тесты CRUD операций с постами
- **test_comments.py** - тесты работы с комментариями
- **test_calendar.py** - тесты календаря (получение постов за период)

### Тесты бота (bot/tests/)

- **test_bot.py** - тесты обработчиков команд бота (команда /start)

## Что тестируется

### API Endpoints

✅ POST `/api/session` - создание сессии
✅ POST `/api/posts` - создание поста
✅ GET `/api/posts` - список постов
✅ GET `/api/posts/{id}` - получение поста
✅ PUT `/api/posts/{id}` - обновление поста
✅ DELETE `/api/posts/{id}` - удаление поста
✅ POST `/api/comments` - добавление комментария
✅ GET `/api/calendar/range` - получение постов за период

### Бот

✅ Обработка команды `/start`
✅ Создание клавиатуры с WebApp кнопкой
✅ Проверка корректности URL WebApp

### Модули

✅ Функция `verify_init_data` в модуле auth

## Примечания

- Тесты используют моки и не требуют реальной базы данных
- Тесты бота не требуют реального токена Telegram
- Все тесты изолированы и могут запускаться параллельно


