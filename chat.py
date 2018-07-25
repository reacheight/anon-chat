from user_states import UserStates
from random import choice


class Chat:
    def __init__(self, communicator):
        self.communicator = communicator
        self.chat_table = {}
        self.chat_states = {}
        self.chat_queue = []

    def get_user_state(self, user):
        return self.chat_states.get(user, UserStates.IN_MENU)

    def set_user_state(self, user, state):
        self.chat_states[user] = state

    def interlocutor_is_ready(self):
        return len(self.chat_queue) > 0

    def add_to_table(self, first_user, second_user):
        self.chat_table[first_user] = second_user
        self.chat_table[second_user] = first_user

    def connect(self, first_user, second_user):
        self.chat_states[first_user] = self.chat_states[second_user] = UserStates.IN_CHAT
        self.add_to_table(first_user, second_user)

    def notify_about_chat(self, *users):
        for user in users:
            self.communicator.send_text(user, 'Собеседник найден! Начинайте общаться!')

    def notify_about_queue(self, user):
        self.communicator.send_text(user, 'Вы добавлены в очередь. Ожидайте собеседника.')

    def notify_about_interlocutor_stop_chat(self, user):
        self.communicator.send_text(user, 'Ваш собеседник прервал чат.')

    def notify_about_user_stop_chat(self, user):
        self.communicator.send_text(user, 'Вы прервали чат.')

    def notify_about_user_leave_queue(self, user):
        self.communicator.send_text(user, 'Вы покинули очередь.')

    def get_interlocutor(self):
        interlocutor = choice(self.chat_queue)
        self.chat_queue.remove(interlocutor)

        return interlocutor

    def add_to_queue(self, user):
        self.chat_states[user] = UserStates.IN_QUEUE
        self.chat_queue.append(user)

    def find_interlocutor(self, user):
        if self.interlocutor_is_ready():
            interlocutor = self.get_interlocutor()
            self.connect(user, interlocutor)
            self.notify_about_chat(user, interlocutor)

        else:
            self.add_to_queue(user)
            self.notify_about_queue(user)

    def send_message_to_interlocutor(self, user, message):
        interlocutor = self.chat_table[user]
        self.communicator.send_text(interlocutor, message)

    def disconnect(self, user):
        interlocutor = self.chat_table[user]

        del self.chat_table[user]
        del self.chat_table[interlocutor]
        del self.chat_states[user]
        del self.chat_states[interlocutor]

    def stop_chat(self, user):
        interlocutor = self.chat_table[user]
        self.disconnect(user)
        self.notify_about_interlocutor_stop_chat(interlocutor)
        self.notify_about_user_stop_chat(user)

    def remove_from_queue(self, user):
        del self.chat_states[user]
        self.chat_queue.remove(user)
        self.notify_about_user_leave_queue(user)

    def start(self, user):
        user_state = self.get_user_state(user)

        if user_state == UserStates.IN_CHAT:
            # пишем что юзер уже в чате
            pass
        elif user_state == UserStates.IN_QUEUE:
            # пишем что юзер уже в очереди
            pass
        else:
            self.find_interlocutor(user)

    def stop(self, user):
        user_state = self.get_user_state(user)

        if user_state == UserStates.IN_CHAT:
            self.stop_chat(user)
        elif user_state == UserStates.IN_QUEUE:
            self.remove_from_queue(user)
        else:
            # пишем что юзер не в чате и не в очереди
            pass
