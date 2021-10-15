from aiogram import types

default_user_markup = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='🔍 Найти олимпиаду'),
        ],
        [
            types.KeyboardButton(text='🔍 Олимпиады по предмету'),
        ],
    ],
    resize_keyboard=True
)
