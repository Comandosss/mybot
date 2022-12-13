#Библиотека c эмодзи
from emoji import emojize
#Импорт settings.py для сокрытия токенов, паролей и личных данных
import settings
#Модуль random отвечает за работу со случайными числами, функция randint - за целые числа; choice - за выбор случайного элемента
from random import randint, choice
#Класс для создания клавиатур
from telegram import ReplyKeyboardMarkup, KeyboardButton


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


#Функция отправки случайной картинки при нажатии кнопки Прислать котика и отправки геолокации(работает с мобилы)
def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Прислать котика', KeyboardButton('Мои координаты', request_location=True)]
    ])
