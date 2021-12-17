import telebot
from telebot import types

bot = telebot.TeleBot('5049822153:AAF_vCDWlGtTsR2dfasB9-inwQ-PEjzsVCM')
#  qwer это старт бота
@bot.message_handler(commands=['qwer'])
def welcom(message): # создаем функцию которая приветствует пользователя при нажатии старта

    photo = open('app.jpeg', 'rb') # перердаем с помошью функции "open" картинку в формате "jpeg"

    bot.send_photo(message.chat.id, photo) # тут предаем message-в чат телеграмма photo это переменная

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # 1. переменная markup.
                                                             # 2.types указывем тип кнопок
                                                             # 3.ReplyKeyboardMarkup
                                                             # 4.resize_keyboard=True пускай выводит мне следуюшие кнопки

    button1 = types.KeyboardButton('Идем дальше') # первая созданная кнопка которая высвечивает
                                         # сообщение 'Идем дальше'
    bot.send_message(message.chat.id,
                     f'Привет, тут у тебя есть возможность найти  {message.from_user}',
                     reply_markup=markup)

    button2 = types.KeyboardButton('Купить смартфон') # тут добавляем кнопку еше одну с помошью переменной 'button2'
                                                # и передаем ей тип кнопки 'types'-'KeyboardButton'

    markup.add(button1,button2) # в переменну 'markup' мы добавляем
                                # эти две переменные в которых есть кнопки "button1", "button2"
# создаем декоратор в которую заварачиваем все кнопки
@bot.message_handler(content_types = ['text'])
def aswer(message):

    if message.text == "GO":
        bot.send_message(message.chat.id, 'welcom to eyes sauron')
    elif message.text == 'BUYiphone':

        markup = types.InlineKeyboardMarkup(row_width=3)

        button3= types.InlineKeyboardButton("iphone",
                                            callback_data='iphone')

        button4 = types.InlineKeyboardButton("iphone 2",
                                             callback_data='iphone 2')

        button5 = types.InlineKeyboardButton("iphone 3",
                                             callback_data='iphone 3')

        markup.add(button3,button4,button5)

        bot.send_message(message.chat.id,
                         'Какую марку айфона вы хотите?',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'error')

@bot.callback_query_handler(func=lambda call : True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'iphone':
                bot.send_message(call.message.chat.id,
                                 '500$')

            if call.data == 'iphone 2':
                bot.send_message(call.message.chat.id,
                                     '600$')

            if call.data == 'iphone 3':
                bot.send_message(call.message.chat.id,
                                     '700$')

    except:
        print('error')



bot.polling(none_stop=True)
