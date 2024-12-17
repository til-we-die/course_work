import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from messenger import routing

# Инициализация Django
django.setup()

# Устанавливаем переменную окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_work.settings')

# Настройка ASGI приложения
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Для обработки HTTP-запросов
    "websocket": AuthMiddlewareStack(  # Для обработки WebSocket-соединений
        URLRouter(
            routing.websocket_urlpatterns  # Роутинг для WebSocket
        )
    ),
})
