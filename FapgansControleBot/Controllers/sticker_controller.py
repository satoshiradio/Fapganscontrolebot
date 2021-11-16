import logging

from telegram import Message, Update, User as TG_User
from telegram.ext import CallbackContext

from FapgansControleBot.Services.fapgans_service import FapgansService
from config import BotConfig

logger = logging.getLogger(__name__)


def is_fapgans(message: Message) -> bool:
    if message:
        if message.sticker:
            if message.sticker.file_unique_id == BotConfig.FAPGANS_STICKER_ID:
                return True
    return False


class StickerController:
    def __init__(self, fapgans_service: FapgansService):
        self.fapgans_service = fapgans_service

    def handle_sticker(self, update: Update, context: CallbackContext):
        if update.message:
            if is_fapgans(update.message):
                self.handle_fapgans(update.effective_user, update.effective_chat.id)

    def handle_fapgans(self, tg_user: TG_User, chat_id: int):
        logger.info("%s (%s) send a Fapgans!", tg_user.username, tg_user.id)
        self.fapgans_service.handle_fapgans(tg_user.id, tg_user.username, chat_id)
