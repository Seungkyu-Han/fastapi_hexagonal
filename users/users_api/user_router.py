from fastapi import Depends, APIRouter
from snowflake import SnowflakeGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db_session
from config.jwt import auth_guard
from config.snowflake_generator import get_snowflake_generator
from users.users_api.dto.request.create_user_request import CreateUserRequest
from users.users_api.dto.request.login_user_request import LoginUserRequest
from users.users_application.user_service import create_user, login
from users.users_core.user import User
from users.users_infra import get_user_repository
from users.users_infra.repositories.user_repository import UserRepository

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/")
async def create_user_api(
        create_user_request: CreateUserRequest,
        user_repository: UserRepository = Depends(get_user_repository),
        snowflake_generator: SnowflakeGenerator = Depends(get_snowflake_generator),
) -> None:
    await create_user(
        name=create_user_request.name,
        email=create_user_request.email,
        raw_password=create_user_request.password,
        user_repository=user_repository,
        snowflake_generator=snowflake_generator,
    )


@user_router.post("/login")
async def login_api(
        login_user_request: LoginUserRequest,
        user_repository: UserRepository = Depends(get_user_repository)
) -> str:
    return await login(
        email=login_user_request.email,
        raw_password=login_user_request.password,
        user_repository=user_repository,
    )

@user_router.get("/check")
async def check_api(
        authorization: dict = Depends(auth_guard)
):
    print(authorization)