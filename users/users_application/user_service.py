import snowflake
from snowflake import SnowflakeGenerator

from users.users_core.user import User
from users.users_core.vo.email import Email


async def create_user(name: str, email: str, raw_password: str, snowflake_generator: SnowflakeGenerator) -> User:
    user = User(
        user_id=next(snowflake_generator),
        name=name,
        email=Email(email),
        encrypted_password=raw_password,
    )

    return user

