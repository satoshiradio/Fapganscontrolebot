from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.repository import Repository


class ICreditRepository(Repository[Credit]):
    def find_credit_by_price(self, price: float):
        raise NotImplementedError

    def active_gans_periods(self):
        raise NotImplementedError

    def get_unused_credits_lower_or_equal_to_price(self, price: float):
        raise NotImplementedError
