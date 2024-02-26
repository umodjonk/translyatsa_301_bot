from telebot.types import Message,ReplyKeyboardRemove

from  loader import bot

from keyboards.defaoult import *

@bot.message_handler(commands=['start'])
def reaction_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,f'Assalomu alaykum{message.from_user.full_name}',reply_markup=Start_btn())