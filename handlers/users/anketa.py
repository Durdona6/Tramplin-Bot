from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.social import rumainMenu,engmainMenu,uzmainMenu
from loader import dp
from states.personalData import PersonalData,ruPersonalData,engPersonalData


@dp.callback_query_handler(text='uzvacancy')
async def select_category(call:types.CallbackQuery):
    await call.message.answer("Qiziqqan yo'nalishingiz.")
    await PersonalData.yonalish.set()


@dp.message_handler(state=PersonalData.yonalish)
async def answer_fullname(message: types.Message, state: FSMContext):
    yonalish = message.text
    await state.update_data(
        {
            'yonalish': yonalish
        }
        )
    
    await message.answer("Familiya,Ism,Sharifingizni to'liq kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.fullname)
async def answer_email(message: types.Message, state: FSMContext):
    fullname = message.text


    await state.update_data(
        {
            'name': fullname
        }
        )
    
    await message.answer('Resume')
    await PersonalData.next()

@dp.message_handler(state=PersonalData.resume, content_types=types.ContentType.DOCUMENT)
async def answer_resume(message: types.Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_name
        }
        )
    


    await message.answer('Telefon raqamingizni kiriting')
    await PersonalData.next()
   

@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text


    await state.update_data(
        {
            'phone': phone
        }
        )

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    yonalish = data.get("Yo'nalish")
    name = data.get('name')
    rezume = data.get('resume')
    phone = data.get('phone')

    msg = "Quyidagi ma'lumotlarni qabul qilindi:\n"
    msg += f"<b>Yo'nalishingiz</b> - {yonalish}\n"
    msg += f"<b>Ismingiz</b> - {name}\n"
    msg += f"<b>Resume</b> - {rezume}\n"
    msg += f"<b>Phone</b> - {phone}" 
    await message.answer(msg, reply_markup=uzmainMenu)
    await state.finish()
    # await state.reset_state(with_data = False)





    
@dp.callback_query_handler(text='ruvacancy')
async def select_category(call:types.CallbackQuery):
    await call.message.answer("Ваше интересующее направление.")
    await ruPersonalData.ruyonalish.set()


@dp.message_handler(state=ruPersonalData.ruyonalish)
async def answer_fullname(message: types.Message, state: FSMContext):
    ruyonalish = message.text
    await state.update_data(
        {
            'Ваше направление': ruyonalish
        }
        )
    
    await message.answer("Фамилия, Имя, Отчество.")
    await ruPersonalData.next()


@dp.message_handler(state=ruPersonalData.rufullname)
async def answer_email(message: types.Message, state: FSMContext):
    rufullname = message.text


    await state.update_data(
        {
            'Ваше имя': rufullname
        }
        )
    
    await message.answer('Резюме')
    await ruPersonalData.next()

@dp.message_handler(state=ruPersonalData.ruresume, content_types=types.ContentType.DOCUMENT)
async def answer_phone(message: types.Message, state: FSMContext):
    ruresume = message.document

    await state.update_data(
        {
            'Резюме': ruresume.file_name
        }
        )
    
    await message.answer('Введите ваш номер телефона.')
    await ruPersonalData.next()
   

@dp.message_handler(state=ruPersonalData.ruphoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    ruphone = message.text


    await state.update_data(
        {
            'Телефон': ruphone
        }
        )

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    ruyonalish = data.get("Ваше направление")
    runame = data.get('Ваше имя')
    ruresume = data.get('Резюме')
    ruphone = data.get('Телефон')
    msg = "Следующая информация принята:\n"
    msg += f"<b>Ваше направление</b> - {ruyonalish}\n"
    msg += f"<b>Ваше имя</b> - {runame}\n"
    msg += f"<b>Резюме</b> - {ruresume}\n"
    msg += f"<b>Телефон</b> - {ruphone}" 
    await message.answer(msg, reply_markup=rumainMenu)
    await state.finish()
    # await state.reset_state(with_data = False)






    
@dp.callback_query_handler(text='engvacancy')
async def select_category(call:types.CallbackQuery):
    await call.message.answer("Your area of interest.")
    await engPersonalData.engyonalish.set()


@dp.message_handler(state=engPersonalData.engyonalish)
async def answer_fullname(message: types.Message, state: FSMContext):
    engyonalish = message.text
    await state.update_data(
        {
            'Direction': engyonalish
        }
        )
    await message.answer("Surname, First Name, Patronymic")
    await engPersonalData.next()


@dp.message_handler(state=engPersonalData.engfullname)
async def answer_email(message: types.Message, state: FSMContext):
    engfullname = message.text


    await state.update_data(
        {
            'name': engfullname
        }
        )
    await message.answer('Resume')
    await engPersonalData.next()

@dp.message_handler(state=engPersonalData.engresume, content_types=types.ContentType.DOCUMENT)
async def answer_phone(message: types.Message, state: FSMContext):
    engresume = message.document

    await state.update_data(
        {
            'resume': engresume.file_name
        }
        )
    


    await message.answer('Enter your phone number.')
    await engPersonalData.next()
   

@dp.message_handler(state=engPersonalData.engphoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    engphone = message.text


    await state.update_data(
        {
            '<b>phone</b>': engphone
        }
        )

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    engyonalish = data.get("Direction")
    engname = data.get('name')
    engresume = data.get('resume')
    engphone = data.get('phone')

    msg = "The following information has been received:\n"
    msg += f"<b>Your area of interest</b> - {engyonalish}\n"
    msg += f"<b>Your name</b> - {engname}\n"
    msg += f"<b>Resume</b> - {engresume}\n"
    msg += f"<b>Phone</b> - {engphone}" 
    await message.answer(msg, reply_markup=engmainMenu)
    await state.finish()
    # await state.reset_state(with_data = False)


