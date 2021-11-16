from telegram.ext import Updater
from telegram.utils.helpers import mention_html

from FapgansControleBot.Models.user import User
from FapgansControleBot.Views.View import View


class WarningView(View):
    def __init__(self, updater: Updater):
        super().__init__(updater)

    def too_many_ganzen(self, chat_id: int, user: User, gans_count: int):
        self.send_error(chat_id,
                        f'{mention_html(user.user_telegram_id, user.user_username)} heeft {gans_count} ganzen gestuurd.')

    def not_in_gans_period(self, chat_id: int, user: User):
        self.send_error(chat_id,
                        f'{mention_html(user.user_telegram_id, user.user_username)} heeft een gans gestuurd. Je bent te vroeg of te laat.')
