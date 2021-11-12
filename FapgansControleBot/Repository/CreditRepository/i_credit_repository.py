from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.repository import Repository


class ICreditRepository(Repository[Credit]):
    def find_credit_by_price(self, price: int):
        raise NotImplementedError

    def active_gans_periods(self):
        raise NotImplementedError
