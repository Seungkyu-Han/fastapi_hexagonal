from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db_session
from users.users_infra.repositories.user_repository import UserRepository


async def get_user_repository(
        db: AsyncSession = Depends(get_db_session)
) -> UserRepository:
    return UserRepository(db)