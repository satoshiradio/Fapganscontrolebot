import config
from Bot.Repository.database import Database
from Bot.Repository.i_repository import IRepository
from Bot.Repository.i_unit_of_work import IUnitOfWork

from Bot.Repository.i_user_repository import IUserRepository
from Bot.Repository.user_repository import UserRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self,
                 database_uri=config.DbConfig.SQLALCHEMY_DATABASE_URI,
                 user_repository_value: IRepository = None):
        self.database = Database(database_uri)
        self.session = self.database.session()
        # repositories
        self.user_repository_value = user_repository_value
        if not self.user_repository_value:
            self.user_repository_value = UserRepository(self.session)

    @property
    def get_user_repository(self) -> IUserRepository:
        return self.user_repository_value

    def set_user_repository(self, repository: IRepository):
        self.user_repository_value = repository

    def complete(self) -> None:
        self.session.commit()
