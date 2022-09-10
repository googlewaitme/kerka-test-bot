from loader import dp

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import messages


@dp.message_handler(CommandStart())
async def send_start(message: types.Message):
    # TODO here keyboard
    text = messages.START_MESSAGE_TEMPLATE.format(username=message.from_user.first_name)
    await message.answer(text)
