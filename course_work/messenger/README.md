### **Чат (Messenger)**

1. **Получение списка ВСЕХ чатов и создание нового чата**
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

2. **Получение сообщений в чате и отправка нового сообщения**
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

3. **Получение чатов текущего пользователя**
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

#### **WebSocket API**

1. **Подключение к чату через WebSocket**
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