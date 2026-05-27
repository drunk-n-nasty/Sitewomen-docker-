# 🚀 Sitewomen (Django Backend Templatе) - Современный backend-проект на Django с использованием Docker, Docker Compose, PostgreSQL, Redis и NGINX.
## 📦 Стек
- Python 3.13
- Django
- PostgreSQL
- Redis
- Nginx
- Docker
- Docker Compose
## ⚙️ Возможности
- 🐳 Полная контейнеризация проекта
- ⚡ Быстрый запуск через Docker Compose
- 🗄 PostgreSQL как основная база данных
- 🚀 Redis для кеша / Celery / очередей
- 🌐 Nginx как reverse proxy
- 🔒 Подготовленная структура для production
- 📁 Удобная backend-архитектура
## 🚀 Быстрый старт
**1. Клонирование репозитория** 

`git clone https://github.com/drunk-n-nasty/Sitewomen-docker-.git`

**2. Создание .env** 

`DJANGO_SECRET_KEY=example` \
`DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost [::1]` \
`DATABASE_NAME=sitewomen`\
`DATABASE_USERNAME=postgres`\
`DATABASE_PASSWORD=8767`\
`DATABASE_HOST=dbps`\
`DATABASE_PORT=5432`

**3. Запуск проекта**

`docker compose up --build`

**4. Миграции**

`docker compose exec backend python manage.py migrate`

**5. Создание суперпользователя**

`docker compose exec backend python manage.py createsuperuser`

**6.Открытие проекта**

`http://localhost`

