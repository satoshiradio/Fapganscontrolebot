from telegram import ReplyMarkup, ParseMode
from telegram.ext import Updater


class View:
    def __init__(self, updater: Updater):
        self.updater = updater

    def send_message(self, chat_id: int, text: str, keyboard: ReplyMarkup = None) -> None:
        self.updater.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard,
        )

    def send_error(self, chat_id, text: str, keyboard: ReplyMarkup = None) -> None:
        formatted_text = f'⚠<b>{text}</b>⚠'
        self.send_message(chat_id, formatted_text, keyboard)