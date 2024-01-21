
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from real_time_collaboration.sockets.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', ChatConsumer.as_asgi()),
    ])
})


# myapp/routing.py
# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'/ws/chat/$', consumers.ChatConsumer.as_asgi()),
# ]



# # real_time_collaboration/sockets/routing.py
# from django.urls import re_path
# from .consumers import ChatConsumer

# websocket_urlpatterns = [
#     re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
# ]

