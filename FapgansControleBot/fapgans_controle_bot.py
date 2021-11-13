from telegram.ext import Updater, MessageHandler, Filters

import config
from FapgansControleBot.Controllers.credit_controller import CreditController
from FapgansControleBot.Controllers.sticker_controller import StickerController
from FapgansControleBot.Controllers.user_controller import UserController
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork

POLL_INTERVAL = 1


class FapgansControleBot:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work: IUnitOfWork = unit_of_work

        # Bot
        self.updater = Updater(token=config.BotConfig.TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Controllers
        self.user_controller = UserController(self.unit_of_work)
        self.message_controller = StickerController(self.unit_of_work)
        self.credit_controller = CreditController(self.unit_of_work)

        # Start Bot
        self.__process_handlers()
        self.updater.start_polling(poll_interval=POLL_INTERVAL)
        print("Bot is ready to handle commands and ganzen")

    def __process_handlers(self):
        self.dispatcher.add_handler(self.credit_controller.get_commands())
        sticker_handler = MessageHandler(Filters.sticker, self.message_controller.handle_sticker)
        self.dispatcher.add_handler(sticker_handler)

