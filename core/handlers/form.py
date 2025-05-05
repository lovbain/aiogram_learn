from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from core.keyboards.reply import keyboard_number, keyboard_nazad
from core.filters.zapret import zapret
from core.keyboards.reply import adm
from index import ADMIN_1, ADMIN_2, ADMIN_3



async def get_form(message: Message, state: FSMContext):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.clear()
    else:
        await message.answer(
            f"{message.from_user.first_name},\nДля наиболее коректного ответа нам нужно узнать ваше имя, фамилию, класс, возраст, номер телефона, чтобы связаться с вами через телеграмм. 💬\n\nНачинаем заполнять анкету. 📋\nВведите свою фамилию, имя ✏️",
            reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_NAME)
    else:
        await message.answer(f"Ваша фамилия, имя: {message.text}\r\nВ каком вы классе?\n(цифра и буква) ✏️",
                             reply_markup=keyboard_nazad)
        await state.update_data(name=message.text)
        await state.set_state(StepsForm.GET_CLASSS)


async def get_classs(message: Message, state: FSMContext):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_CLASSS)
    else:
        await message.answer(f"Ваш класс: {message.text}\r\nВведите свой возраст ✏️", reply_markup=keyboard_nazad)
        await state.update_data(classs=message.text)
        await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_AGE)
    else:
        await message.answer(f"Ваш возраст: {message.text}\r\nВведите свой вопрос ✏️", reply_markup=keyboard_nazad)
        await state.update_data(vozrast=message.text)
        await state.set_state(StepsForm.GET_VOPROS)

async def get_vopros(message: Message, state: FSMContext, ):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста, введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_VOPROS)
    else:
        await message.answer(f"Введите свой номер телефона ☎️", reply_markup=keyboard_nazad)
        await state.update_data(vopros=message.text)
        await state.set_state(StepsForm.GET_NUMBER)

async def get_number(message: Message, state: FSMContext):
    spisok = message.text.split(' ')
    count = 0
    count1 = 0
    for slova in spisok:
        for i in zapret:
            if i == slova:
                count += 1
            else:
                continue
    for i in zapret:
        if i in message.text:
            count1 += 1
        else:
            continue
    if count != 0 or count1 != 0:
        await message.answer(f"Я вас не понимаю, пожалуйста введите коректные данные 🙌",
                             reply_markup=keyboard_nazad)
        await state.set_state(StepsForm.GET_NUMBER)
    else:
        await message.answer(
            f"1 - Ничкова Полина Дмитриевна\n2 - Варфоломеева Юлия Сергеевна\n3 - Иванникова Полина Вячеславовна\nВыберите цифру психолога, которому вы хотите задать свой вопрос 🔢",
            reply_markup=keyboard_number)
        await state.update_data(number=message.text)
        await state.set_state(StepsForm.GET_PSYH)



async def get_psyh(message: Message, state: FSMContext, bot):
    context_data = await state.get_data()
    name = context_data.get("name")
    classs = context_data.get("classs")
    vozrast = context_data.get("vozrast")
    vopros = context_data.get("vopros")
    number = context_data.get("number")
    data_user = f"📝 Сохраненные данные:\r\n" \
                f" * Фамилия, имя: {name}\r\n" \
                f" * Класс: {classs}\r\n" \
                f" * Возраст: {vozrast}\n" \
                f" * Номер телефона: {number}\n" \
                f"Вопрос пользователя {message.from_user.first_name}: '{vopros}'\n\n"
    await message.answer(data_user)
    await state.clear()
    if message.text == "1":
        await message.answer(f"Спасибо, обращение отправлено Ничковой Полине Дмитриевне",
                             reply_markup=keyboard_nazad)
        await bot.send_message(ADMIN_1, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
    elif message.text == "2":
        await message.answer(f"Спасибо, обращение отправлено Варфоломеевой Юлии Сергеевне",
                             reply_markup=keyboard_nazad)
        await bot.send_message(ADMIN_2, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
    elif message.text == "3":
        await message.answer(f"Спасибо, обращение отправлено Иванниковой Полине Вячеславовне",
                             reply_markup=keyboard_nazad)
        await bot.send_message(ADMIN_3, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
    elif message.text == "Всем":
        await message.answer(f"Спасибо, обращение отправлено психологам",
                             reply_markup=keyboard_nazad)
        await bot.send_message(ADMIN_1, text=data_user)
        await bot.send_message(ADMIN_2, text=data_user)
        await bot.send_message(ADMIN_3, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
        await state.clear()
    else:
        await message.answer(f"Введите номер ✏️")