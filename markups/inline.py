from aiogram import types

technical_olympiads = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Математика", callback_data='olymp_6'),
        ],
        [
            types.InlineKeyboardButton(text="Информатика", callback_data='olymp_7'),
        ],
        [
            types.InlineKeyboardButton(text="Физика", callback_data='olymp_12'),
        ],
        [
            types.InlineKeyboardButton(text="Химия", callback_data='olymp_13'),
        ],
        [
            types.InlineKeyboardButton(text="Биология", callback_data='olymp_11'),
        ],
        [
            types.InlineKeyboardButton(text="География", callback_data='olymp_10'),
        ],
        [
            types.InlineKeyboardButton(text="Астрономия", callback_data='olymp_20'),
        ],
        [
            types.InlineKeyboardButton(text="Экология", callback_data='olymp_21'),
        ],
        [
            types.InlineKeyboardButton(text="Экономика", callback_data='olymp_14'),
        ],
        [
            types.InlineKeyboardButton(text="Технология", callback_data='olymp_17'),
        ],
        [
            types.InlineKeyboardButton(text="Робототехника", callback_data='olymp_27'),
        ],
        [
            types.InlineKeyboardButton(text="Черчение", callback_data='olymp_31'),
        ],
        [
            types.InlineKeyboardButton(text="Физкультура", callback_data='olymp_19'),
        ],
    ]
)
humanitarian_olympiads = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Русский язык", callback_data='olymp_1'),
        ],
        [
            types.InlineKeyboardButton(text="Иностранные языки", callback_data='olymp_3'),
        ],
        [
            types.InlineKeyboardButton(text="История", callback_data='olymp_8'),
        ],
        [
            types.InlineKeyboardButton(text="Литература", callback_data='olymp_2'),
        ],
        [
            types.InlineKeyboardButton(text="Лингвистика", callback_data='olymp_24'),
        ],
        [
            types.InlineKeyboardButton(text="ОБЖ", callback_data='olymp_16'),
        ],
        [
            types.InlineKeyboardButton(text="Обществознание", callback_data='olymp_9'),
        ],
        [
            types.InlineKeyboardButton(text="Предпринимательство", callback_data='olymp_23'),
        ],
        [
            types.InlineKeyboardButton(text="Право", callback_data='olymp_15'),
        ],
        [
            types.InlineKeyboardButton(text="Психология", callback_data='olymp_28'),
        ],
        [
            types.InlineKeyboardButton(text="ИЗО", callback_data='olymp_22'),
        ],
        [
            types.InlineKeyboardButton(text="Искусство", callback_data='olymp_18'),
        ]
    ]
)

numbers_1_8 = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="1", callback_data='number_1'),
            types.InlineKeyboardButton(text="2", callback_data='number_2'),
        ],
        [
            types.InlineKeyboardButton(text="3", callback_data='number_3'),
            types.InlineKeyboardButton(text="4", callback_data='number_4'),
        ],
        [
            types.InlineKeyboardButton(text="5", callback_data='number_5'),
            types.InlineKeyboardButton(text="6", callback_data='number_6'),
        ],
        [
            types.InlineKeyboardButton(text="7", callback_data='number_7'),
            types.InlineKeyboardButton(text="8", callback_data='number_8'),
        ]
    ]
)
