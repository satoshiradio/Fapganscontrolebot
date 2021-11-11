from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Exceptions.user_exceptions import InvalidUserID
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from FapgansControleBot.Repository.i_user_repository import IUserRepository


class UserController:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work
        self.user_repository: IUserRepository = self.unit_of_work.get_user_repository

    def get_user(self, user_id) -> User:
        try:
            user = self.user_repository.get(user_id)
        except NoResult:
            raise InvalidUserID
        return user
