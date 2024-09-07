from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


language_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='uz')
        ],
        [
            InlineKeyboardButton(text='🇷🇺 Русский язык', callback_data='ru')
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English ",callback_data='eng')
        ]
    ]
)