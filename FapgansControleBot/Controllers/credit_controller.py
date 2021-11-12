from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler

from FapgansControleBot.Exceptions.database_exceptions import NoResult
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
            CommandHandler("ganzentrek", self.ganzentrek),
            CommandHandler("active", self.active)

        ],
            states={}, fallbacks=[], allow_reentry=True)

    @user_admin
    def give_credits(self, update: Update, context: CallbackContext):
        price = price_formatter(update.message.text.removeprefix("/give_credits "))
        credits = Credit(start_price=price)
        self.unit_of_work.get_credit_repository().add(credits)
        self.unit_of_work.complete()

    @user_admin
    def ganzentrek(self, update: Update, context: CallbackContext):
        price = price_formatter(update.message.text.removeprefix("/ganzentrek "))
        self.start_gans_period(price)

    def active(self, update: Update, context: CallbackContext):
        try:
            result: Credit = self.unit_of_work.get_credit_repository().active_gans_periods()
        except NoResult:
            print("No active credit")
            return
        print(result.credit_id)

    def start_gans_period(self, start_price):
        try:
            result: Credit = self.unit_of_work.get_credit_repository().find_credit_by_price(start_price)
        except NoResult:
            print("No credit at this price!")
            return
        result.start()
        self.unit_of_work.complete()
