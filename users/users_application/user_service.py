import os

from datetime import datetime, timedelta, timezone

from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt
import jwt

from config.transactional import transactional
from users.users_core.user import User
from users.users_core.vo.email import Email
from users.users_infra.repositories.user_repository import UserRepository

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 60))


# @transactional
async def create_user(
        name: str,
        email: str,
        raw_password: str,
        user_repository: UserRepository,
        snowflake_generator: SnowflakeGenerator,
) -> User:
    salt = bcrypt.gensalt()
    encrypted_password: str = bcrypt.hashpw(raw_password.encode('utf-8'), salt).decode()
    user = User(
        user_id=next(snowflake_generator),
        name=name,
        email=Email(email),
        encrypted_password=encrypted_password,
    )

    await user_repository.user_save(user)

    return user


async def login(
        email: str,
        raw_password,
        user_repository: UserRepository
) -> str:
    user: User | None = await user_repository.user_find_by_email(email=Email(email))

    if not user:
        raise Exception

    if not user.match_password(raw_password=raw_password, match_function=bcrypt.checkpw):
        raise Exception

    expire_time = datetime.now(tz=timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    payload = {
        "sub": str(user.user_id),
        "email": user.email.value,
        "exp": expire_time,
        "iat": datetime.now(tz=timezone.utc)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token
