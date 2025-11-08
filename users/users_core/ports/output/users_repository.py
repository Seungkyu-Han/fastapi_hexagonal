from abc import ABC, abstractmethod
from typing import Optional
from users.users_core.user import User

class UserRepository(ABC):

    @abstractmethod
    async def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> User:
        pass
