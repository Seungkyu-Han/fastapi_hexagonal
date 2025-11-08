from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from config.transactional import transactional
from users.users_core.user import User
from users.users_core.vo.email import Email
from users.users_infra.repositories.user_repository import user_save


@transactional
async def create_user(
        name: str,
        email: str,
        raw_password: str,
        snowflake_generator: SnowflakeGenerator,
        db: AsyncSession
) -> User:
    user = User(
        user_id=next(snowflake_generator),
        name=name,
        email=Email(email),
        encrypted_password=raw_password,
    )

    await user_save(user, db)

    return user