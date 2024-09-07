from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.bio import uzcategoryMenu,rucategoryMenu,engcategoryMenu
from keyboards.inline.social import uzmainMenu,uzKurslar, ruKurslar,engKurslar,Back_to_Kurslar,rumainMenu,engmainMenu,ruBack_to_Kurslar,engBack_to_Kurslar,uzXodimlar,ruXodimlar,engXodimlar,uzBack_to_xodimlar,ruBack_to_xodimlar,engBack_to_xodimlar
from aiogram.types import InputFile

user_message_ids = {}

@dp.callback_query_handler(text='uz')
async def select_category(call: CallbackQuery):
    msg = "Ajoyib! 👍 O'zbek tili tanlandi 🇺🇿"
    await call.message.answer(msg)
    photo_file = InputFile(path_or_bytesio='photo/TRp.jpg')
    start_message = await call.message.answer_photo(photo_file,f"Kerakli bo'limga o'tish uchun tugmalardan birini tanlang ⤵️", reply_markup=uzcategoryMenu)
    user_message_ids[call.message.from_user.id] = start_message.message_id
    await call.message.delete()


@dp.callback_query_handler(text='ru')
async def select_category(call:CallbackQuery):
    msg = "Русский язык выбран 🇷🇺"
    await call.message.answer(msg)
    photo_file = InputFile(path_or_bytesio='photo/TRp.jpg')
    start_message = await call.message.answer_photo(photo_file,f"Выберите одну из кнопок, чтобы перейти в нужный раздел ⤵️", reply_markup=rucategoryMenu) 
    user_message_ids[call.message.from_user.id] = start_message.message_id
    await call.message.delete()

@dp.callback_query_handler(text='eng')
async def select_category(call: CallbackQuery):
    msg = "Great! 👍 English language selected 🇺🇸 "
    await call.message.answer(msg)
    photo_file = InputFile(path_or_bytesio='photo/TRp.jpg')
    start_message = await call.message.answer_photo(photo_file,f"Select one of the buttons to go to the desired section ⤵️",reply_markup=engcategoryMenu)
    user_message_ids[call.message.from_user.id] = start_message.message_id
    await call.message.delete()



@dp.callback_query_handler(text="uzabout")
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=uzmainMenu)

@dp.callback_query_handler(text='ruabout')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=rumainMenu)


@dp.callback_query_handler(text='engabout')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=engmainMenu)

    

@dp.callback_query_handler(text="uzmenu")
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=uzcategoryMenu)

@dp.callback_query_handler(text="rumenu")
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=rucategoryMenu)

@dp.callback_query_handler(text="engmenu")
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='c:/Users/user/Downloads/Trp.jpg')
    await call.message.answer_photo(photo_file,'Tramplin!',reply_markup=engcategoryMenu)

@dp.callback_query_handler(text='uzkurslar')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
    await call.message.answer_photo(photo_file,"Shulardan birini tanlang ⤵️",reply_markup=uzKurslar)

@dp.callback_query_handler(text='rukurslar')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
    await call.message.answer_photo(photo_file,"Выберите один из этих ⤵️",reply_markup=ruKurslar)

@dp.callback_query_handler(text='engkurslar')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
    await call.message.answer_photo(photo_file,"Choose one of these ⤵️",reply_markup=engKurslar)

@dp.callback_query_handler(text='uzbackend')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/Backend.jpg')
    await call.message.answer_photo(photo_file, caption='Backend dasturchi veb-sayt yoki veb-ilovaning funksionaliga, ma’lumotlarni qayta ishlashga xizmat qiladi. Shuning uchun backend dasturchilar ma’lumotlar ombori bilan ishlashni yaxshi bilishlari kerak. Bundan tashqari turli darajadagi murakkablikka ega bo’lgan algoritmlar bilan ishlay olishlari va loyihalar uchun arxitektura qurishlari talab etiladi. Aslida, backend dasturiy va apparat qismiga ham tegishli. Biroq, tarixan, backend va frontend ayniqsa, web-developmentda aniq ajralib chiqdi. Va bu ayni paytda eng mashhur soha bo’lib kelmoqda.',reply_markup=Back_to_Kurslar)

