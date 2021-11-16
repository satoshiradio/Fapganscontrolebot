import config
from FapgansControleBot.Repository.CreditRepository.credit_repository import CreditRepository
from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository
from FapgansControleBot.Repository.GansRepository.gans_repository import GansRepository
from FapgansControleBot.Repository.GansRepository.i_gans_repository import IGansRepository
from FapgansControleBot.Repository.UserRepository.i_user_repository import IUserRepository
from FapgansControleBot.Repository.UserRepository.user_repository import UserRepository
from FapgansControleBot.Repository.WarningRepository.i_warning_repository import IWarningRepository
from FapgansControleBot.Repository.WarningRepository.warning_repository import WarningRepository
from FapgansControleBot.Repository.database import Database
from FapgansControleBot.Repository.i_repository import IRepository
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self,
                 database_uri=config.DbConfig.SQLALCHEMY_DATABASE_URI,
                 user_repository: IRepository = None,
                 credit_repository: IRepository = None,
                 gans_repository: IRepository = None,
                 warning_repository: IRepository = None):
        self.database = Database(database_uri)
        self.session = self.database.session()
        # repositories
        self.user_repository = user_repository
        if not self.user_repository:
            self.user_repository = UserRepository(self.session)

        self.credit_repository = credit_repository
        if not self.credit_repository:
            self.credit_repository = CreditRepository(self.session)

        self.gans_repository = gans_repository
        if not self.gans_repository:
            self.gans_repository = GansRepository(self.session)

        self.warning_repository = warning_repository
        if not self.warning_repository:
            self.warning_repository = WarningRepository(self.session)

    def get_user_repository(self) -> IUserRepository:
        return self.user_repository

    def set_user_repository(self, repository: IRepository) -> None:
        self.user_repository = repository

    def get_credit_repository(self) -> ICreditRepository:
        return self.credit_repository

    def set_credit_repository(self, repository: IRepository) -> None:
        self.user_repository = repository

    def get_gans_repository(self) -> IGansRepository:
        return self.gans_repository

    def set_gans_repository(self, repository: IRepository) -> None:
        self.gans_repository = repository

    def set_warning_repository(self, repository: IRepository):
        self.warning_repository = repository

    def get_warning_repository(self) -> IWarningRepository:
        return self.warning_repository

    def complete(self) -> None:
        self.session.commit()
