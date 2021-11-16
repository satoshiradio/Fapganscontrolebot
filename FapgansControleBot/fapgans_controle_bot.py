from telegram.ext import Updater, MessageHandler, Filters

import config
from FapgansControleBot.Controllers.credit_controller import CreditController
from FapgansControleBot.Controllers.sticker_controller import StickerController
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Services.credit_service import CreditService
from FapgansControleBot.Services.fapgans_service import FapgansService
from FapgansControleBot.Services.price_service import PriceService
from FapgansControleBot.Services.user_service import UserService
from FapgansControleBot.Views.WarningView import WarningView

POLL_INTERVAL = 1


class FapgansControleBot:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work: IUnitOfWork = unit_of_work

        # Bot
        self.updater = Updater(token=config.BotConfig.TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Views
        self.warning_view = WarningView(self.updater)

        # Services
        self.user_service = UserService(self.unit_of_work)
        self.credit_service = CreditService(self.unit_of_work)
        self.price_service = PriceService(self.unit_of_work)
        self.fapgans_service = FapgansService(self.unit_of_work, self.warning_view, self.user_service)

        # Controllers
        self.message_controller = StickerController(self.fapgans_service)
        self.credit_controller = CreditController(self.credit_service, self.fapgans_service,)

        # Start Bot
        self.__process_handlers()
        self.updater.start_polling(poll_interval=POLL_INTERVAL)
        self.price_service.start(self.price_service.handle_price_action)
        print("Bot is ready to handle commands and ganzen")

    def __process_handlers(self):
        self.dispatcher.add_handler(self.credit_controller.get_commands())
        sticker_handler = MessageHandler(Filters.sticker, self.message_controller.handle_sticker)
        self.dispatcher.add_handler(sticker_handler)
