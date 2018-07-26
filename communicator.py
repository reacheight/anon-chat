from string_formatting import *


class Communicator:
    def __init__(self, bot):
        self.bot = bot

    def notify(self, user, text):
        self.bot.send_message(user, italic(text), parse_mode='Markdown')

    def send_message(self, user, message):
        text = message.text
        audio = message.audio
        document = message.document
        photo = message.photo
        sticker = message.sticker
        video = message.video
        voice = message.voice
        video_note = message.video_note
        caption = message.caption
        location = message.location

        if text:
            self.bot.send_message(user, fold('Собеседник: ') + screen_markdown(text), parse_mode='Markdown')
        elif audio:
            self.bot.send_audio(user, audio.file_id, caption=caption)
        elif document:
            self.bot.send_document(user, document.file_id, caption=caption)
        elif photo:
            self.bot.send_photo(user, photo[-1].file_id, caption=caption)
        elif sticker:
            self.bot.send_sticker(user, sticker.file_id)
        elif video:
            self.bot.send_video(user, video.file_id, caption=caption)
        elif voice:
            self.bot.send_voice(user, voice.file_id, caption=caption)
        elif video_note:
            self.bot.send_video_note(user, video_note.file_id)
        elif location:
            self.bot.send_location(user, location.latitude, location.longitude)