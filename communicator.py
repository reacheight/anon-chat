class Communicator:
    def __init__(self, bot):
        self.bot = bot

    def notify(self, user, text):
        self.bot.send_message(user, text)

    def send_message(self, user, message):
        # TODO распарсить телеграм-сообщение и отправить по новому адрессу
        pass
