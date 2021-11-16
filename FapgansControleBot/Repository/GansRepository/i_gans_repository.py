from FapgansControleBot.Models.gans import Gans
from FapgansControleBot.Repository.repository import Repository


class IGansRepository(Repository[Gans]):
    pass

    def amount_of_ganzen_by_user_id(self, user_id: int, credit_id: int) -> int:
        raise NotImplementedError