@dp.callback_query_handler(text='rubackend')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/Backend.jpg')
    await call.message.answer_photo(photo_file,caption="Бэкэнд-разработчик обеспечивает функциональность и обработку данных веб-сайта или веб-приложения. Вот почему бэкенд-разработчикам необходимо знать, как работать с базой данных. Кроме того, требуется уметь работать с алгоритмами разного уровня сложности и строить архитектуру проектов. Фактически, бэкэнд относится как к программному, так и к аппаратному обеспечению. Однако исторически бэкенд и фронтенд были четко разделены, особенно в веб-разработке. И это самая популярная сфера на данный момент.",reply_markup=ruBack_to_Kurslar)

@dp.callback_query_handler(text='engbackend')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/Backend.jpg')
    await call.message.answer_photo(photo_file,caption="The backend developer serves the functionality and data processing of the website or web application. That's why backend developers need to know how to work with a database. In addition, it is required to be able to work with algorithms of different levels of complexity and build architecture for projects. In fact, backend refers to both software and hardware. However, historically, backend and frontend have been clearly separated, especially in web development. And this is the most popular field at the moment.",reply_markup=engBack_to_Kurslar)

@dp.callback_query_handler(text='uzortga')
async def select_category(call: CallbackQuery):
   await call.message.delete()
   photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
   await call.message.answer_photo(photo_file,"Shulardan birini tanlang⤵️",reply_markup=uzKurslar)

