from FapgansControleBot.Models.user import User
from FapgansControleBot.Repository.repository import Repository


class IUserRepository(Repository[User]):
    pass

    def find_user_by_telegram_id(self, user_telegram_id: int) -> User:
        raise NotImplementedError
