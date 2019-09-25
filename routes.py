import telebot
from telebot import types
from telebot import apihelper

themes = ['Парадоксы', 'Лингвистика']
add_commands = ['/themes']

apihelper.proxy = {'tg':'tg://proxy?server=tg2.lksh.ru&port=443&secret=dd303d674c54861cf90d9811ac09aa7e40'}

bot = telebot.TeleBot('910318393:AAGXDLpPQBBpC4POTy35Tcd5km_wMEapT8I')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	website = types.InlineKeyboardButton(text = 'Перейти на сайт', url = 'problems.ru')
	markup.add(website)
	bot.send_message(message.chat.id, 'Привет! Чтобы узнать о возможностях бота, напиши: ' + '/help', reply_markup = markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'У бота имеются следующие дополнительные команды: ' + str(*add_commands))

@bot.message_handler(commands=['themes'])
def send_welcome(message):
	#BUTTONS MARKUP
	markup = types.InlineKeyboardMarkup()
	paradox = types.InlineKeyboardButton(text = 'Парадоксы', callback_data = 'Парадоксы')
	lingua = types.InlineKeyboardButton(text = 'Лингвистика', callback_data = 'Лингвистика')
	markup.add(paradox, lingua)
	bot.send_message(message.chat.id, 'Выбери одну тему', reply_markup=markup)
	#KEYBOARD MARKUP
	# markup = types.ReplyKeyboardMarkup(row_width = 2)
	# theme1 = types.KeyboardButton('Парадоксы')
	# theme2 = types.KeyboardButton('Лингвистика')
	# markup.row(theme1, theme2)
	# bot.send_message(message.chat.id, 'Выбери одну тему', reply_markup=markup)

@bot.callback_query_handler(func = lambda c: True)
def inline(c):
	if c.data == 'Парадоксы':
		bot.send_message(c.message.chat.id, 'Вот пример парадокса:', reply_markup=None)
		bot.send_message(c.message.chat.id, 'У деда Мороза бесконечное число конфет. '
											+ 'За минуту до Нового года дед Мороз дает детям 100 конфет, '
											+ 'а Снегурочка одну конфету отбирает. '
											+ 'За полминуты до наступления Нового года дед Мороз дает детям еще 100 конфет, '
											+ 'а Снегурочка снова одну конфету отбирает. '
											+ 'То же самое повторяется за 15 секунд, за 7,5 секунд и т.д. до Нового года. '
											+ 'Докажите, что Снегурочка сможет к Новому году отобрать у детей все конфеты.')
	elif c.data == 'Лингвистика':
		bot.send_message(c.message.chat.id, 'Вот пример лингвистической задачи:', reply_markup=None)
		bot.send_message(c.message.chat.id, 'Все считали, что Дракон был однооким, двуухим, треххвостым, четырехлапым и пятииглым. '
											+ 'На самом деле, только четыре из этих определений выстраиваются '
											+ 'в определенную закономерность, а одно — лишнее. Какое?')


@bot.message_handler(content_types=['text'])
def echo_all(message):
	if (message.text == 'Парадоксы'):
		bot.send_message(message.chat.id, 'Вот пример парадокса:', reply_markup=None)
		bot.send_message(message.chat.id, 'У деда Мороза бесконечное число конфет. '
											+ 'За минуту до Нового года дед Мороз дает детям 100 конфет, '
											+ 'а Снегурочка одну конфету отбирает. '
											+ 'За полминуты до наступления Нового года дед Мороз дает детям еще 100 конфет, '
											+ 'а Снегурочка снова одну конфету отбирает. '
											+ 'То же самое повторяется за 15 секунд, за 7,5 секунд и т.д. до Нового года. '
											+ 'Докажите, что Снегурочка сможет к Новому году отобрать у детей все конфеты.')
	elif (message.text == 'Лингвистика'):
		bot.send_message(message.chat.id, 'Вот пример лингвистической задачи:', reply_markup=None)
		bot.send_message(message.chat.id, 'Все считали, что Дракон был однооким, двуухим, треххвостым, четырехлапым и пятииглым. '
											+ 'На самом деле, только четыре из этих определений выстраиваются '
											+ 'в определенную закономерность, а одно — лишнее. Какое?')
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=None)

print('Working')

if (__name__ == '__main__'):
	bot.polling(none_stop = True)