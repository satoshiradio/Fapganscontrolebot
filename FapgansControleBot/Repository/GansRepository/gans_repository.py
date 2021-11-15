from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Repository.GansRepository.i_gans_repository import IGansRepository


class GansRepository(IGansRepository):

    def __init__(self, database):
        self.Model = Gans
        super().__init__(database)


