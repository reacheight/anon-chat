class Communicator:
    def __init__(self, bot):
        self.bot = bot

    def send_text(self, user, text):
        self.bot.send_message(user, text)