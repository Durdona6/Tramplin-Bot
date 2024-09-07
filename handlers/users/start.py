from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.language import language_Keyboard

from loader import dp

@dp.message_handler(CommandStart())
async def select_start(message: types.Message):
    await message.answer(f'Salom {message.from_user.first_name} <b>Tramplin IT Academy</b>ning telegram botiga xush kelibsz\n')
    await message.answer("Davom etish uchun kerakli tilni tanlang\nВыберите нужный язык, чтобы продолжить\nSelect the desired language to continue👇",reply_markup=language_Keyboard)
