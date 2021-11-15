from abc import ABC, abstractmethod

from FapgansControleBot.Repository.CreditRepository.i_credit_repository import ICreditRepository
from FapgansControleBot.Repository.GansRepository.i_gans_repository import IGansRepository
from FapgansControleBot.Repository.UserRepository.i_user_repository import IUserRepository
from FapgansControleBot.Repository.i_repository import IRepository


class IUnitOfWork(ABC):
    @abstractmethod
    def get_user_repository(self) -> IUserRepository:
        raise NotImplementedError

    @abstractmethod
    def set_user_repository(self, repository: IRepository):
        raise NotImplementedError

    @abstractmethod
    def get_credit_repository(self) -> ICreditRepository:
        raise NotImplementedError

    @abstractmethod
    def set_credit_repository(self, repository: IRepository):
        raise NotImplementedError

    @abstractmethod
    def get_gans_repository(self) -> IGansRepository:
        raise NotImplementedError

    @abstractmethod
    def set_gans_repository(self, repository: IRepository):
        raise NotImplementedError

    @abstractmethod
    def complete(self) -> int:
        raise NotImplementedError
