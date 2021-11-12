import requests
import time

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork


class PriceController:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.credit_repository: ICreditRepository = unit_of_work.get_credit_repository()

    @staticmethod
    def get_price() -> float:
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            data = response.json()
            return data["bpi"]["USD"]["rate_float"]
        except requests.exceptions.RequestException:
            return 0

    @staticmethod
    def do_every(func, seconds):
        start_time = time.time()

        while True:
            func()
            time.sleep(seconds - ((time.time() - start_time) % seconds))

    def start(self):
        self.do_every(self.handle_price_action, 60)

    def handle_price_action(self):
        try:
            price = self.get_price()
            print(price)
            result = self.credit_repository.get_unused_credits_lower_or_equal_to_price(price)
            result.start()
        except NoResult:
            print('No credit at this price: {0:.2f}'.format(price))
