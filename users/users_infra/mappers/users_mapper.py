from users.users_core.vo.email import Email
from users.users_infra.entites.user_entity import UserEntity
from users.users_core.user import User

def to_domain(user_entity: UserEntity) -> User:
    return User(
        user_id=user_entity.user_id,
        name=user_entity.name,
        email=Email(user_entity.email),
        encrypted_password=user_entity.encrypted_password
    )

def to_entity(user: User) -> UserEntity:
    return UserEntity(
        user_id=user.user_id,
        name=user.name,
        email=user.email.value,
        encrypted_password=user.encrypted_password
    )