from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME = State()
    GET_AGE = State()
    GET_CLASSS = State()
    GET_VOPROS = State()
    GET_PSYH = State()
    GET_CONTACT = State()
    GET_NUMBER = State()


class StepsForm2(StatesGroup):
    VOPROS = State()
    GET_PSYH = State()

class StepsForm3(StatesGroup):
    PREDLOG = State()
    GET_NUM = State()