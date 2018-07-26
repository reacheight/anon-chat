from user_states import UserStates
from random import choice


class Chat:
    def __init__(self, communicator):
        self.communicator = communicator
        self.chat_table = {}
        self.chat_states = {}
        self.chat_queue = []

    def start(self, user):
        user_state = self.get_user_state(user)

        if user_state == UserStates.IN_CHAT:
            self.notify('Ваш собеседник уже найден.', user)
        elif user_state == UserStates.IN_QUEUE:
            self.notify('Вы уже находитесь в очереди.', user)
        else:
            self.find_interlocutor(user)

    def stop(self, user):
        user_state = self.get_user_state(user)

        if user_state == UserStates.IN_CHAT:
            self.stop_chat(user)
        elif user_state == UserStates.IN_QUEUE:
            self.remove_from_queue(user)
        else:
            self.notify('Вы ещё не начали поиск собеседника.', user)

    def send_message_to_interlocutor(self, user, message):
        user_state = self.get_user_state(user)

        if user_state == UserStates.IN_CHAT:
            interlocutor = self.chat_table[user]
            self.communicator.send_message(interlocutor, message)

    def find_interlocutor(self, user):
        if self.interlocutor_is_ready():
            interlocutor = self.get_interlocutor()
            self.connect(user, interlocutor)
            self.notify('Собеседник найден! Начинайте общаться!', user, interlocutor)

        else:
            self.add_to_queue(user)
            self.notify('Вы добавлены в очередь. Ожидайте собеседника.', user)

    def stop_chat(self, user):
        interlocutor = self.chat_table[user]
        self.disconnect(user)
        self.notify('Ваш собеседник прервал чат.', interlocutor)
        self.notify('Вы прервали чат.', user)

    def remove_from_queue(self, user):
        del self.chat_states[user]
        self.chat_queue.remove(user)
        self.notify('Вы покинули очередь', user)

    def get_interlocutor(self):
        interlocutor = choice(self.chat_queue)
        self.chat_queue.remove(interlocutor)

        return interlocutor

    def connect(self, first_user, second_user):
        self.chat_states[first_user] = self.chat_states[second_user] = UserStates.IN_CHAT
        self.add_to_table(first_user, second_user)

    def disconnect(self, user):
        interlocutor = self.chat_table[user]

        del self.chat_table[user]
        del self.chat_table[interlocutor]
        del self.chat_states[user]
        del self.chat_states[interlocutor]

    def add_to_queue(self, user):
        self.chat_states[user] = UserStates.IN_QUEUE
        self.chat_queue.append(user)

    def add_to_table(self, first_user, second_user):
        self.chat_table[first_user] = second_user
        self.chat_table[second_user] = first_user

    def notify(self, text, *users):
        for user in users:
            self.communicator.notify(user, text)

    def get_user_state(self, user):
        return self.chat_states.get(user, UserStates.IN_MENU)

    def interlocutor_is_ready(self):
        return len(self.chat_queue) > 0
