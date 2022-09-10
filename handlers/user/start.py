from loader import dp

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import messages

from keyboards.inline import add_balance_key


@dp.message_handler(CommandStart())
async def send_start(message: types.Message):
    # TODO here keyboard
    text = messages.START_MESSAGE_TEMPLATE.format(username=message.from_user.first_name)
    keyboard = add_balance_key.get()
    await message.answer(text, reply_markup=keyboard)
