# -*- coding: utf-8 -*-
import telebot
import sqlite3
from app import bot, SEX, NAME, AGE, PIC_LINK, HEIGHT,HEIG_MIN, HEIG_MAX, HEAD, TIME_MIN, TIME_MAX, W_A_W, DOG, FIND


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Приветик, дружок :) Готов найти свою самую настоящую любовь? Да?)')
    bot.send_message(message.chat.id, 'Тогда у меня к тебе парочка вопросов')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, 'Напиши /reg')


@bot.message_handler(commands=['reg'])
def handle_reg(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name


# Handles all text messages that match the regular expression
@bot.message_handler(content_types=['text'], regexp="python")
def handle_python_message(message):
    bot.send_message(message.chat.id, "Я обожаю python!")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    bot.send_message(message.chat.id, 'напиши "/reg"')


def get_name(message):
    global NAME
    NAME = message.text
    bot.send_message(message.chat.id, 'А ты мальчик или девчуля? Ответом пусть будет один из этих двух вариантов')
    bot.register_next_step_handler(message, get_sex)


def get_sex(message):
    global SEX
    if message.text.lower() == 'мальчик':
        SEX = 0
    elif message.text.lower() == 'девчуля':
        SEX = 1
    else:
        bot.send_message(message.chat.id, 'Ты написал неправильно... Попробуй-ка еще разочек :)')
        bot.register_next_step_handler(message, get_sex)
        return
    bot.send_message(message.chat.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global AGE
    try:
        AGE = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
        return
    bot.send_message(message.chat.id, 'А теперь отправь ссылку на своё фото ^^')
    bot.send_message(message.chat.id, 'Постарайся не ошибаться, иначе твоя любовь тебя не найдет!')
    bot.register_next_step_handler(message, get_pic_link)


def get_pic_link(message):
    global PIC_LINK
    PIC_LINK = message.text
    bot.send_message(message.chat.id, 'Напиши свой рост')
    bot.register_next_step_handler(message, get_height)


def get_height(message):
    global HEIGHT
    try:
        HEIGHT = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_height)
        return
    bot.send_message(message.chat.id, 'Напиши минимальный рост будущего партнера')
    bot.register_next_step_handler(message, get_minheight)


def get_minheight(message):
    global HEIG_MIN
    try:
        HEIG_MIN = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_minheight)
        return
    bot.send_message(message.chat.id, 'Напиши максимальный рост будущего партнера')
    bot.register_next_step_handler(message, get_maxheight)


def get_maxheight(message):
    global HEIG_MAX
    try:
        HEIG_MAX = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_maxheight)
        return
    bot.send_message(message.chat.id, 'Кто будет мужик в доме? Ты или не ты?')
    bot.send_message(message.chat.id, 'пс, пиши "я" / "не я"')
    bot.register_next_step_handler(message, get_head)


def get_head(message):
    global HEAD
    if message.text.lower() == 'не я':
        HEAD = 0
    elif message.text.lower() == 'я':
        HEAD = 1
    else:
        bot.send_message(message.chat.id, 'Ты написал неправильно... Попробуй-ка еще разочек :)')
        bot.register_next_step_handler(message, get_head)
        return
    bot.send_message(message.chat.id, 'Какое минимальное кол-во часов в неделю вы будете проводить вместе?')
    bot.register_next_step_handler(message, get_mintime)


def get_mintime(message):
    global TIME_MIN
    try:
        TIME_MIN = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_mintime)
        return
    bot.send_message(message.chat.id, 'Какое максимальное кол-во часов в неделю ты готов проводить вместе?')
    bot.register_next_step_handler(message, get_maxtime)


def get_maxtime(message):
    global TIME_MAX
    try:
        TIME_MAX = int(message.text)  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_maxtime)
        return
    bot.send_message(message.chat.id, 'Кем из романа "Война и мир" ты мог бы быть? Напиши номер варианта')
    bot.send_message(message.chat.id, '(Пол героя не важен, cуть лишь в том, чье поведение тебе ближе)')
    bot.send_message(message.chat.id, '1 Андрей Болконский')
    bot.send_message(message.chat.id, '2 Николай Ростов')
    bot.send_message(message.chat.id, '3 Пьер Безухов')
    bot.send_message(message.chat.id, '4 Наташа Ростова')
    bot.send_message(message.chat.id, '5 Марья Болконская')
    bot.send_message(message.chat.id, '6 Элен Курагина')
    bot.send_message(message.chat.id, '7 Анатоль Курагин')
    bot.register_next_step_handler(message, get_character)


def get_character(message):
    global W_A_W
    try:
        W_A_W = (int(message.text)) % 3  # проверяем, что возраст введен корректно
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_character)
        return
    bot.send_message(message.chat.id, 'Хочешь ли ты завести собаку? Ответь да/нет')
    bot.register_next_step_handler(message, get_dog)


def get_dog(message):
    global DOG
    if message.text.lower() == 'нет':
        DOG = 0
    elif message.text.lower() == 'да':
        DOG = 1
    else:
        bot.send_message(message.chat.id, 'Ты написал неправильно... Попробуй-ка еще разочек :)')
        bot.register_next_step_handler(message, get_dog)
        return
    bot.send_message(message.chat.id, 'Фуууух, последний вопросик')
    bot.send_message(message.chat.id, 'Где тебя искать - то? :)')
    bot.register_next_step_handler(message, get_find)


