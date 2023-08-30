# Проект CatBot

CatBot - это бот для Telegram, который присылает пользователю котиков.

## Установка

1. Клонируйте репозиторий с Github:

```
git clone https://github.com/Comandosss/mybot.git
```

2. Создайте виртуальное окружение:

```
python -m venv env
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Создайте файл `settings.py` и впишите переменные:

```
API_KEY = 'API-ключ бота'
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```

5. Запустите бота командой

```
python bot.py
```
