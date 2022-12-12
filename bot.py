#Библиотека c эмодзи
from emoji import emojize
#Модуль glob находит все файлы по определнному шаблону
from glob import glob
#Журнал логов
import logging
#Импорт settings.py для сокрытия токенов, паролей и личных данных
import settings
#Модуль random отвечает за работу со случайными числами, функция randint - за целые числа; choice - за выбор случайного элемента
from random import randint, choice
#Cтрока конфигурирования журнала 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


#Компонент отвечающий за коммуникацию с сервером Телеги(Updater), за обработку команд(CommandHandler)
logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S')


#Функция вызова приветствия со эмоджи
#update - информация, пришедшая из Телеги(команда 'start', информация о пользователе, которую вызвал эту команду)
#context - когда мы хотим отправить другому пользователю команду
def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Привет, пользователь {context.user_data['emoji']}!")


#Функция ответа пользователю на входящие сообщение
def talk_to_me(update, context):
    #context.user_data: Это словарь: если мы добавим в него ключ с данными, эти данные будут доступны для этого пользователя.
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f"{text} {context.user_data['emoji']}")

#Функция получения смайлика
def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')# smile(текст) преобразуем в иконку смайлика, language='alias'(текстовые обозначения смайликов)
    return user_data['emoji']

#Функция вывода результата, для игры в числа
def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Твое число {user_number}, мое {bot_number}, ты выиграл'
    elif user_number == bot_number:
        message = f'Твое число {user_number}, мое {bot_number}, ничья'
    else:
        message = f'Твое число {user_number}, мое {bot_number}, ты проиграл'
    return message

 
#Функция проверки веденых данных на int, для игры в числа
def guess_number(update, context):
    print(context.args) #вывод в консоль
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except(TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число рядом с командой'
    update.message.reply_text(message)


#Функция отправки случайной картинки в нужный чат
def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*') #получаем список картинок
    cat_photo_filename = choice(cat_photo_list) #выбираем случайную картинку
    chat_id = update.effective_chat.id #получение id чата с текущим пользователем, нужно для картинки
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb')) #'rb' - формат readbinary(двоичный) считывания картинки в питоне


def main():
    #Создаем бота и передаем ему токен для авторизации на серверах Телеги
    mybot = Updater(settings.API_KEY, use_context=True)
    #Используем диспетчер для того, чтобы при наступлении события вызывалась наша функция main(), start - команда, greet_user - вызов функции
    dp = mybot.dispatcher
    #Вызов привествия бота командой /start
    dp.add_handler(CommandHandler('start', greet_user))
    #Вызов игры с ботом командой /guess
    dp.add_handler(CommandHandler('guess', guess_number))
    #Вызов рандомной картинки с котом командой /cat
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    #При использовании MessageHandler указываем, что хотим реагировать только на текстовые события Filters.text, talk_to_me - вызов функции
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #Отображение в сообщения перед запуском бота в bot.log
    logging.info('Бот запустился')
    #Запуск бесконечного цикла запроса и обновлений от бота
    mybot.start_polling()
    #Принудительная остановка CTRL-C
    mybot.idle()


#Запуск бота(исполнение только при прямом вызове, но не при импорте)
if __name__== '__main__':
    main()
