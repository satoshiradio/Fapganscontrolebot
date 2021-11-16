import logging

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Services.price_service import PriceService
from FapgansControleBot.Views.WarningView import WarningView

logger = logging.getLogger(__name__)


class FapgansController:
    def __init__(self, unit_of_work: IUnitOfWork, warning_view: WarningView):
        self.unit_of_work = unit_of_work
        self.price_service = PriceService()
        self.warning_view = warning_view

    def is_valid_gans(self, chat_id: int, user: User, gans: Gans) -> bool:
        try:
            current_period: Credit = self.current_gans_period()
        except NoResult:
            logger.info("Not in a gans period")
            self.warning_view.not_in_gans_period(chat_id,user)
            return False
        gans.credit_id = current_period.credit_id
        amount_of_ganzen = self.amount_of_ganzen_in_credit(user.user_id, current_period.credit_id)
        if amount_of_ganzen > current_period.amount_of_stickers:
            logger.info(f'User ({user.user_username}) sent too many fapganzen')
            self.warning_view.too_many_ganzen(chat_id, user, amount_of_ganzen)
            return False
        return True

    def current_gans_period(self) -> Credit:
        return self.unit_of_work.get_credit_repository().active_gans_periods()

    def amount_of_ganzen_in_credit(self, user_id: int, credit_id: int) -> int:
        return self.unit_of_work.get_gans_repository().amount_of_ganzen_by_user_id(user_id, credit_id)
