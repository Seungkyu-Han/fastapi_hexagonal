from sqlalchemy.ext.asyncio import AsyncSession

from users.users_core.user import User
from users.users_core.vo.email import Email
from users.users_infra.entites.user_entity import UserEntity
from users.users_infra.mappers.users_mapper import to_entity, to_domain


async def user_save(user: User, db: AsyncSession) -> User:
    user_entity = to_entity(user)

    db.add(user_entity)

    return user


async def user_find_by_email(email: Email, db: AsyncSession) -> User | None:
    from sqlalchemy import select
    user_entity = (await db.execute(
        select(UserEntity).where(UserEntity.email == email.value)
    )).scalar_one_or_none()

    if user_entity:
        return to_domain(user_entity)

    return None
