from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler

from FapgansControleBot.Middleware.admin_middleware import user_admin
from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Utils.Price_utils import price_formatter


class CreditController:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    def get_commands(self) -> ConversationHandler:
        return ConversationHandler(entry_points=[
            CommandHandler("give_credits", self.give_credits),

        ],
            states={}, fallbacks=[], allow_reentry=True)

    @user_admin
    def give_credits(self, update: Update, context: CallbackContext):
        text = update.message.text
        price = price_formatter(text.split(' ')[1])
        credits = Credit(start_price=price)
        self.unit_of_work.get_credit_repository().add(credits)
        self.unit_of_work.complete()
