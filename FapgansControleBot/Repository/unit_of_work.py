import config
from FapgansControleBot.Repository.database import Database
from FapgansControleBot.Repository.i_repository import IRepository
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork

from FapgansControleBot.Repository.i_user_repository import IUserRepository
from FapgansControleBot.Repository.user_repository import UserRepository


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

    @property
    def get_user_repository(self) -> IUserRepository:
        return self.user_repository

    def set_user_repository(self, repository: IRepository):
        self.user_repository_value = repository

    def complete(self) -> None:
        self.session.commit()
