from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm2
from core.filters.zapret import zapret
from core.keyboards.inline import ssilka
from core.keyboards.reply import adm, keyboard_nazad, keyboard_number
from index import ADMIN_ID, ADMIN_1, ADMIN_2, ADMIN_3


async def get_second_form(message: Message, state: FSMContext):
    await message.answer(
        f"Отправляя анонимный вопрос, вы даете согласие на его публикацию в телеграмм канале 'Психологи ФМШ' по ссылке ниже. 👇\nПубликация не будет содержать никаких данных о пользователе кроме самого вопроса. 🤫",
        reply_markup=ssilka)
    await message.answer(
        f"Вы также можете задать свой вопрос лично психологу в переписке.\nДля этого нажмите на кнопку 'Записаться на консультацию' в главном меню. 🧑‍💻",
        reply_markup=keyboard_nazad)
    await message.answer(
        f"Введите свой вопрос ✏️", reply_markup=keyboard_nazad)
    await state.set_state(StepsForm2.VOPROS)


async def get_second_vopros(message: Message, state: FSMContext):
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
        await state.set_state(StepsForm2.VOPROS)
    else:
        await message.answer(
            f"1 - Ничкова Полина Дмитриевна\n2 - Варфоломеева Юлия Сергеевна\n3 - Иванникова Полина Вячеславовна\nВыберите психолога, которому вы хотите задать свой вопрос",
            reply_markup=keyboard_number)

        await state.update_data(vopros=message.text)
        await state.set_state(StepsForm2.GET_PSYH)


async def get_psyh(message: Message, state: FSMContext, bot):
    context_data = await state.get_data()
    vopros = context_data.get("vopros")
    data_user = f"Анонимное обращение 📨:\r\n" \
                f"'{vopros}'\n\n"
    data_user_for_user = f"Ваш анонимный вопрос ✉️:\r\n" \
                         f"'{vopros}'\n\n"
    if message.text == "1":
        await message.answer(data_user_for_user)
        await message.answer(
            f"Анонимный вопрос отправлен психологу. 📪\nСкоро вы получите ответ в телеграмм канале 'Психологи ФМШ' по кнопке ниже. 👇",
            reply_markup=ssilka)
        await bot.send_message(ADMIN_1, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
        await state.clear()
    elif message.text == "2":
        await message.answer(data_user_for_user)
        await message.answer(
            f"Анонимный вопрос отправлен психологу. 📪\nСкоро вы получите ответ в телеграмм канале 'Психологи ФМШ' по кнопке ниже. 👇",
            reply_markup=ssilka)
        await bot.send_message(ADMIN_2, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
        await state.clear()
    elif message.text == "3":
        await message.answer(data_user_for_user)
        await message.answer(
            f"Анонимный вопрос отправлен психологу. 📪\nСкоро вы получите ответ в телеграмм канале 'Психологи ФМШ' по кнопке ниже. 👇",
            reply_markup=ssilka)
        await bot.send_message(ADMIN_3, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
        await state.clear()
    elif message.text == "Всем":
        await message.answer(data_user_for_user)
        await message.answer(
            f"Анонимный вопрос отправлен психологам. 📪\nСкоро вы получите ответ в телеграмм канале 'Психологи ФМШ' по кнопке ниже. 👇",
            reply_markup=ssilka)
        await bot.send_message(ADMIN_1, text=data_user)
        await bot.send_message(ADMIN_2, text=data_user)
        await bot.send_message(ADMIN_3, text=data_user)
        await bot.send_message(ADMIN_ID, text=data_user)
        await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)
        await state.clear()
    else:
        await message.answer(f"Я вас не понимаю, пожалуйста, выберите психолога, которому вы хотите задать свой вопрос 🙌")