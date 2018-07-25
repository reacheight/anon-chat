from user_states import UserStates


class Chat:
    def __init__(self):
        self.chat_table = {}
        self.chat_states = {}
        self.chat_queue = []

    def get_user_state(self, user):
        return self.chat_states.get(user, UserStates.IN_MENU)

    def set_user_state(self, user, state):
        self.chat_states[user] = state
