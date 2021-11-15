import config
import requests
import threading
import time


class PriceService:
    def __init__(self,
                 service_uri=config.PriceServiceConfig.SERVICE_URI,
                 poll_interval=config.PriceServiceConfig.POLL_INTERVAL_IN_SECONDS):
        self.service_uri = service_uri
        self.poll_interval = poll_interval
        return

    def start(self, func):
        t = threading.Thread(target=self.do_every_seconds, args=(func,self.poll_interval))
        t.start()

    def get_price(self) -> float:
        try:
            response = requests.get(self.service_uri)
            data = response.json()
            return data["bpi"]["USD"]["rate_float"]
        except requests.exceptions.RequestException:
            return 0

    @staticmethod
    def do_every_seconds(func, seconds):
        start_time = time.time()

        while True:
            func()
            time.sleep(seconds - ((time.time() - start_time) % seconds))
