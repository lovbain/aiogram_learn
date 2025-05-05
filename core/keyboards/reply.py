from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Наш телеграмм канал"
        ),
        KeyboardButton(
            text="Записаться на консультацию"
        )
    ],
    [
        KeyboardButton(
            text="Задать вопрос психологу 🙋‍♂️"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", selective=True)

keyboard_1 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Анонимно 🙈"
        )],
        [KeyboardButton(
            text="Не анонимно 🐵"
        )],
        [KeyboardButton(
            text="Назад ⬅️"
        )]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", selective=True)


keyboard_nazad = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Назад ⬅️"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, selective=True)

adm = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Наш телеграмм канал 🙂"
        ),
        KeyboardButton(
            text="Записаться на консультацию 📝"
        )
    ],
    [
        KeyboardButton(
            text="Задать вопрос психологу 🙋‍♂️"
        ),
        KeyboardButton(
            text="Ваши предложения 🤝"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", selective=True)

keyboard_5 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Варфоломеева Юлия Сергеевна"
        ),
        KeyboardButton(
            text="Иванникова Полина Вячеславовна"
        ),
        KeyboardButton(
            text="Ничкова Полина Дмитриевна"
        ),
        KeyboardButton(
            text="Назад ⬅️"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", selective=True)


keyboard_number = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="1",
        )],
    [KeyboardButton(
        text="2"
    )],
    [KeyboardButton(
        text="3"
    )],
    [KeyboardButton(
        text="Всем"
    )],
    [KeyboardButton(
        text="Назад ⬅️"
    )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выбери кнопку", selective=True)