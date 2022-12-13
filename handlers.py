#Модуль glob находит все файлы по определнному шаблону
from glob import glob
#Модуль random отвечает за работу со случайными числами, choice - за выбор случайного элемента
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard


#Функция вызова приветствия со эмоджи
#update - информация, пришедшая из Телеги(команда 'start', информация о пользователе, которую вызвал эту команду)
#context - когда мы хотим отправить другому пользователю команду
def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Привет, пользователь {context.user_data['emoji']}!",
        reply_markup=main_keyboard() 
    ) #передаем пареметр reply_markup


#Функция ответа пользователю на входящие сообщение
def talk_to_me(update, context):
    #context.user_data: Это словарь: если мы добавим в него ключ с данными, эти данные будут доступны для этого пользователя.
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    update.message.reply_text(f"{text} {context.user_data['emoji']}")


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
    update.message.reply_text(message, reply_markup=main_keyboard())


#Функция отправки случайной картинки в нужный чат
def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*') #получаем список картинок
    cat_photo_filename = choice(cat_photo_list) #выбираем случайную картинку
    chat_id = update.effective_chat.id #получение id чата с текущим пользователем, нужно для картинки
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup=main_keyboard()) #'rb' - формат readbinary(двоичный) считывания картинки в питоне


#Функция передачи геолокаци
def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )
