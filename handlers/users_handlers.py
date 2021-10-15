from loader import dp, types
from data.database import users_db as db
from aiogram.types.chat import ChatType
from markups import reply, inline
from states import UserParams, GroupParams

users_dict_for_searching_olympiads = {}
num_to_subject = {1: 'Русский язык', 2: 'Литература', 3: 'Иностранные языки', 6: 'Математика', 7: 'Информатика', 8: 'История', 9: 'Обществознание', 10: 'География', 11: 'Биология', 12: 'Физика', 13: 'Химия', 14: 'Экономика', 15: 'Право', 16: 'ОБЖ', 17: 'Технология', 18: 'Искусство', 19: 'Физкультура', 20: 'Астрономия', 21: 'Экология', 22: 'ИЗО', 23: 'Предпринимательство', 24: 'Лингвистика', 27: 'Робототехника', 28: 'Психология', 31: 'Черчение'}

@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await db.add_new_user(user_id, user_name)
    await message.answer("Приветствую! Я бот, который поможет тебе не пропустить олимпиады по важным для тебя предметам! Введи команду /help, чтобы подробнее ознакомиться с моим функционалом", reply_markup=reply.default_user_markup)

@dp.message_handler(ChatType.is_private, commands='help')
async def tell_about_functions(message: types.Message):
    await message.answer("У меня есть 2 основные функции:\n"
                        "1. '🔍 Найти олимпиаду'\n"
                        "Эта функция позволяет найти информацию по конкретной олимпиаде.\n"
                        "Например: <b>Ломоносов</b>, <b>Высшая проба</b>.\n"
                        "2. '🔍 Олимпиады по предмету'\n"
                        "Эта функция поможет найти олимпиады по выбранному предмету с рейтингом выше 8.0, регистрация на которые начнется в ближайшую неделю.")



@dp.message_handler(ChatType.is_private, text = '🔍 Найти олимпиаду')
async def find_an_olympiad(message: types.Message):
    await message.answer('Ведите название олимпиады:')
    await UserParams.Setolympiad.set()

@dp.message_handler(state=UserParams.Setolympiad)
async def takeolimpyad(message: types.Message, state: UserParams.Setolympiad):
    user_id = message.from_user.id
    text = message.text
    users_dict_for_searching_olympiads[user_id] = [str(text)]
    await message.answer(f"Выберете количество олимпиад, которые получите по запросу <b>{text}</b>:", reply_markup=inline.numbers_1_8)
    await state.finish()

@dp.callback_query_handler(text_contains='number_')
async def takenumber_1_8(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    user_id = call.from_user.id
    num = call.data.split('_')[1]
    users_dict_for_searching_olympiads[user_id].append(num)
    #'''МЕСТО ДЛЯ ПАРСЕРА'''
    users_dict_for_searching_olympiads.pop(user_id, None)

@dp.message_handler(ChatType.is_private, text = '🔍 Олимпиады по предмету')
async def find_subjects_olympiads(message: types.Message):
    await message.answer('Выберете предмет, об олимпиадах которого вы бы хотели получить информацию:')
    await message.answer('Технические науки:', reply_markup=inline.technical_olympiads)
    await message.answer('Гуманитарные науки:', reply_markup=inline.humanitarian_olympiads)

@dp.callback_query_handler(text_contains='olymp_')
async def take_subject(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    unicum_num_subject = int(call.data.split('_')[1])
    await call.message.answer(f'Вот, какие олимпиады по предмету <b>{num_to_subject[unicum_num_subject]}</b> с рейтингом больше 8.0 мне удалось найти:')
    # '''Место для парсера'''










