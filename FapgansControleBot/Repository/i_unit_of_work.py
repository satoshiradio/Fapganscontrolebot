from abc import ABC, abstractmethod

from FapgansControleBot.Repository.i_user_repository import IUserRepository
from FapgansControleBot.Repository.i_repository import IRepository


class IUnitOfWork(ABC):
    @abstractmethod
    def get_user_repository(self) -> IUserRepository:
        raise NotImplementedError

    @abstractmethod
    def set_user_repository(self, repository: IRepository):
        raise NotImplementedError

    @abstractmethod
    def complete(self) -> int:
        raise NotImplementedError
