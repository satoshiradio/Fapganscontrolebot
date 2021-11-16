import logging
import threading
import time

import requests

import config
from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork

logger = logging.getLogger(__name__)


class PriceService:
    def __init__(self,
                 unit_of_work: IUnitOfWork,
                 service_uri=config.PriceServiceConfig.SERVICE_URI,
                 poll_interval=config.PriceServiceConfig.POLL_INTERVAL_IN_SECONDS):
        self.service_uri = service_uri
        self.poll_interval = poll_interval
        self.unit_of_work = unit_of_work
        self.credit_repository = self.unit_of_work.get_credit_repository()

    def start(self, func):
        t = threading.Thread(target=self.do_every_seconds, args=(func, self.poll_interval))
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

    def handle_price_action(self):
        price = self.get_price()
        try:
            result = self.credit_repository.get_unused_credits_lower_or_equal_to_price(price)
            logger.info('Starting auto-fap at price: {0:.2f}'.format(price))
            # result.start()
        except NoResult:
            logger.info('No credit at price: {0:.2f}'.format(price))
