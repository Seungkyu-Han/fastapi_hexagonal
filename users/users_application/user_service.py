from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt

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
    salt = bcrypt.gensalt()
    encrypted_password: str = bcrypt.hashpw(raw_password.encode('utf-8'), salt).decode()
    user = User(
        user_id=next(snowflake_generator),
        name=name,
        email=Email(email),
        encrypted_password=encrypted_password,
    )

    await user_save(user, db)

    return user