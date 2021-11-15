from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Services.price_service import PriceService
import logging

logger = logging.getLogger(__name__)


class PriceController:
    def __init__(self, unit_of_work: IUnitOfWork):
        # self.logger = logging.getLogger(__name__)
        self.credit_repository: ICreditRepository = unit_of_work.get_credit_repository()
        self.price_service = PriceService()
        self.price_service.start(self.handle_price_action)

    def handle_price_action(self):
        price = self.price_service.get_price()
        try:
            result = self.credit_repository.get_unused_credits_lower_or_equal_to_price(price)
            logger.info('Starting auto-fap at price: {0:.2f}'.format(price))
            result.start()
        except NoResult:
            logger.info('No credit at price: {0:.2f}'.format(price))
