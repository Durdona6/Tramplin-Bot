from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    yonalish= State()
    fullname = State()
    resume = State()
    phoneNumber = State()


class ruPersonalData(StatesGroup):
    ruyonalish = State()
    rufullname = State()
    ruresume = State()
    ruphoneNumber = State()


class engPersonalData(StatesGroup):
    engyonalish= State()
    engfullname = State()
    engresume = State()
    engphoneNumber = State()
