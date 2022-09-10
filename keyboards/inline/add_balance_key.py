from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


balance_cb = CallbackData('balance', 'action')


def get():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Пополнить баланс', callback_data=balance_cb.new('add'))
    )
    return markup 
