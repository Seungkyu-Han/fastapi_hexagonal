from typing import Callable


class User:
    id: int
    name: str
    email: str
    encrypted_password: str

    def match_password(self, raw_password: str, match_function: Callable[[str, str], bool]) -> bool:
        return match_function(self.encrypted_password, raw_password)