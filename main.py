from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import asyncio
from aiogram import F
from aiogram.filters import CommandStart

from core.keyboards.inline import select_psych
from core.utils.commands import set_commands
from core.keyboards.reply import keyboard_1, adm
from core.handlers import form, second_form, th_form
from core.utils.statesform import StepsForm, StepsForm2, StepsForm3
from index import ADMIN_ID, TOKEN


async def get_start(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id,
                           f"Здравствуйте, {message.from_user.first_name}!  👋\nВыберите кнопку для продолжения 👇",
                           reply_markup=adm)


async def vopros(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Как вы хотите задать свой вопрос?",
                           reply_markup=keyboard_1)


async def nazad1(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, text="Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот остановлен")


async def kanal(message: Message, bot: Bot):
    await message.answer('https://t.me/psy_fmsh!', reply_markup=adm)


async def vibor(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'К какому психологу вы хотите записаться на консультацию?',
                           reply_markup=select_psych)
    await message.answer(f"Вы вернулись в главное меню 🧑‍💻", reply_markup=adm)


async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, CommandStart())
    dp.message.register(kanal, F.text == 'Наш телеграмм канал 🙂')
    dp.message.register(vibor, F.text == 'Записаться на консультацию 📝')
    dp.message.register(vopros, F.text == 'Задать вопрос психологу 🙋‍♂️')
    dp.message.register(nazad1, F.text == "Назад ⬅️")
    dp.message.register(second_form.get_second_form, F.text == "Анонимно 🙈")
    dp.message.register(form.get_form, F.text == "Не анонимно 🐵")
    dp.message.register(th_form.get_th, F.text == "Ваши предложения 🤝")
    dp.message.register(th_form.get_th_form, StepsForm3.PREDLOG)
    dp.message.register(th_form.get_num, StepsForm3.GET_NUM)
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_classs, StepsForm.GET_CLASSS)
    dp.message.register(form.get_number, StepsForm.GET_NUMBER)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
    dp.message.register(form.get_vopros, StepsForm.GET_VOPROS)
    dp.message.register(form.get_psyh, StepsForm.GET_PSYH)
    dp.message.register(second_form.get_second_vopros, StepsForm2.VOPROS)
    dp.message.register(second_form.get_psyh, StepsForm2.GET_PSYH)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
