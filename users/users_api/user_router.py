from fastapi import APIRouter, Depends
from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db_session
from config.snowflake_generator import get_snowflake_generator
from users.users_api.dto.request.create_user_request import CreateUserRequest
from users.users_application.user_service import create_user
from users.users_core.user import User
from users.users_infra.repositories.user_repository import user_save

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/")
async def create_user_api(
        create_user_request: CreateUserRequest,
        snowflake_generator: SnowflakeGenerator = Depends(get_snowflake_generator),
        db: AsyncSession = Depends(get_db_session),
) -> None:
    user: User = await create_user(
        name=create_user_request.name,
        email=create_user_request.email,
        raw_password=create_user_request.password,
        snowflake_generator=snowflake_generator,
        db=db,
    )

    await user_save(user, db)