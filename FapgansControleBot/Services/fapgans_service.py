import logging

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Services.user_service import UserService
from FapgansControleBot.Views.WarningView import WarningView

logger = logging.getLogger(__name__)


class FapgansService:
    def __init__(self, unit_of_work: IUnitOfWork, warning_view: WarningView, user_service: UserService):
        self.unit_of_work = unit_of_work
        self.warning_view = warning_view
        self.user_service = user_service

    def handle_fapgans(self, tg_user_id: int, tg_username: str, chat_id: int):

        # user = self.unit_of_work.get_user_repository().find_user_by_telegram_id(tg_user_id)
        user = self.user_service.find_user_or_register(tg_user_id, tg_username)
        gans = self.register_gans(user)
        self.is_valid_gans(chat_id, user, gans)

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

    def register_gans(self, user: User) -> Gans:
        fapgans = Gans(user.user_id)
        self.unit_of_work.get_gans_repository().add(fapgans)
        return fapgans

    def start_gans_period(self, start_price):
        try:
            result: Credit = self.unit_of_work.get_credit_repository().find_credit_by_price(start_price)
        except NoResult:
            logger.info("No credit at this price!")
            return
        result.start()
        self.unit_of_work.complete()