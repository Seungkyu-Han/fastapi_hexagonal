from sqlalchemy.ext.asyncio import AsyncSession

from users.users_core.user import User
from users.users_infra.mappers.users_mapper import to_entity


async def user_save(user: User, db: AsyncSession)-> User:
    user_entity = to_entity(user)

    db.add(user_entity)

    return user