import telebot

bot = None

SEX = 0
NAME = ''
AGE = 0
PIC_LINK = ''
HEIGHT = 0
HEIG_MIN = 0
HEIG_MAX = 0
HEAD = 0
TIME_MIN = 0
TIME_MAX = 0
W_A_W = 0
DOG = 0
FIND = ''


def init_bot(token):
    global bot
    bot = telebot.TeleBot(token)

    from app import handlers
