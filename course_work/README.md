## Эндпоинты для регистрации и аутентификации

1. **Получение списка пользователей и создание нового пользователя**
   - **URL**: `accounts/api/users/`
   - **Метод**: `GET` (для получения списка пользователей) и `POST` (для создания нового пользователя)
   - **Тело запроса** (для создания пользователя):
     ```json
     {
         "username": "newuser",
         "email": "newuser@example.com",
         "password": "yourpassword"
     }
     ```
   - **Ответ** (для получения списка пользователей):
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

2. **Получение токена**
   - **URL**: `accounts/api/token/`
   - **Метод**: `POST`
   - **Тело запроса**:
     ```json
     {
         "username": "yourusername",
         "password": "yourpassword"
     }
     ```
   - **Ответ**:
     ```json
     {
         "refresh": "refresh_token",
         "access": "access_token"
     }
     ```

3. **Обновление токена**
   - **URL**: `accounts/api/token/refresh/`
   - **Метод**: `POST`
   - **Тело запроса**:
     ```json
     {
         "refresh": "refresh_token"
     }
     ```
   - **Ответ**:
     ```json
     {
         "access": "new_access_token"
     }
     ```

## Эндпоинты для получения информации по профилю пользователя

4. Получение профиля пользователя
   - **URL**: `profiles/api/profile/`
   - **Метод**: `GET`
   - **Описание**: Возвращает данные текущего авторизованного пользователя, включая его профиль и список постов.
   - **Ответ**:
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

5. Получение списка постов
   - **URL**: `profiles/api/posts/`
   - **Метод**: `GET`
   - **Описание**: Возвращает список всех постов.
   - **Ответ**:
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

6. Создание нового поста
   - **URL**: `profiles/api/posts/`
   - **Метод**: `POST`
   - **Описание**: Создает новый пост от имени авторизованного пользователя.
   - **Тело запроса**:
     ```json
     {
         "title": "Новый пост",
         "content": "Текст"
     }
     ```
   - **Ответ**:
     ```json
     {
         "id": 3,
         "title": "Новый пост",
         "content": "Текст",
         "created_at": "2024-12-12T15:00:00Z"
     }
     ```
## Эндпоинты для чата

7. Получение списка ВСЕХ чатов и создание нового чата
   - **URL**: `/messenger/api/chatrooms/`
   - **Метод**: `GET` (список чатов), `POST` (создание чата)
   - **Тело запроса** (для создания чата):
     ```json
     {
         "recipient": "username"
     }
     ```
   - **Ответ** (пример списка чатов):
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

8. Получение сообщений в чате и отправка нового сообщения
   - **URL**: `/messenger/api/chatrooms/<room_name>/messages/`
   - **Метод**: `GET` (список сообщений), `POST` (отправка сообщения)
   - **Тело запроса** (для отправки сообщения):
     ```json
     {
         "content": "Привет!"
     }
     ```
   - **Ответ** (пример списка сообщений):
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

9. Получение чатов текущего пользователя
   - **URL**: `/messenger/api/user/chatrooms/`
   - **Метод**: `GET`
   - **Ответ**:
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

10. Подключение к чату через WebSocket
   - **URL**: `/messenger/ws/ws/chat/<room_name>/`
   - **Пример подключения**: 
     ```
     ws = new WebSocket("ws://localhost:8000/messenger/ws/ws/chat/user1_user2/");
     ```
   - **Тело сообщения** (отправка сообщения через WebSocket):
     ```json
     {
         "message": "Привет!"
     }
     ```
   - **Ответ** (сообщение от сервера):
     ```json
     {
         "id": 1,
         "user": "user1",
         "content": "Привет!",
         "timestamp": "2023-12-01T10:00:00Z"
     }
     ```