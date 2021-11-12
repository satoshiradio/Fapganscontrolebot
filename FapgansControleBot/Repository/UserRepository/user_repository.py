from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.UserRepository.i_user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, database):
        self.Model = User
        super().__init__(database)

    def find_user_by_telegram_id(self, user_telegram_id: int) -> User:
        result: User = self.build() \
            .filter(User.user_telegram_id == user_telegram_id).first()
        if not result:
            raise NoResult("No registered user with this telegram ID")
        return result
