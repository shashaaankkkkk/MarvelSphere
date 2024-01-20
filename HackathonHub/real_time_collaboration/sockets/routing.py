from django.urls import re_path
from .consumers import CodeEditorConsumer

websocket_urlpatterns = [
    re_path(r'ws/code-editor/(?P<room_code>\w+)/$', CodeEditorConsumer.as_asgi()),
]
