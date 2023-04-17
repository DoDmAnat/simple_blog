# simple_blog

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DoDmAnat/simple_blog
```

```
cd simple_blog/backend
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/script/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов к API

### Регистрация нового пользователя:

```bash
POST - 'http://localhost/api/users/'
```

```yaml
{
  "username": "user_username.",
  "email": "user@mail.ru",
  "password": "user_password.",
  "first_name": "user_first_name",
  "last_name": "user_last_name",
}
```

#### Ответ

```yaml
{
  "id": 2,
  "username": "user_username.",
  "email": "user@mail.ru",
  "first_name": "user_first_name",
  "last_name": "user_last_name",
}
```

### Получение токена:

#### Запрос

```bash
POST - 'http://localhost/api/auth/token/login/'
```

```yaml
{ "password": "user_password.", "email": "user@mail.ru" }
```

#### Ответ

```yaml
{ "auth_token": "token_value" }
```

### Информация о своей учетной записи:

#### Запрос

```bash
GET - 'http://localhost/api/users/me/'
header 'Authorization: Token "token_value"'
```

#### Ответ

```yaml
{
  "id": 2,
  "username": "user_username.",
  "email": "user@mail.ru",
  "first_name": "user_first_name",
  "last_name": "user_last_name",
  "is_subscribed": false,
}
```

### Получение всех публикаций

```
GET api/posts/
```

### POST-запрос авторизованного пользователя на добавление записи

```
POST .../api/posts/

{
    "text": "Текст поста",
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg=="
}
```

Пример ответа

```
{
        "id": 1,
        "author": "admin1",
        "text": "Пост1",
        "pub_date": "Apr 13, 2023",
        "image": "http://127.0.0.1:8000/media/posts/Open.png",
        "comments": []
    },
```

### POST-запрос авторизованного пользователя на добавление комментария

```
POST .../api/posts/1/comments/

{
    "text": string (текст комментария)
}
```

Пример ответа

```
{
    "id": integer (id комментария),
    "author": "string (username пользователя)",
    "text": "string (текст комментария)",
    "created": string <date-time>,
    "post": integer (id публикации),
}
```

Запуск фронтенда:

```
cd simple_blog/frontend
```

```
npm install
```

```
npm run serve
```

Автор: [Домрачев Дмитрий](https://github.com/DoDmAnat)
