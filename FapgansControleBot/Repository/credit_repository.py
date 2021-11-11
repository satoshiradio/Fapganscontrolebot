from FapgansControleBot.Models.credit import Credit
from FapgansControleBot.Repository.i_credit_repository import ICreditRepository


class CreditRepository(ICreditRepository):
    def __init__(self, database):
        self.Model = Credit
        super().__init__(database)
