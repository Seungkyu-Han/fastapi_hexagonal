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

    def match_password(self, raw_password: str, match_function: Callable[[str, str], bool]) -> bool:
        return match_function(raw_password, self.encrypted_password)