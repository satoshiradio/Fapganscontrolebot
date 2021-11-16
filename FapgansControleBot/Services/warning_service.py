from datetime import datetime

from FapgansControleBot.Models.fapganswarning import FapgansWarning
from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Services.price_service import PriceService
from FapgansControleBot.Views.WarningView import WarningView


class WarningService:
    def __init__(self, unit_of_work: IUnitOfWork, warning_view: WarningView):
        self.unit_of_work = unit_of_work
        self.price_service = PriceService()
        self.warning_view = warning_view

    def register_warning(self, user: User, gans: Gans):
        warning: FapgansWarning = FapgansWarning()
        warning.user_id = user.user_id
        warning.gans_id = gans.gans_id
        warning.date = datetime.utcnow()
        self.unit_of_work.get_warning_repository().add(warning)
