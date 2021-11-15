from FapgansControleBot.Models.fapganswarning import FapgansWarning
from FapgansControleBot.Repository.WarningRepository.i_warning_repository import IWarningRepository


class WarningRepository(IWarningRepository):

    def __init__(self, database):
        self.Model = FapgansWarning
        super().__init__(database)


