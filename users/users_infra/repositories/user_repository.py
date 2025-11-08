from sqlalchemy.ext.asyncio import AsyncSession

from users.users_core.user import User
from users.users_core.vo.email import Email
from users.users_infra.entites.user_entity import UserEntity
from users.users_infra.mappers.users_mapper import to_entity, to_domain

class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def user_save(self, user: User) -> User:
        user_entity = to_entity(user)

        self.db.add(user_entity)

        return user


    async def user_find_by_email(self, email: Email) -> User | None:
        from sqlalchemy import select
        user_entity = (await self.db.execute(
            select(UserEntity).where(UserEntity.email == email.value)
        )).scalar_one_or_none()

        if user_entity:
            return to_domain(user_entity)

        return None
