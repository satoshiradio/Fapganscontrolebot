from telegram.ext import Updater
from telegram.utils.helpers import mention_html

from FapgansControleBot.Models.user import User
from FapgansControleBot.Views.View import View


class WarningView(View):
    def __init__(self, updater: Updater):
        super().__init__(updater)

    def too_many_ganzen(self, admins: dict[str, str], chat_id: int, user: User, gans_count: int):
        self.send_error(chat_id,
                        f'{mention_html(user.user_telegram_id, user.user_username)} heeft {gans_count} ganzen gestuurd en dat is te veel.', self.create_mentions(admins))

    def not_in_gans_period(self, admins: dict[str, str], chat_id: int, user: User):
        self.send_error(chat_id,
                        f'{mention_html(user.user_telegram_id, user.user_username)} heeft zomaar een gans gestuurd!', self.create_mentions(admins))

    def create_mentions(self, admins):
        mentions = []
        for username, userid in admins.items():
            mentions.append(mention_html(userid, username))
        return ', '.join(mentions)
