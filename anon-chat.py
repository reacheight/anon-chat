import telebot
import config
from user_states import UserStates
from chat import Chat

bot = telebot.TeleBot(config.token)
chat = Chat(bot)


@bot.message_handler(commands=['start'])
def start_command(message):
    user = message.from_user.id
    user_state = chat.get_user_state(user)

    if user_state == UserStates.IN_CHAT:
        pass
    elif user_state == UserStates.IN_QUEUE:
        pass
    else:
        pass


@bot.message_handler(commands=['start_chat'])
def start_chat_command(message):
    user = message.from_user.id
    user_state = chat.get_user_state(user)

    if user_state == UserStates.IN_CHAT:
        pass
    elif user_state == UserStates.IN_QUEUE:
        pass
    else:
        chat.find_interlocutor(user)


@bot.message_handler(commands=['stop'])
def stop_command(message):
    user = message.from_user.id
    user_state = chat.get_user_state(user)

    if user_state == UserStates.IN_CHAT:
        chat.stop_chat(user)
    elif user_state == UserStates.IN_QUEUE:
        chat.remove_from_queue(user)
    else:
        pass


@bot.message_handler(content_types=['text'])
def text_message(message):
    user = message.from_user.id
    user_state = chat.get_user_state(user)

    if user_state == UserStates.IN_CHAT:
        chat.send_message_to_interlocutor(user, message.text)


bot.polling(none_stop=True)