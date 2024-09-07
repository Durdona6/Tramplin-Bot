from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.bio import uzcategoryMenu, rucategoryMenu, engcategoryMenu

Back_to_Kurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="uzortga")
        ]
    ]
)

ruBack_to_Kurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔙 назад', callback_data="ruortga")
      
        ]
    ]
)

engBack_to_Kurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔙 Back', callback_data="engortga")
        ]
    ]
)

       
uzmainMenu = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔝 Asosiy menyu', callback_data="uzmenu", reply_markup=uzcategoryMenu)
        ]
    ]
)

rumainMenu = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔝 Главное меню', callback_data="rumenu", reply_markup=rucategoryMenu)
        ]
    ]
)

engmainMenu = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='🔝 Main menu', callback_data="engmenu", reply_markup=engcategoryMenu)
        ]
    ]
)



uzKurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='Backend', callback_data="uzbackend"),
            InlineKeyboardButton(text='Fronted', callback_data='uzfronted')
        ],
        [
            InlineKeyboardButton(text='👾Kiberxavfsizlik', callback_data='uzkiberxavfsizlik'),
            InlineKeyboardButton(text='Grafik Dizayn', callback_data='uzgraphics')
        ],
        [
            InlineKeyboardButton(text='🔝 Asosiy menyu', callback_data="uzmenu", reply_markup=uzcategoryMenu)
        ],
    ]
)

ruKurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='Бэкэнд', callback_data="rubackend"),
            InlineKeyboardButton(text='Фронтед', callback_data='rufronted')
        ],
        [
            InlineKeyboardButton(text='👾Кибербезопасность', callback_data='rukiberxavfsizlik'),
            InlineKeyboardButton(text='Графический дизайн', callback_data='rugraphics')
        ],
        [
            InlineKeyboardButton(text='🔝 Главное меню', callback_data="rumenu", reply_markup=rucategoryMenu)
        ],
    ]
)

engKurslar = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='Backend', callback_data="engbackend"),
            InlineKeyboardButton(text='Fronted', callback_data='engfronted')
        ],
        [
            InlineKeyboardButton(text='👾 Cyber ​​security', callback_data='engkiberxavfsizlik'),
            InlineKeyboardButton(text='Graphic Design', callback_data='enggraphics')
        ],
        [
            InlineKeyboardButton(text='🔝 Main menu', callback_data="engmenu", reply_markup=engcategoryMenu)
        ],
    ]
)



uzXodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text='Otajon Bozorboyev',callback_data='uzotajon'),
          InlineKeyboardButton(text='Rustam', callback_data='uzrustam')  
        ],
        [
            InlineKeyboardButton(text='Xusan', callback_data='uzxusan'),
        ],
        [
            InlineKeyboardButton(text='🔝 Asosiy menu', callback_data='uzmenu', reply_markub=uzcategoryMenu)
        ],
    ]
)

ruXodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отаджон Бозорбоев', callback_data='ruotajon'),
            InlineKeyboardButton(text='Рустам', callback_data='rurustam')
        ],
        [
            InlineKeyboardButton(text='Хусан', callback_data='ruxusan'),
        ],
        [
            InlineKeyboardButton(text='🔝 Главное меню', callback_data='rumenu', reply_markub=rucategoryMenu)
        ],
    ]
)

engXodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text='Otajon Bozorboyev', callback_data='engotajon'),
          InlineKeyboardButton(text='Rustam', callback_data='engrustam')  
        ],
        [
            InlineKeyboardButton(text='Xusan', callback_data='engxusan'),
        ],
        [
            InlineKeyboardButton(text='🔝 Main menu', callback_data='engmenu', reply_markub=engmainMenu)
        ],
    ]
)


uzBack_to_xodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙ortga', callback_data='uzOrtga')
        ],
    ]
)




ruBack_to_xodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 назад', callback_data='ruOrtga')
        ],
    ]
)


engBack_to_xodimlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Back', callback_data='engOrtga')
        ],
    ]
)