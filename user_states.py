from enum import Enum, auto


class UserStates(Enum):
    IN_CHAT = 'in_chat'
    IN_QUEUE = 'in_queue'
    IN_MENU = 'in_menu'
