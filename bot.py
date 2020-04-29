#Bot's token: 1049518862:AAF05gg_kcyOadGX9t8Tm_1fzPsM81mL-go

import telebot


bot = telebot.TeleBot('1049518862:AAF05gg_kcyOadGX9t8Tm_1fzPsM81mL-go')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == 'Привет':
		bot.send_message(message.from_user.id, 'Привет, чем я могу помочь?')
	elif message.tex == '/help':
		bot.send_message(message.from_user.id, 'Напиши привет!')
	else:
		bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help')

bot.polling(none_stop=True, interval=0)