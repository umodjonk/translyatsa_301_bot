from telebot.types import ReplyKeyboardMarkup,KeyboardButton


def Start_btn():
   markub=ReplyKeyboardMarkup(resize_keyboard=True)
   markub.add(
       KeyboardButton('About🥷'),
       KeyboardButton('Translater')
   )
   return markub

def languages_btn():
    markub=ReplyKeyboardMarkup(resize_keyboard=True)
    markub.add(
        KeyboardButton("🇺🇿-🇬🇧"),
        KeyboardButton('🇺🇿-🇷🇺'),
        KeyboardButton('🇺🇿-🇦🇱'),
        KeyboardButton('🇩🇪-🇺🇿'),
        KeyboardButton('🇺🇿-🇩🇪'),
    )
    return markub
