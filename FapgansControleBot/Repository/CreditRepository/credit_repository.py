import datetime

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository


class CreditRepository(ICreditRepository):

    def __init__(self, database):
        self.Model = Credit
        super().__init__(database)

    def find_credit_by_price(self, price: float) -> Credit:
        result: Credit = self.build() \
            .filter(Credit.start_price == price) \
            .filter(Credit.end_time == None).first()
        if not result:
            raise NoResult("No credit at this price")
        return result

    def active_gans_periods(self) -> Credit:
        result: Credit = self.build() \
            .filter(Credit.end_time >= datetime.datetime.utcnow()).first()
        if not result:
            raise NoResult("No credit at this price")
        return result

    def get_unused_credits_lower_or_equal_to_price(self, price: float):
        result: Credit = self.build() \
            .filter(Credit.start_price <= price) \
            .filter(Credit.end_time == None).first()
        if not result:
            raise NoResult("No credit at this price")
        return result