def get_find(message):
    global FIND
    FIND = message.text
    bot.send_message(message.chat.id, 'Уже в поиске твоей любви <3 ')
    search_love(message)


def send_answer(message, cur):
    for row in cur:
        name, pic_link, find = row
        bot.send_message(message.chat.id, name)
        bot.send_message(message.chat.id, pic_link)
        bot.send_message(message.chat.id, 'Чтобы найти свою любовь, отправляйся...')
        bot.send_message(message.chat.id, find)
        return


def search_love(message):
    global SEX
    global NAME
    global AGE
    global PIC_LINK
    global HEIGHT
    global HEIG_MIN
    global HEIG_MAX
    global HEAD
    global TIME_MIN
    global TIME_MAX
    global W_A_W
    global DOG
    global FIND
    with sqlite3.connect('true_lovers.db') as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS lovers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sex INTEGER,
                name VARCHAR(255),
                age INTEGER,
                pic_link VARCHAR(255),
                height INTEGER,
                head INTEGER,
                min_time INTEGER,
                max_time INTEGER,
                W_A_W INTEGER,
                dog INTEGER,
                find VARCHAR(255)
        )''')

        cmd = '''INSERT INTO lovers (sex, name, age, pic_link, height, head, min_time, max_time, W_A_W, dog, find) 
        VALUES('{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}')'''.format(
        SEX, NAME, AGE, PIC_LINK, HEIGHT, HEAD, TIME_MIN, TIME_MAX, W_A_W, DOG, FIND)
        cur.execute(cmd)

        cmd1 = '''SELECT name, pic_link, find
        from lovers 
        WHERE sex != (?)'''
        cmd2 = '''SELECT name, pic_link, find
                from lovers 
                WHERE sex <> (?)
                AND HEIGHT < (?) AND HEIGHT > (?)'''
        cmd3 = '''SELECT name, pic_link, find
                from lovers 
                WHERE sex <> (?)
                AND height < (?) AND height > (?)
                AND head <> (?)'''
        cmd4 = '''SELECT name, pic_link, find
                from lovers 
                WHERE sex <> (?)
                AND height < (?) AND height > (?)
                AND head <> (?)
                AND min_time < (?) and max_time > (?)'''
        cmd5 = '''SELECT name, pic_link, find
                from lovers 
                WHERE sex <> (?)
                AND height < (?) AND height > (?)
                AND head <> (?)
                AND min_time < (?) and max_time > (?)
                AND W_A_W = (?)'''
        cmd6 = '''SELECT name, pic_link, find
                from lovers 
                WHERE sex <> (?)
                AND height < (?) AND height > (?)
                AND head <> (?)
                AND min_time < (?) and max_time > (?)
                AND W_A_W = (?)
                AND dog = (?)'''

        cur = conn.cursor()
        cur.execute(cmd2, [str(SEX), int(HEIG_MAX), int(HEIG_MIN)])
        data = cur.fetchall()
        if len(data) == 0:
            cur = conn.cursor()
            cur.execute(cmd1, [str(SEX)])
            bot.send_message(message.chat.id, 'Процент совместимости 10')
            send_answer(message, cur)
            return

        cur = conn.cursor()
        cur.execute(cmd3, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD)])
        data = cur.fetchall()
        if len(data) == 0:
            cur = conn.cursor()
            cur.execute(cmd2, [str(SEX), HEIG_MAX, HEIG_MIN])
            bot.send_message(message.chat.id, 'Процент совместимости 35')
            send_answer(message, cur)
            return

        cur = conn.cursor()
        cur.execute(cmd4, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD), int(TIME_MAX), int(TIME_MIN)])
        data = cur.fetchall()
        if len(data) == 0:
            cur = conn.cursor()
            cur.execute(cmd3, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD)])
            bot.send_message(message.chat.id, 'Процент совместимости 45')
            send_answer(message, cur)
            return

        cur = conn.cursor()
        cur.execute(cmd5, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD), int(TIME_MAX), int(TIME_MIN), int(W_A_W)])
        data = cur.fetchall()
        if len(data) == 0:
            cur = conn.cursor()
            cur.execute(cmd4, [str(SEX), int(HEIG_MAX), HEIG_MIN, HEAD, int(TIME_MAX), int(TIME_MIN)])
            bot.send_message(message.chat.id, 'Процент совместимости 65')
            send_answer(message, cur)
            return

        cur = conn.cursor()
        cur.execute(cmd6, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD), int(TIME_MAX), int(TIME_MIN), int(W_A_W),
                           int(DOG)])
        data = cur.fetchall()
        cur1 = conn.cursor()
        if len(data) >= 1:
            bot.send_message(message.chat.id, 'Процент совместимости 100')
            cur = conn.cursor()
            cur.execute(cmd6,
                        [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD), int(TIME_MAX), int(TIME_MIN), int(W_A_W),
                         int(DOG)])
            send_answer(message, cur)
            return
        else:
            cur1.execute(cmd5, [str(SEX), int(HEIG_MAX), int(HEIG_MIN), int(HEAD), int(TIME_MAX), int(TIME_MIN), int(W_A_W)])
            bot.send_message(message.chat.id, 'Процент совместимости 85')
            send_answer(message, cur)
            return
