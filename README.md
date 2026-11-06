
## Запуск через Docker

1. Запустить Docker Desktop.
2. В корне проекта (где лежит `docker-compose.yml`) выполнить:
   ```bash
   docker compose up --build
   ```
3. Открыть: http://127.0.0.1:8000/

## Запуск локально (без Docker)

1. Активировать виртуальное окружение:
   ```bash
   .venv\Scripts\activate
   ```
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Перейти в папку `web-edu` и запустить сервер:
   ```bash
   cd web-edu
   python manage.py runserver
   ```
4. Открыть: http://127.0.0.1:8000/

## Основные файлы
* `docker-compose.yml` — конфигурация для запуска через Docker
* `Dockerfile` — инструкция для сборки образа
* `requirements.txt` — зависимости проекта
* `web-edu/manage.py` — управляющий скрипт Django
```
