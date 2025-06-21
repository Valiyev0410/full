
from telebot import types

def localisation_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_uz = types.KeyboardButton(text="uz🇺🇿")
    btn_ru = types.KeyboardButton(text="ru🇷🇺")
    btn_eng = types.KeyboardButton(text="Eng🇺🇸")
    keyboard.row(btn_uz, btn_ru, btn_eng)
    return keyboard

def menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_computers = types.KeyboardButton(text="Kompyuterlar")
    btn_laptops = types.KeyboardButton(text="Noutbuklar")
    btn_tv = types.KeyboardButton(text="Printerlar")
    keyboard.row(btn_computers, btn_laptops, btn_tv)
    return keyboard

def product_inline_url(url):
    keyboard = types.InlineKeyboardMarkup()
    btn_buy = types.InlineKeyboardButton(text="Sotib olish", callback_data="buy")
    btn_url = types.InlineKeyboardButton(text="Batafsil", url=url)
    keyboard.row(btn_buy, btn_url)
    return keyboard

def generate_pagination():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    step_go = types.KeyboardButton(text="Keyingi")
    step_back = types.KeyboardButton(text="ro'yxatni qaytarish")
    step_back_menu = types.KeyboardButton(text="orqaga")
    keyboard.row(step_go, step_back)
    keyboard.row(step_back_menu)
    return keyboard
