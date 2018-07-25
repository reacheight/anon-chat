import telebot
import config
from chat import Chat
from communicator import Communicator

bot = telebot.TeleBot(config.token)
chat = Chat(Communicator(bot))


@bot.message_handler(commands=['start'])
def start_command(message):
    pass


@bot.message_handler(commands=['start_chat'])
def start_chat_command(message):
    user = message.from_user.id
    chat.start(user)


@bot.message_handler(commands=['stop'])
def stop_command(message):
    user = message.from_user.id
    chat.stop(user)


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'video_note',
                                    'caption', 'location'])
def text_message(message):
    user = message.from_user.id
    chat.send_message_to_interlocutor(user, message)


bot.polling(none_stop=True)