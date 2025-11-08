from fastapi import APIRouter, Depends
from snowflake import SnowflakeGenerator

from config.snowflake_generator import get_snowflake_generator
from users.users_api.dto.request.create_user_request import CreateUserRequest
from users.users_application.user_service import create_user
from users.users_core.user import User

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/")
async def create_user_api(create_user_request: CreateUserRequest, snowflake_generator: SnowflakeGenerator = Depends(get_snowflake_generator)) -> None:
    print(create_user_request)
    user: User = await create_user(
        name=create_user_request.name,
        email=create_user_request.email,
        raw_password=create_user_request.password,
        snowflake_generator=snowflake_generator
    )

    print(user.user_id)