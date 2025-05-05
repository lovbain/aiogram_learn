from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ssilka = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Ответы на анонимные вопросы",
            url="https://t.me/psy_fmsh"
        )
    ]
])

select_psych = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Ничкова Полина Дмитриевна",
            url="https://t.me/Polina_Nichkova"
        )
    ],
    [
        InlineKeyboardButton(
            text="Варфоломеева Юлия Сергеевна",
            url="https://t.me/Julia_Varfolomeeva"
        )
    ],
    [
        InlineKeyboardButton(
            text="Иванникова Полина Вячеславовна",
            url="https://t.me/polli_ivannikova"
        )
    ]
])