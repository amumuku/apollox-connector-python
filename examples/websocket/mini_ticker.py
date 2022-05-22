import time
import logging
from apollox.lib.utils import config_logging
from apollox.websocket.client.stream import WebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

my_client = Client()
my_client.start()

my_client.mini_ticker(
    id=1,
    callback=message_handler,
    symbol="btcusdt"
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()