@dp.callback_query_handler(text='ruortga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
    await call.message.answer_photo(photo_file,"Выберите один из этих ⤵️",reply_markup=ruKurslar)

@dp.callback_query_handler(text='engortga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fullsteak.jpg')
    await call.message.answer_photo(photo_file,"Выберите один из этих ⤵️",reply_markup=engKurslar)

@dp.callback_query_handler(text='uzfronted')
async def select_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fronted.jpg')
    await call.message.answer_photo(photo=photo_file, 
        caption=(
"""Foydalanuvchi qidiruv satrida manzilni kiritadi, tashqi manbadan yoki qidiruv tizimidan havola orqali o'tadi. Unga ko'p reklama ko'rsatiladi. Unga uzundan uzoq ro'yxatdan o'tish oynalarini to'ldirish talab etiladi. Unga noqulay navigatsiya va o'qish qiyin bo'lgan kontent taqdim etiladi. Sahifa uzoq vaqt davomida yuklanadi yoki mobil qurilmalar uchun moslashtirilmaydi yoki eski dizaynga ega. Foydalanuvchi nima qiladi? To'g'ri, saytni tark etadi.\n
Frontend developerning vazifasi maksimal tarzda voqealar rivojidan, yaratilgan interfeys va undagi ma'lumotlar orqali foydalanuvchini ogoh qilib borish. U o'z navbatida bir necha ierarxiyaga bo'lingan foydalanuvchi interfeysini ishlab chiqishi kerak bo'ladi. Bular maket dizayni, layout(верстка), adaptatsiya. Veb-ilova ishlab chiqishda eng asosiy qism bu UI/UX ya'ni foydalanuvchining birinchi taasurotiga ta'sir o'tkazadi."""
        ),
        reply_markup=Back_to_Kurslar
    )

@dp.callback_query_handler(text='rufronted')
async def select_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fronted.jpg')
    await call.message.answer_photo(photo=photo_file,
        caption=(
"""Пользователь вводит адрес в строку поиска, переходит по ссылке из внешнего источника или поисковой системы. На ней отображается много рекламы. От него требуется заполнять длинные окна регистрации. Неудобная навигация и трудночитаемый контент. Страница долго загружается, не оптимизирована для мобильных устройств или имеет устаревший дизайн. Что делает пользователь? Правильно, он покидает сайт.\n
Задача фронтенд-разработчика — максимально информировать пользователя о развитии событий через созданный интерфейс и информацию в нем. Ему, в свою очередь, придется разработать пользовательский интерфейс, разделенный на несколько иерархий. Это макетирование, верстка, адаптация. Наиболее важной частью разработки веб-приложений является UI/UX, который влияет на первое впечатление пользователя."""
        ),
        reply_markup=ruBack_to_Kurslar   
    )

@dp.callback_query_handler(text='engfronted')
async def select_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/fronted.jpg')
    await call.message.answer_photo(photo=photo_file,
        caption=(
"""The user enters the address in the search bar, goes through a link from an external source or search engine. A lot of ads are displayed on it. He is required to fill out long registration windows. It presents awkward navigation and hard-to-read content. The page takes a long time to load, or is not optimized for mobile devices, or has an outdated design. What does the user do? That's right, it leaves the site.\n
The task of the frontend developer is to inform the user about the development of events as much as possible through the created interface and the information in it. He, in turn, will have to develop a user interface that is divided into several hierarchies. These are layout design, layout, adaptation. The most important part of web application development is UI/UX, which affects the user's first impression."""
        ),
        reply_markup=engBack_to_Kurslar
    )

@dp.callback_query_handler(text='uzkiberxavfsizlik')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/kiberxavfsizlik.jpg')
    await call.message.answer_photo(photo=photo_file,
        caption=(
"""Kiberxavfsizlik nima? Ba’zilarimiz bu atamani ilgari eshitganmiz, lekin ba’zilarimiz bu nimani anglatishini yoki nima uchun bunday deb atalishini bilmasligimiz mumkin. Shunday qilib, kiberxavfsizlikning ma’nosini to’liq tushunish uchun keling, so’zni ikki qismga ajratamiz: “kiber” va “xavfsizlik\n\n<b>Kiber va xavfsizlik nima?</b>
“ Kiber ” atamasi odatda kompyuterlar,axborot texnologiyalari yoki internet bilan bog’liq narsalarni anglatadi.Buni yaxshiroq tushunish uchun uni kompyuterlar va internetga tegishli maxsus so’z sifatida tasavvur qiling.\n
Xavfsizlik – bu xavf yoki tahdiddan xoli bo’lish va xavfsiz bo’lish holatini anglatadi."""
        ),
        reply_markup=Back_to_Kurslar
    )

@dp.callback_query_handler(text='rukiberxavfsizlik')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/kiberxavfsizlik.jpg')
    await call.message.answer_photo(photo=photo_file,
        caption=(
"""Что такое кибербезопасность? Некоторые из нас слышали этот термин раньше, но некоторые из нас могут не знать, что он означает и почему его так называют. Итак, чтобы полностью понять значение кибербезопасности, давайте разделим это слово на две части: «кибер» и «безопасность».\n\n<b>Что такое кибербезопасность и безопасность?</b>
Термин «кибер» обычно относится ко всему, что связано с компьютерами, информационными технологиями или Интернетом. Чтобы лучше понять это, подумайте об этом как о специальном слове, обозначающем компьютеры и Интернет.\n
Безопасность – это состояние безопасности и свободы от опасности или угрозы."""
        ),
        reply_markup=ruBack_to_Kurslar
    )

@dp.callback_query_handler(text='engkiberxavfsizlik')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/kiberxavfsizlik.jpg')
    await call.message.answer_photo(photo=photo_file,
caption=(
"""What is cybersecurity? Some of us have heard the term before, but some of us may not know what it means or why it is called that. So, to fully understand the meaning of cybersecurity, let's break the word down into two parts: "cyber" and "security".\n\n<b>What is cybersecurity and security?</b>
The term "cyber" generally refers to anything related to computers, information technology, or the Internet. To better understand it, think of it as a special word for computers and the Internet.\n
Security is the state of being safe and free from danger or threat."""
        ),
        reply_markup=engBack_to_Kurslar
    )

@dp.callback_query_handler(text='uzgraphics')
async def selesct_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/graphics.jpg')
    await call.message.answer_photo(photo=photo_file,
        caption=(
"""Grafik dizayn — dizayn sohasining yoʻnalishlaridan biri boʻlib, maʼlum axborotni ijtimoiy guruhlarga yetkazish uchun vizual kontent yaratish, ularni tartiblash, loyihalashga xizmat qiladi. Grafik dizaynning asosiy maqsadi muammolarni aniqlash va ularni ijodkorlik bilan innovatsion va raqamli vositalar yordamida oʻzgartirish va toʻgʻri talqin qilishdan iborat.\n
Bu soha vakillari, grafik dizaynerlar, vizual xabarlarni talqin qilish, ularni tartiblash va mijozga taqdim etish ustida ishlaydi. Dizayn ishi mijozning talabiga asoslanishi mumkin, bu talab lingvistik jihatdan ogʻzaki yoki yozma ravishda belgilanadi, yaʼni grafik dizayner mijozning ogʻzaki yoki yozma xabarini grafik koʻrinishga aylantiradi.
"""
        ),
        reply_markup=Back_to_Kurslar
    )


@dp.callback_query_handler(text='rugraphics')
async def selesct_category (call: CallbackQuery):
 await call.message.delete()
 photo_file = InputFile(path_or_bytesio='photo/graphics.jpg')
 await call.message.answer_photo(photo=photo_file,
        caption=(
"""Графический дизайн - одно из направлений области дизайна, которое служит для создания, систематизации и оформления визуального контента для донесения определенной информации до социальных групп. Основная цель графического дизайна - выявление проблем и их творческое изменение с помощью инновационные и цифровые инструменты и правильно их интерпретировать.\n
Эти представители отрасли, графические дизайнеры, работают над интерпретацией визуальных сообщений, их организацией и представлением клиенту. Проектная работа может быть основана на требовании клиента, которое лингвистически определено устно или письменно, то есть графический дизайнер переводит устное или письменное сообщение клиента в графическое представление.
"""
        ),
        reply_markup=ruBack_to_Kurslar
    )

@dp.callback_query_handler(text='enggraphics')
async def selesct_category(call:CallbackQuery):
 await call.message.delete()
 photo_file = InputFile(path_or_bytesio='photo/graphics.jpg')
 await call.message.answer_photo(photo=photo_file,
 caption=(
"""Graphic design is one of the directions of the field of design, which serves to create, arrange, and design visual content to convey certain information to social groups. The main goal of graphic design is to identify problems and change them creatively using innovative and digital tools and interpret them correctly. .\n
These industry representatives, graphic designers, work on interpreting visual messages, organizing them and presenting them to the client. The design work can be based on the client's requirement, which is linguistically defined verbally or written, that is, the graphic designer translates the client's verbal or written message into a graphic representation.
"""
        ),
        reply_markup=engBack_to_Kurslar
    )





@dp.callback_query_handler(text='uzxodimlar')
async def select_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file,reply_markup=uzXodimlar)

