# Документация API

## Эндпоинты для регистрации и аутентификации

### 1. Получение списка пользователей и создание нового пользователя
- **URL**: `accounts/api/users/`
- **Методы**: `GET`, `POST`

#### Тело запроса (для создания пользователя):
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "yourpassword"
}
```

#### Ответ (для получения списка пользователей):
```json
[
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com"
    }
]
```

---

### 2. Получение токена
- **URL**: `accounts/api/token/`
- **Метод**: `POST`

#### Тело запроса:
```json
{
    "username": "yourusername",
    "password": "yourpassword"
}
```

#### Ответ:
```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

---

### 3. Обновление токена
- **URL**: `accounts/api/token/refresh/`
- **Метод**: `POST`

#### Тело запроса:
```json
{
    "refresh": "refresh_token"
}
```

#### Ответ:
```json
{
    "access": "new_access_token"
}
```

## Эндпоинты для профилей пользователей

### 4. Получение профиля пользователя
- **URL**: `profiles/api/profile/`
- **Метод**: `GET`

#### Описание:
Возвращает данные текущего авторизованного пользователя, включая его профиль и список постов.

#### Ответ:
```json
{
    "id": 1,
    "username": "example_user",
    "email": "example@example.com",
    "profile": {
        "image": "/media/user_images/default.jpg",
        "bio": "Био"
    },
    "posts": [
        {
            "id": 1,
            "title": "Пост 1",
            "content": "Текст",
            "created_at": "2024-12-12T10:00:00Z"
        },
        {
            "id": 2,
            "title": "Пост 2",
            "content": "Текст",
            "created_at": "2024-12-12T12:00:00Z"
        }
    ]
}
```

---

### 5. Получение списка постов
- **URL**: `profiles/api/posts/`
- **Метод**: `GET`

#### Описание:
Возвращает список всех постов.

#### Ответ:
```json
[
    {
        "id": 1,
        "title": "Пост 1",
        "content": "Текст",
        "created_at": "2024-12-12T10:00:00Z"
    },
    {
        "id": 2,
        "title": "Пост 2",
        "content": "Текст",
        "created_at": "2024-12-12T12:00:00Z"
    }
]
```

---

### 6. Создание нового поста
- **URL**: `profiles/api/posts/`
- **Метод**: `POST`

#### Тело запроса:
```json
{
    "title": "Новый пост",
    "content": "Текст"
}
```

#### Ответ:
```json
{
    "id": 3,
    "title": "Новый пост",
    "content": "Текст",
    "created_at": "2024-12-12T15:00:00Z"
}
```

---

### 7. Поиск пользователей по логину
- **URL**: `profiles/api/search-user/`
- **Метод**: `GET`

#### Параметры запроса:
- `username` (string) — логин пользователя.

#### Пример запроса:
```http
GET /profiles/api/search-user/?username=jane_doe
Authorization: Bearer <access_token>
```

#### Пример ответа:
```json
{
    "id": 2,
    "username": "jane_doe",
    "email": "jane@example.com",
    "profile": {
        "image": "/media/user_images/default.jpg",
        "bio": "Jane's bio",
        "friends": []
    },
    "posts": []
}
```

---

### 8. Добавление пользователя в друзья
- **URL**: `profiles/api/add-friend/`
- **Метод**: `POST`

#### Тело запроса:
```json
{
    "username": "jane_doe"
}
```

#### Пример ответа:
```json
{
    "message": "jane_doe добавлен в друзья."
}
```

---

### 9. Удаление пользователя из друзей
- **URL**: `profiles/api/remove-friend/`
- **Метод**: `POST`

#### Тело запроса:
```json
{
    "username": "jane_doe"
}
```

#### Пример ответа:
```json
{
    "message": "jane_doe удален из друзей."
}
```

---
## Эндпоинты для чатов

### 10. Получение списка всех чатов и создание нового чата
- **URL**: `messenger/api/chatrooms/`
- **Методы**: `GET`, `POST`

#### Тело запроса (для создания чата):
```json
{
    "recipient": "username"
}
```

#### Ответ (пример списка чатов):
```json
[
    {
        "id": 1,
        "name": "user1_user2",
        "members": [1, 2],
        "display_name": "user2"
    }
]
```

---

### 11. Получение сообщений в чате и отправка нового сообщения
- **URL**: `messenger/api/chatrooms/<room_name>/messages/`
- **Методы**: `GET`, `POST`

#### Тело запроса (для отправки сообщения):
```json
{
    "content": "Привет!"
}
```

#### Ответ (пример списка сообщений):
```json
[
    {
        "id": 1,
        "user": "user1",
        "content": "Привет!",
        "timestamp": "2023-12-01T10:00:00Z"
    }
]
```

---

### 12. Получение чатов текущего пользователя
- **URL**: `messenger/api/user/chatrooms/`
- **Метод**: `GET`

#### Ответ:
```json
[
    {
        "id": 1,
        "name": "user1_user2",
        "members": [1, 2],
        "display_name": "user2"
    }
]
```

---

## WebSocket API

### 13. Подключение к чату через WebSocket
- **URL**: `messenger/ws/ws/chat/<room_name>/`

#### Пример подключения:
```javascript
const ws = new WebSocket("ws://localhost:8000/messenger/ws/ws/chat/user1_user2/");
```

#### Тело сообщения (отправка сообщения через WebSocket):
```json
{
    "message": "Привет!"
}
```

#### Ответ (сообщение от сервера):
```json
{
    "id": 1,
    "user": "user1",
    "content": "Привет!",
    "timestamp": "2023-12-01T10:00:00Z"
}
```

