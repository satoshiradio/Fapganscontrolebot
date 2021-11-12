from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.UserRepository.i_user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, database):
        self.Model = User
        super().__init__(database)
