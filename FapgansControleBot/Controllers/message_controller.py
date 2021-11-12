from telegram import Message, Update, User as TG_User

from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from telegram.ext import CallbackContext

from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from config import BotConfig


def is_fapgans(message: Message) -> bool:
    if message:
        if message.sticker:
            if message.sticker.file_unique_id == BotConfig.FAPGANS_STICKER_ID:
                return True
    return False


class MessageController:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    def handle_sticker(self, update: Update, context: CallbackContext):
        if update.message:
            if is_fapgans(update.message):
                self.handle_fapgans(update.effective_user)

    def handle_fapgans(self, tg_user: TG_User):
        try:
            user: User = self.unit_of_work.get_user_repository().find_user_by_telegram_id(tg_user.id)
        except NoResult:
            user: User = User(tg_user.id, tg_user.username)
            self.unit_of_work.get_user_repository().add(user)
            self.unit_of_work.complete()

        fapgans = Gans(user.user_id)
        self.unit_of_work.get_gans_repository().add(fapgans)
        self.unit_of_work.complete()


