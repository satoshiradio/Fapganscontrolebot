from datetime import datetime

from FapgansControleBot.Models.fapganswarning import FapgansWarning
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork


class StickerService:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    def register_warning(self, user: User, gans: Gans):
        warning: FapgansWarning = FapgansWarning()
        warning.user_id = user.user_id
        warning.gans_id = gans.gans_id
        warning.date = datetime.utcnow()
        self.unit_of_work.get_warning_repository().add(warning)

    def validate_fapgans(self, user: User, chat_id: int):
        gans = self.register_gans(user)
        self.unit_of_work.complete()
        is_valid: bool = self.fapgans_service.is_valid_gans(chat_id, user, gans)
        if not is_valid:
            self.register_warning(user, gans)
        self.unit_of_work.complete()
