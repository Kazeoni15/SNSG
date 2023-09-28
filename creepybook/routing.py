from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import *

# I wrote this code
app = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/chat/<str:room_id>/", ChatConsumer.as_asgi()),
    ]),
})

# end if code I wrote