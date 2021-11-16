import logging

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork

logger = logging.getLogger(__name__)


class CreditService:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    def start_gans_period(self, start_price):
        try:
            result: Credit = self.unit_of_work.get_credit_repository().find_credit_by_price(start_price)
        except NoResult:
            logger.info("No credit at this price!")
            return
        result.start()
        self.unit_of_work.complete()

    def register_credit(self, price):
        new_credits = Credit(start_price=price)
        self.unit_of_work.get_credit_repository().add(new_credits)
        self.unit_of_work.complete()