@dp.callback_query_handler(text='ruxodimlar')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file,reply_markup=ruXodimlar)


@dp.callback_query_handler(text='engxodimlar')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file, reply_markup=engXodimlar)


@dp.callback_query_handler(text='uzOrtga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file,reply_markup=uzXodimlar)

@dp.callback_query_handler(text='ruOrtga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file,reply_markup=ruXodimlar)

@dp.callback_query_handler(text='engOrtga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/xodimlar.jpg')
    await call.message.answer_photo(photo_file,reply_markup=engXodimlar)

@dp.callback_query_handler(text='uzotajon')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Ismi-sharifi:</b>\nOtajon Bozorboyev'
    msg += "<b>Tug'ilgan yili va joyi:</b>\n8-yanvar 1999-yil;\nJizzax viloyati,Jizzax shahri\n"
    msg += "<b>Ta'limi:</b>\nToshkent temir yo'l transport kasb-hunar kolleji (2018)\n"
    msg += "<b>Ish tajribasi:</b>\n"
    msg += """"-O'zbekiston temir yo'llari" AJ tashkiloti Jizzax temir yo'l msasofasi xodimlar bo'limi nazoratchisi (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024);Tramplin IT Academy Backend dasturchi va Pythin backend mentor (2024-hozirgacha)\n"""
    msg += "<b>Texnik ko'nikmalari:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n"
    msg += "<b>Tillar:</b>\nO'zbek tili(Ona tili);\nIngliz tili(B2);\nArab tili(O'qiy olish);\nYapon tili(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=uzBack_to_xodimlar)

@dp.callback_query_handler(text='ruotajon')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Имя:</b>\nОтаджон Бозорбоев'
    msg += "<b>Год и место рождения:</b>\n8 января 1999 года;\nДжизакская область, город Джизак\n"
    msg += "<b>Образование:</b>\nТашкентский профессиональный колледж железнодорожного транспорта (2018)\n"
    msg += "<b>Опыт работы:</b>\n"
    msg += """"-АО "Узбекистон темир йуллари" организация Джизакская железная дорога руководитель отдела кадров (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer и Python Backend Mentor (с 2024 г. по настоящее время)\n"""
    msg += "<b>Технические навыки:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word, Excel) , Power Point, Paint и т. д.)\n"
    msg += "<b>Языки:</b>\nУзбекский язык(Родной язык);\nАнглийский язык(B2);\nАрабский язык(Обучение);\nЯпонский язык(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=ruBack_to_xodimlar)

@dp.callback_query_handler(text='engotajon')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Name:</b>\nOtajon Bozorboyev'
    msg += "<b>Year and place of birth:</b>\nJanuary 8, 1999;\nJizzakh region, city of Jizzakh\n"
    msg += "<b>Education:</b>\nTashkent Railway Transport Vocational College (2018)\n"
    msg += "<b>Work experience:</b>\n"
    msg += """"-Uzbekiston temir yollari" JSC organization Jizzakh railway distance personnel department supervisor (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer and Pythin Backend Mentor (2024 to present)\n"""
    msg += "<b>Technical Skills:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word , Excel, Power Point, Paint, etc.)\n"
    msg += "<b>Languages:</b>\nUzbek language(Native language);\nEnglish language(B2);\nArabic language(Learning);\nJapanese language(N3)"
    await call.message.answer_photo(photo=photo_file,caption=msg, reply_markup=engBack_to_xodimlar)





@dp.callback_query_handler(text='uzrustam')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Ismi-sharifi:</b>\nOtajon Bozorboyev'
    msg += "<b>Tug'ilgan yili va joyi:</b>\n8-yanvar 1999-yil;\nJizzax viloyati,Jizzax shahri\n"
    msg += "<b>Ta'limi:</b>\nToshkent temir yo'l transport kasb-hunar kolleji (2018)\n"
    msg += "<b>Ish tajribasi:</b>\n"
    msg += """"-O'zbekiston temir yo'llari" AJ tashkiloti Jizzax temir yo'l msasofasi xodimlar bo'limi nazoratchisi (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024);Tramplin IT Academy Backend dasturchi va Pythin backend mentor (2024-hozirgacha)\n"""
    msg += "<b>Texnik ko'nikmalari:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n"
    msg += "<b>Tillar:</b>\nO'zbek tili(Ona tili);\nIngliz tili(B2);\nArab tili(O'qiy olish);\nYapon tili(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=uzBack_to_xodimlar)



@dp.callback_query_handler(text='rurustam')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Имя:</b>\nОтаджон Бозорбоев'
    msg += "<b>Год и место рождения:</b>\n8 января 1999 года;\nДжизакская область, город Джизак\n"
    msg += "<b>Образование:</b>\nТашкентский профессиональный колледж железнодорожного транспорта (2018)\n"
    msg += "<b>Опыт работы:</b>\n"
    msg += """"-АО "Узбекистон темир йуллари" организация Джизакская железная дорога руководитель отдела кадров (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer и Python Backend Mentor (с 2024 г. по настоящее время)\n"""
    msg += "<b>Технические навыки:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word, Excel) , Power Point, Paint и т. д.)\n"
    msg += "<b>Языки:</b>\nУзбекский язык(Родной язык);\nАнглийский язык(B2);\nАрабский язык(Обучение);\nЯпонский язык(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=ruBack_to_xodimlar)




@dp.callback_query_handler(text='engrustam')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Name:</b>\nOtajon Bozorboyev'
    msg += "<b>Year and place of birth:</b>\nJanuary 8, 1999;\nJizzakh region, city of Jizzakh\n"
    msg += "<b>Education:</b>\nTashkent Railway Transport Vocational College (2018)\n"
    msg += "<b>Work experience:</b>\n"
    msg += """"-Uzbekiston temir yollari" JSC organization Jizzakh railway distance personnel department supervisor (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer and Pythin Backend Mentor (2024 to present)\n"""
    msg += "<b>Technical Skills:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word , Excel, Power Point, Paint, etc.)\n"
    msg += "<b>Languages:</b>\nUzbek language(Native language);\nEnglish language(B2);\nArabic language(Learning);\nJapanese language(N3)"
    await call.message.answer_photo(photo=photo_file,caption=msg, reply_markup=engBack_to_xodimlar)




@dp.callback_query_handler(text='uzxusan')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Ismi-sharifi:</b>\nOtajon Bozorboyev'
    msg += "<b>Tug'ilgan yili va joyi:</b>\n8-yanvar 1999-yil;\nJizzax viloyati,Jizzax shahri\n"
    msg += "<b>Ta'limi:</b>\nToshkent temir yo'l transport kasb-hunar kolleji (2018)\n"
    msg += "<b>Ish tajribasi:</b>\n"
    msg += """"-O'zbekiston temir yo'llari" AJ tashkiloti Jizzax temir yo'l msasofasi xodimlar bo'limi nazoratchisi (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024);Tramplin IT Academy Backend dasturchi va Pythin backend mentor (2024-hozirgacha)\n"""
    msg += "<b>Texnik ko'nikmalari:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n"
    msg += "<b>Tillar:</b>\nO'zbek tili(Ona tili);\nIngliz tili(B2);\nArab tili(O'qiy olish);\nYapon tili(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=uzBack_to_xodimlar)



@dp.callback_query_handler(text='ruxusan')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Имя:</b>\nОтаджон Бозорбоев'
    msg += "<b>Год и место рождения:</b>\n8 января 1999 года;\nДжизакская область, город Джизак\n"
    msg += "<b>Образование:</b>\nТашкентский профессиональный колледж железнодорожного транспорта (2018)\n"
    msg += "<b>Опыт работы:</b>\n"
    msg += """"-АО "Узбекистон темир йуллари" организация Джизакская железная дорога руководитель отдела кадров (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer и Python Backend Mentor (с 2024 г. по настоящее время)\n"""
    msg += "<b>Технические навыки:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word, Excel) , Power Point, Paint и т. д.)\n"
    msg += "<b>Языки:</b>\nУзбекский язык(Родной язык);\nАнглийский язык(B2);\nАрабский язык(Обучение);\nЯпонский язык(N3)"
    await call.message.answer_photo(photo=photo_file, caption=msg, reply_markup=ruBack_to_xodimlar)


@dp.callback_query_handler(text='engxusan')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    msg = '<b>Name:</b>\nOtajon Bozorboyev'
    msg += "<b>Year and place of birth:</b>\nJanuary 8, 1999;\nJizzakh region, city of Jizzakh\n"
    msg += "<b>Education:</b>\nTashkent Railway Transport Vocational College (2018)\n"
    msg += "<b>Work experience:</b>\n"
    msg += """"-Uzbekiston temir yollari" JSC organization Jizzakh railway distance personnel department supervisor (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024) );Tramplin IT Academy Backend Developer and Pythin Backend Mentor (2024 to present)\n"""
    msg += "<b>Technical Skills:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office (Word , Excel, Power Point, Paint, etc.)\n"
    msg += "<b>Languages:</b>\nUzbek language(Native language);\nEnglish language(B2);\nArabic language(Learning);\nJapanese language(N3)"
    await call.message.answer_photo(photo=photo_file,caption=msg, reply_markup=engBack_to_xodimlar)