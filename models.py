from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    "User Class Repr"
    user_id: int = 0
    screen_name: str = ""
    user: str = ""
    agent: str = ""



@dataclass
class Data:
    "Bot Data Sheet Model"
    name: str = ""
    club_id: int = 0
    agent: str = ""
    agent_rb: int = 0
    ref_code: str = ""
    group_id: int = 0


