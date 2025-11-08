from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from users.users_core.ports.output.users_repository import UserRepository
from users.users_core.user import User
from users.users_infra.entites.user_entity import UserEntity
from users.users_infra.mappers.users_mapper import to_domain, to_entity


class UserRepositoryPg(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def find_by_id(self, user_id: int) -> Optional[User]:
        user_entity: None | UserEntity = await self.db.get(UserEntity, user_id)

        if user_entity:
            return to_domain(user_entity=user_entity)
        return None

    async def save(self, user: User) -> User:
        user_entity: UserEntity = to_entity(user)

        self.db.add(user_entity)

        await self.db.commit()

        return user