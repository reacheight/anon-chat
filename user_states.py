from enum import Enum, auto


class UserStates(Enum):
    IN_CHAT = auto()
    IN_QUEUE = auto()
    IN_MENU = auto()
