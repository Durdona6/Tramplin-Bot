from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

uzcategoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✍️ Haqida', callback_data="uzabout"),
            InlineKeyboardButton(text='📚 Kurslar', callback_data="uzkurslar")
        ],
        [
            InlineKeyboardButton(text='👥 Xodimlar', callback_data="uzxodimlar"),
            InlineKeyboardButton(text="💼 Vakansiya", callback_data='uzvacancy')
        ],
        [
            InlineKeyboardButton(text='📞Murojat uchun', url="https://t.me/obozorboyev_bot")
        ]      
    ]
)

rucategoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✍️ О чем', callback_data="ruabout"),
            InlineKeyboardButton(text='📚 Курсы', callback_data="rukurslar")
        ],
        [
            InlineKeyboardButton(text='👥 Сотрудники', callback_data="ruxodimlar"),
            InlineKeyboardButton(text="💼 Вакансия", callback_data='ruvacancy')
        ],
        [
            InlineKeyboardButton(text='📞Для справки', url="https://t.me/obozorboyev_bot")
        ]      
    ]
)


engcategoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✍️ About', callback_data="engabout"),
            InlineKeyboardButton(text='📚 Courses', callback_data="engkurslar")
        ],
        [
            InlineKeyboardButton(text='👥 Employees', callback_data="engxodimlar"),
            InlineKeyboardButton(text="💼 Vacancy", callback_data='engvacancy')
        ],
        [
            InlineKeyboardButton(text='📞For reference', url="https://t.me/obozorboyev_bot")
        ]      
    ]
)
