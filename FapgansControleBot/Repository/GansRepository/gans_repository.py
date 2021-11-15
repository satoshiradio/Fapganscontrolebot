from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Repository.GansRepository.i_gans_repository import IGansRepository


class GansRepository(IGansRepository):

    def __init__(self, database):
        self.Model = Gans
        super().__init__(database)

    def amount_of_ganzen_by_user_id(self, user_id: int, credit_id: int) -> int:
        return self.build() \
            .filter(Gans.credit_id <= credit_id) \
            .filter(Gans.user_id == user_id) \
            .count()


