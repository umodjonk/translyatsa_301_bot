from telebot.types import Message,ReplyKeyboardRemove

from deep_translator import GoogleTranslator

from  loader import bot

from keyboards.defaoult import *

UZB='UZ'
RUS='RU'
ENG='GB'
Alb='Al'
Nem='DE'

@bot.message_handler(func=lambda message:message.text=='Translater')
def reaction_translater(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,"Tilni tanlang",reply_markup=languages_btn())

@bot.message_handler(func=lambda message:message.text=="UZ-EN")
def translater(message:Message):
    chat_id=message.chat.id
    svg=bot.send_message(chat_id,"tarjima qilmoqchi bolgan sozni yuboring")
    bot.register_next_step_handler(svg,translate_UZ_GB)

def translate_UZ_GB(message:Message):
    chat_id=message.chat.id
    bot.reply_to(message,GoogleTranslator(source=UZB,target=ENG).translate(message.text))

@bot.message_handler(func=lambda message:message.text=="🇺🇿-🇬🇧")
def translator(message:Message):
    chat_id=message.chat.id
    svg=bot.send_message(chat_id,"tarjima qilmoqchi bolgan sozni yuboring")
    bot.register_next_step_handler(svg,translate_UZ_RU)

def translate_UZ_RU(messsage:Message):
    chat_id=messsage.chat.id
    bot.reply_to(messsage,GoogleTranslator(source=UZB,target=RUS).translate(messsage.text))




@bot.message_handler(func=lambda message:message.text=="🇺🇿-🇦🇱")
def translator(message:Message):
    chat_id=message.chat.id
    svg=bot.send_message(chat_id,"tarjima qilmoqchi bolgan sozni yuboring")
    bot.register_next_step_handler(svg,translate_UZ_Al)


def translate_UZ_Al(messsage:Message):
    chat_id=messsage.chat.id
    bot.reply_to(messsage,GoogleTranslator(source=UZB,target=Alb).translate(messsage.text))

@bot.message_handler(func=lambda message:message.text=="🇩🇪-🇺🇿")
def translator(message:Message):
    chat_id=message.chat.id
    svg=bot.send_message(chat_id,"tarjima qilmoqchi bolgan sozni yuboring")
    bot.register_next_step_handler(svg,translate_DE_UZ)


def translate_DE_UZ(messsage:Message):
    chat_id=messsage.chat.id
    bot.reply_to(messsage,GoogleTranslator(source=UZB,target=Nem).translate(messsage.text))






