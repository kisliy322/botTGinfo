import telebot
bot = telebot.TeleBot('')# your api tg bot
name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');
def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text);
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами пожалуйста');
        break
        bot.send_message(message.from_user.id, 'Тебе ' + str(age) +' лет, тебя зовут ' +name+ '' +surname+ '?');
bot.polling(none_stop=True, interval=0)
