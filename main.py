import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = "7407976869:AAEV2aVcfClySzGKzlJXxH3RkSCKoT816XM"

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def get_text_messages(message):
#     bot.send_message(message.chat.id, 'Привет! Я телеграмм-бот, который умеет повышает активность на сайте. Что-бы начать со мной работать напиши url сайта.')

# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     number = [int(x) for x in message.text.split("+")]
#     # print(", ".join(number))
#     sum = 0
#     for i in number:
#         sum += i
#     bot.reply_to(message, "Сумма: "+str(sum))

@bot.message_handler(content_types=['text'])
def keyboard_test(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text="testing", reply_markup=keyboard)

chat_id = ""

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    chat_id = call.message.chat.id
    if call.data == "yes":
        bot.send_photo(chat_id=chat_id, photo=open('cat.png', 'rb'))
    elif call.data == "no":
        bot.send_photo(chat_id=chat_id, photo=open('cat2.png', 'rb'))

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Menu 1', callback_data='m1')],
              [InlineKeyboardButton('Menu 2', callback_data='m2')],
              [InlineKeyboardButton('Menu 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def show_main_menu(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('Меню 1', callback_data='m1'))
    keyboard.row(types.InlineKeyboardButton('Меню 2', callback_data='m2'))
    keyboard.row(types.InlineKeyboardButton('Меню 3', callback_data='m3'))
    bot.send_message(chat_id, 'Главное меню:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def get_chat_id(message):
    print(message.chat.id)
    bot.stop_polling()

show_main_menu(chat_id=chat_id)

bot.polling(none_stop=True)
