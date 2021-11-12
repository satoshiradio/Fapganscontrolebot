import config
from FapgansControleBot.Repository.CreditRepository.credit_repository import CreditRepository
from FapgansControleBot.Repository.database import Database
from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository
from FapgansControleBot.Repository.i_repository import IRepository
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork

from FapgansControleBot.Repository.UserRepository.i_user_repository import IUserRepository
from FapgansControleBot.Repository.UserRepository.user_repository import UserRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self,
                 database_uri=config.DbConfig.SQLALCHEMY_DATABASE_URI,
                 user_repository: IRepository = None):
        self.database = Database(database_uri)
        self.session = self.database.session()
        # repositories
        self.user_repository = user_repository
        if not self.user_repository:
            self.user_repository = UserRepository(self.session)

        self.credit_repository = user_repository
        if not self.credit_repository:
            self.credit_repository = CreditRepository(self.session)

    def get_user_repository(self) -> IUserRepository:
        return self.user_repository

    def set_user_repository(self, repository: IRepository):
        self.user_repository = repository

    def get_credit_repository(self) -> ICreditRepository:
        return self.credit_repository

    def set_credit_repository(self, repository: IRepository):
        self.user_repository = repository

    def complete(self) -> None:
        self.session.commit()
