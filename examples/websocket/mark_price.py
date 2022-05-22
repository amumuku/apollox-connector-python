import time
import logging
from apollox.lib.utils import config_logging
from apollox.websocket.client.stream import WebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

my_client = Client()
my_client.start()

my_client.mark_price(
    symbol="btcusdt",
    id=13,
    speed=1,
    callback=message_handler,
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()
