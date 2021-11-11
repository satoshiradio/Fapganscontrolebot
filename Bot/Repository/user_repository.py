from Bot.Models.user import User
from Bot.Repository.i_user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, database):
        self.Model = User
        super().__init__(database)
