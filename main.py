import os
from _ast import Lambda
from operator import call
from telebot import TeleBot
from telebot.types import LabeledPrice
from db_bot.Computer_db import Computer_db
from db_bot.printer_db import Printer_db
from keyboards import *
from db_bot.laptop_db import Laptop_db
from config import Config

cfg = Config()

token = cfg.token
click_token = cfg.click_token
bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"Assalomu aleykum {first_name} Bizning onlayn market botimizga xush kelibsiz ")
    menu(message)

def menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Katalogni tanlang", reply_markup=menu_keyboard())
    bot.register_next_step_handler(message, products_catalog)

def products_catalog(message, product_id=0, products=None):
    chat_id = message.chat.id

    if message.text == "orqaga":
        return start(message)

    if message.text == "Noutbuklar":
        products = Laptop_db().select_data()

    if message.text == "Kompyuterlar":
        products = Computer_db().select_data()

    if message.text == "Printerlar":
        products = Printer_db().select_data()

    if message.text == "Keyingi" and product_id < len(products):
        product_id += 1

    if message.text == "ro'yxatni qaytarish" and product_id > 0:
        product_id -= 1

    print(products)
    print(product_id)

    product = products[product_id]

    product_title = product[0]
    product_url = product[1]
    image = product[2]
    product_price = product[3]
    product_description = product[4]
    bot.send_photo(chat_id, image, caption=f'{"Brand_name"}: {product_title}\n\n'
                                           f'{"Description"}: {product_description}'
                                           f'\n\n{"Price"}: {product_price}',
                   reply_markup=product_inline_url(product_url))

    user_message = bot.send_message(chat_id, f"Qolgan malumotlar soni : {len(products) - (product_id + 1)}", reply_markup=generate_pagination())

    if message.text == "Oldinga" and len(products) - (product_id + 1) == 0:
        bot.delete_message(chat_id, message.id + 2)
        bot.send_message(chat_id, "No products!", reply_markup=generate_pagination())
        product_id = product_id - len(products)
    bot.register_next_step_handler(user_message, products_catalog, product_id, products)

@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    chat_id = call.message.chat.id
    if call.data == "buy":
        product_info = call.message.caption.split(": ")
        product_price = ""
        price = product_info[-1].replace('UZS', "")
        for x in price:
            if x.isdigit():
                product_price += x

        INVOICE = {
            "title": product_info[1],
            "description": product_info[3],
            "invoice_payload": "bot-defined invoice payload",
            "provider_token": click_token,
            "start_parameter": "pay",
            "currency": "UZS",
            "prices": [LabeledPrice(label=product_info[1], amount=int(product_price + "00"))],
        }

        bot.send_invoice(chat_id, **INVOICE)

bot.polling(non_stop=True)
