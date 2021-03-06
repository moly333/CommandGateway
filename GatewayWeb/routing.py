from channels.routing import route
from GatewayWeb.consumers import *


channel_routing = [
    route("websocket.connect", ws_add),
    route('websocket.receive', ws_message),
    route("websocket.disconnect", ws_disconnect),
]