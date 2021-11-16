import logging

from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler

from FapgansControleBot.Middleware.admin_middleware import user_admin
from FapgansControleBot.Services.credit_service import CreditService
from FapgansControleBot.Services.fapgans_service import FapgansService
from FapgansControleBot.Utils.Price_utils import price_formatter

logger = logging.getLogger(__name__)


class CreditController:
    def __init__(self,
                 credit_service: CreditService,
                 fapgans_service: FapgansService):
        self.fapgans_service = fapgans_service
        self.credit_service = credit_service

    def get_commands(self) -> ConversationHandler:
        return ConversationHandler(entry_points=[
            CommandHandler("give_credits", self.give_credits),
            CommandHandler("ganzentrek", self.ganzentrek)
        ],
            states={}, fallbacks=[], allow_reentry=True)

    @user_admin
    def give_credits(self, update: Update, context: CallbackContext):
        price = price_formatter(update.message.text.removeprefix("/give_credits "))
        logger.info("Giving %s credits", price)
        self.credit_service.register_credit(price)

    @user_admin
    def ganzentrek(self, update: Update, context: CallbackContext):
        logger.info("Ganzentrek")
        price = price_formatter(update.message.text.removeprefix("/ganzentrek "))
        self.fapgans_service.start_gans_period(price)
