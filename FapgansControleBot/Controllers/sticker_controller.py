import datetime

from telegram import Message, Update, User as TG_User

from FapgansControleBot.Controllers.fapgans_controller import FapgansController
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from FapgansControleBot.Models.fapganswarning import FapgansWarning
from telegram.ext import CallbackContext

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Views import WarningView
from config import BotConfig
import logging

logger = logging.getLogger(__name__)


def is_fapgans(message: Message) -> bool:
    if message:
        if message.sticker:
            if message.sticker.file_unique_id == BotConfig.FAPGANS_STICKER_ID:
                return True
    return False


class StickerController:
    def __init__(self, unit_of_work: IUnitOfWork, warning_view: WarningView):
        self.unit_of_work = unit_of_work
        self.warning_view = warning_view
        self.fapgans_controller = FapgansController(self.unit_of_work, self.warning_view)

    def handle_sticker(self, update: Update, context: CallbackContext):
        if update.message:
            if is_fapgans(update.message):
                self.handle_fapgans(update.effective_user, update.effective_chat.id)

    def handle_fapgans(self, tg_user: TG_User, chat_id: int):
        logger.info("%s (%s) send a Fapgans!", tg_user.username, tg_user.id)
        self.validate_fapgans(tg_user, chat_id)

    def register_gans(self, user: User) -> Gans:
        fapgans = Gans(user.user_id)
        self.unit_of_work.get_gans_repository().add(fapgans)
        return fapgans

    def find_user_or_register(self, tg_user_id: int, username: str) -> User:
        try:
            return self.unit_of_work.get_user_repository().find_user_by_telegram_id(tg_user_id)
        except NoResult:
            return self.register_user(tg_user_id, username)

    def register_user(self, telegram_id: int, username: str) -> User:
        user: User = User(telegram_id, username)
        self.unit_of_work.get_user_repository().add(user)
        self.unit_of_work.complete()
        return user

    def validate_fapgans(self, tg_user: TG_User, chat_id: int):
        user: User = self.find_user_or_register(tg_user.id, tg_user.username)
        gans = self.register_gans(user)
        self.unit_of_work.complete()
        is_valid: bool = self.fapgans_controller.is_valid_gans(chat_id, user, gans)
        if not is_valid:
            self.register_warning(user, gans)
        self.unit_of_work.complete()

    def register_warning(self, user: User, gans: Gans):
        warning: FapgansWarning = FapgansWarning()
        warning.user_id = user.user_id
        warning.gans_id = gans.gans_id
        warning.date = datetime.datetime.utcnow()
        self.unit_of_work.get_warning_repository().add(warning)
