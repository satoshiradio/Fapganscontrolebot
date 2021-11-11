from telegram.ext import Updater, MessageHandler, Filters

import config
from FapgansControleBot.Controllers.message_controller import MessageController
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
        self.message_controller = MessageController(self.unit_of_work)

        # Start Bot
        self.__process_handlers()
        self.updater.start_polling(poll_interval=POLL_INTERVAL)


    def __process_handlers(self):
        sticker_handler = MessageHandler(Filters.all, self.message_controller.handle_message)
        self.dispatcher.add_handler(sticker_handler)