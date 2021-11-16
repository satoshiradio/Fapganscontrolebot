from FapgansControleBot.Exceptions.database_exceptions import NoResult
from FapgansControleBot.Exceptions.user_exceptions import InvalidUserID
from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork


class UserService:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work
        self.user_repository = self.unit_of_work.get_user_repository()

    def register_user(self, telegram_id: int, username: str) -> User:
        user: User = User(telegram_id, username)
        self.user_repository.add(user)

        self.unit_of_work.complete()
        return user

    def find_user_or_register(self, tg_user_id: int, username: str) -> User:
        try:
            return self.user_repository.find_user_by_telegram_id(tg_user_id)
        except NoResult:
            return self.register_user(tg_user_id, username)

    def get_user(self, user_id) -> User:
        try:
            user = self.user_repository.get(user_id)
        except NoResult:
            raise InvalidUserID
        return user
