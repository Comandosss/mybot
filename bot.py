#журнал логов
import logging
#Компонент отвечающий за коммуникацию с сервером Телеги(Updater),
#за обработку команд(CommandHandler)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#Импорт settings.py для сокрытия токенов, пароль и личных данных
import settings
#Cтрока конфигурирования журнала 
logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S')

#Настройка прокси (не работает прокси-сервер, запустил без него)
#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

#Функция вызова приветствия
#update - информация, пришедшая из Телеги(команда 'start', информация о пользователе, которую вызвал эту команду)
#context - когда мы хотим отправить другому пользователю команду
def greet_user(update, context):
    print('Вызван /start')
    #print(update.message.reply_text('Привет, пользователь!'))
    update.message.reply_text('Привет, пользователь!')

#Функция ответа пользователю на входящие сообщение
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    #Создаем бота и передаем ему токен для авторизации на серверах Телеги
    mybot = Updater(settings.API_KEY, use_context=True) #request_kwargs=PROXY)
    #Используем диспетчер для того, чтобы при наступлении события вызывалась наша функция main(), start - команда, greet_user - вызов функции
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
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


