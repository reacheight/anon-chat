from user_states import UserStates
from random import choice


class Chat:
    def __init__(self, bot):
        self.bot = bot
        self.chat_table = {}
        self.chat_states = {}
        self.chat_queue = []

    def get_user_state(self, user):
        return self.chat_states.get(user, UserStates.IN_MENU)

    def set_user_state(self, user, state):
        self.chat_states[user] = state

    def is_ready(self):
        return len(self.chat_queue) > 0

    def add_to_table(self, first_user, second_user):
        self.chat_table[first_user] = second_user
        self.chat_table[second_user] = first_user

    def connect(self, first_user, second_user):
        self.chat_states[first_user] = self.chat_states[second_user] = UserStates.IN_CHAT
        self.add_to_table(first_user, second_user)

    def notify_about_chat(self, user):
        self.bot.send_message(user, 'Собеседник найден! Начинайте общаться!')

    def notify_about_queue(self, user):
        self.bot.send_message(user, 'Вы добавлены в очередь. Ожидайте собеседника.')

    def find_interlocutor(self, user):
        if self.is_ready():
            interlocutor = choice(self.chat_queue)
            self.chat_queue.remove(interlocutor)
            self.connect(user, interlocutor)
            self.notify_about_chat(user)
            self.notify_about_chat(interlocutor)

        else:
            self.chat_queue.append(user)
            self.notify_about_queue(user)

    def send_message_to_interlocutor(self, user, message):
        interlocutor = self.chat_table[user]
        self.bot.send_message(interlocutor, message)
