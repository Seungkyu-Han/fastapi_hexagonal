from typing import Callable
from .vo.email import Email


class User:
    user_id: int
    name: str
    email: Email
    encrypted_password: str

    def __init__(self, user_id: int, name: str, email: Email, encrypted_password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.encrypted_password = encrypted_password

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other) -> bool:
        if isinstance(other, User) and other.user_id == self.user_id:
            return True
        return False

    def match_password(self, raw_password: str, match_function: Callable[[bytes, bytes], bool]) -> bool:
        return match_function(raw_password.encode('utf-8'), self.encrypted_password.encode('utf-8'))
