### Эндпоинты

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
