from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm3
from core.filters.zapret import zapret
from core.keyboards.reply import adm, keyboard_nazad
from index import ADMIN_ID, ADMIN_1, ADMIN_2, ADMIN_3


async def get_th(message: Message, state: FSMContext):
    await message.answer(
        f"Здесь вы можете поделиться с нами своими идеями, предложениями.", reply_markup=keyboard_nazad)
    await message.answer(
        f"Введите свое предложение ✏️", reply_markup=keyboard_nazad)
    await state.set_state(StepsForm3.PREDLOG)


async def get_th_form(message: Message, state: FSMContext):
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
        await state.set_state(StepsForm3.PREDLOG)
    else:
        await message.answer(
            f"Напишите свой номер для связи с вами ☎️", reply_markup=keyboard_nazad)
        await state.update_data(predlog=message.text)
        await state.set_state(StepsForm3.GET_NUM)


async def get_num(message: Message, state: FSMContext, bot):
    spisok = message.text.split(' ')
    print(spisok)
    count = 0
    count1 = 0
    context_data = await state.get_data()
    predlog = context_data.get("predlog")
    data = f"🙋‍♂️ Предложение пользователя {message.from_user.first_name}:\n'{predlog}'\n☎️ Номер телефона для связи: {message.text}"
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
        await state.set_state(StepsForm3.GET_NUM)
    else:
        await bot.send_message(ADMIN_1, text=data)
        await bot.send_message(ADMIN_2, text=data)
        await bot.send_message(ADMIN_3, text=data)
        await message.answer(
            f"Ваше предложение отправлено, спасибо! 😇",
            reply_markup=adm)
        await state.clear()
