#Журнал логов
import logging
#Cтрока конфигурирования журнала 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, guess_number, send_cat_picture, user_coordinates, 
                        talk_to_me)
#Импорт settings.py для сокрытия токенов, паролей и личных данных
import settings

#Компонент отвечающий за коммуникацию с сервером Телеги(Updater), за обработку команд(CommandHandler)
logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt='%H:%M:%S')


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
    #Учим бота реагировать на определенный текст в чате, при нажатии на кнопку/текстового ввода 'Прислать котика'
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    #Передает координаты пользователя
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
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
