from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    "User Class Repr"
    user_id: int = 0
    screen_name: str = ""
    user: str = ""
    agent: str = ""
