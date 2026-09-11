# Blog API

REST API для блога на Django REST Framework.

## Как запустить проект

### 1. Клонировать проект

```bash
git clone <ссылка-на-репозиторий>
cd Test-5
```

### 2. Создать виртуальное окружение

```bash
python3 -m venv venv
```

### 3. Активировать виртуальное окружение

```bash
source venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Выполнить миграции

```bash
python manage.py migrate
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

После запуска API будет доступно по адресу:

`http://127.0.0.1:8000/`

## Документация API

Swagger:

`http://127.0.0.1:8000/swagger/`

ReDoc:

`http://127.0.0.1:8000/redoc/`
