# Content Planner — Планировщик контента для Telegram

Мини-приложение в Telegram для планирования контента с поддержкой согласования постов, ролей пользователей и различных типов медиа.

## Возможности

- **Планирование контента**: создание и управление постами с указанием даты публикации
- **Согласование постов**: система статусов (черновик → на согласовании → утверждено → опубликовано)
- **Роли пользователей**: 
  - `owner` — владелец (полный доступ)
  - `editor` — редактор (создание и редактирование постов)
  - `viewer` — просмотрщик (только просмотр)
- **Типы контента**: текст, фото, короткие и длинные видео
- **Комментарии**: обсуждение постов в процессе согласования
- **Категории и теги**: организация контента
- **Календарь**: просмотр запланированных постов

## Технологии

- **Backend**: Python 3.11+, FastAPI
- **База данных**: PostgreSQL
- **Telegram Bot**: aiogram 3.x
- **Frontend**: Vanilla JavaScript (Telegram WebApp)
- **Миграции**: Alembic
- **Контейнеризация**: Docker, Docker Compose

## Требования

- Python 3.11 или выше
- PostgreSQL 16+
- Docker и Docker Compose (для упрощенного развертывания)
- VPS с публичным IP-адресом и доменом (для Telegram WebApp)
- Telegram Bot Token (получить у [@BotFather](https://t.me/BotFather))

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd Content-planner
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
# Telegram Bot
TG_BOT_TOKEN=your_bot_token_here
TG_WEBAPP_URL=https://yourdomain.com/webapp

# База данных
POSTGRES_DB=content_planner
POSTGRES_USER=planner_user
POSTGRES_PASSWORD=your_secure_password
DATABASE_URL=postgresql://planner_user:your_secure_password@db:5432/content_planner

# Telegram Bot Secret (для верификации WebApp)
TG_BOT_SECRET=your_bot_secret_here
```

### 3. Установка зависимостей

#### Вариант A: Локальная установка

```bash
# Установка зависимостей для API
pip install -r planner/requirements.txt

# Установка зависимостей для бота
pip install -r bot/requirements.txt
```

#### Вариант B: Docker (рекомендуется)

```bash
cd planner
docker-compose up -d
```

### 4. Инициализация базы данных

```bash
cd planner
alembic upgrade head
```

## Структура проекта

```
Content-planner/
├── bot/                    # Telegram бот
│   ├── bot.py             # Основной файл бота
│   ├── requirements.txt   # Зависимости бота
│   └── tests/             # Тесты бота
├── planner/                # Backend API
│   ├── app/
│   │   ├── main.py        # FastAPI приложение
│   │   ├── models.py      # SQLAlchemy модели
│   │   ├── schemas.py     # Pydantic схемы
│   │   ├── db.py          # Настройка БД
│   │   ├── auth.py        # Аутентификация
│   │   ├── rbac.py        # Управление ролями
│   │   └── routes/        # API маршруты
│   │       ├── posts.py   # Управление постами
│   │       ├── comments.py # Комментарии
│   │       ├── users.py   # Пользователи
│   │       ├── calendar.py # Календарь
│   │       └── session.py # Сессии
│   ├── alembic/           # Миграции БД
│   ├── docker-compose.yml # Docker конфигурация
│   └── requirements.txt   # Зависимости API
├── webapp/                 # Frontend (Telegram WebApp)
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── run_tests.py           # Скрипт запуска тестов
├── pytest.ini            # Конфигурация pytest
└── README.md             # Этот файл
```

## Развертывание на VPS

### 1. Подготовка сервера

```bash
# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Установка Docker Compose
sudo apt install docker-compose -y
```

### 2. Настройка домена и SSL

Настройте Nginx как reverse proxy:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /webapp {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
    }
}
```

Настройте SSL с помощью Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### 3. Запуск приложения

```bash
cd planner
docker-compose up -d
```

### 4. Настройка Telegram WebApp

1. Откройте [@BotFather](https://t.me/BotFather) в Telegram
2. Выберите вашего бота
3. Отправьте команду `/newapp`
4. Укажите домен вашего WebApp (например, `yourdomain.com`)
5. Загрузите иконку приложения (опционально)

### 5. Обновление переменных окружения

Убедитесь, что в `.env` указан правильный URL:

```env
TG_WEBAPP_URL=https://yourdomain.com/webapp
```

## Использование

### Запуск бота

```bash
cd bot
python bot.py
```

Или через Docker:

```bash
cd planner
docker-compose up bot
```

### Запуск API

```bash
cd planner
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Или через Docker:

```bash
cd planner
docker-compose up api
```

### Доступ к приложению

1. Откройте Telegram
2. Найдите вашего бота
3. Отправьте команду `/start`
4. Нажмите кнопку "Open planner"

## API Endpoints

### Сессии

- `POST /api/session` — создание сессии через Telegram WebApp

### Посты

- `GET /api/posts` — список постов (с фильтрацией по статусу)
- `POST /api/posts` — создание поста
- `GET /api/posts/{post_id}` — получение поста
- `PUT /api/posts/{post_id}` — обновление поста
- `DELETE /api/posts/{post_id}` — удаление поста

### Комментарии

- `POST /api/comments` — добавление комментария к посту

### Календарь

- `GET /api/calendar` — получение постов за период

### Пользователи

- `GET /api/users` — список пользователей
- `PUT /api/users/{user_id}` — обновление роли пользователя

## Модели данных

### Статусы постов

- `draft` — черновик
- `pending` — на согласовании
- `approved` — утверждено
- `published` — опубликовано
- `archived` — архив

### Роли пользователей

- `owner` — владелец (полный доступ)
- `editor` — редактор (создание и редактирование)
- `viewer` — просмотрщик (только просмотр)

### Структура поста

```json
{
  "id": 1,
  "title": "Заголовок поста",
  "text": "Текст поста",
  "status": "draft",
  "planned_at": "2024-01-15T10:00:00",
  "timezone": "Europe/Moscow",
  "category_id": 1,
  "attachments": {
    "photos": ["url1", "url2"],
    "videos": ["url1"]
  },
  "meta": {
    "platform": "telegram",
    "utm_source": "organic"
  }
}
```

## Тестирование

Подробная инструкция по тестированию находится в файле [TESTING.md](TESTING.md).

### Быстрый запуск тестов

```bash
python run_tests.py
```

### Запуск отдельных тестов

```bash
# Все тесты
pytest

# Только тесты API
pytest planner/tests/ -v

# Только тесты бота
pytest bot/tests/ -v
```

## Безопасность

- Аутентификация через Telegram WebApp (`initData`)
- Проверка подписи данных от Telegram
- RBAC (Role-Based Access Control) для управления доступом
- Хранение чувствительных данных в переменных окружения

## 📝 Миграции базы данных

```bash
cd planner

# Создание новой миграции
alembic revision --autogenerate -m "описание изменений"

# Применение миграций
alembic upgrade head

# Откат миграции
alembic downgrade -1
```

## Решение проблем

### Бот не отвечает

- Проверьте правильность `TG_BOT_TOKEN`
- Убедитесь, что бот запущен
- Проверьте логи: `docker-compose logs bot`

### WebApp не открывается

- Проверьте, что `TG_WEBAPP_URL` указан правильно
- Убедитесь, что домен настроен в BotFather
- Проверьте SSL сертификат
- Убедитесь, что API доступен по указанному адресу

### Ошибки подключения к БД

- Проверьте переменные окружения `DATABASE_URL`
- Убедитесь, что PostgreSQL запущен
- Проверьте права доступа пользователя БД

## Лицензия



## Авторы

Danil Iluhin

## Вклад в проект



