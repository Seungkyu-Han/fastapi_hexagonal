from abc import ABC
from typing import Optional
from users.users_core.users import User

class UserRepository(ABC):

    @classmethod
    async def find_by_id(cls, user_id: int) -> Optional[User]:
        pass

