from aiogram.types.chat import ChatType

import messages
from core.olymp import OlympItem
from core.olymps_parser.olymps_parser import OlympsParser
from data.database import users_db as db
from loader import dp, types
from markups import reply, inline
from states import UserParams

users_dict_for_searching_olympiads = {}
num_to_subject = {1: 'Русский язык', 2: 'Литература', 3: 'Иностранные языки', 6: 'Математика', 7: 'Информатика',
                  8: 'История', 9: 'Обществознание', 10: 'География', 11: 'Биология', 12: 'Физика', 13: 'Химия',
                  14: 'Экономика', 15: 'Право', 16: 'ОБЖ', 17: 'Технология', 18: 'Искусство', 19: 'Физкультура',
                  20: 'Астрономия', 21: 'Экология', 22: 'ИЗО', 23: 'Предпринимательство', 24: 'Лингвистика',
                  27: 'Робототехника', 28: 'Психология', 31: 'Черчение'}


@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await db.add_new_user(user_id, user_name)
    await message.answer(messages.welcome_message, reply_markup=reply.default_user_markup)


@dp.message_handler(ChatType.is_private, commands='help')
async def tell_about_functions(message: types.Message):
    await message.answer(messages.about_bot_message, reply_markup=reply.default_user_markup)


@dp.message_handler(ChatType.is_private, text='🔍 Найти олимпиаду')
async def find_an_olympiad(message: types.Message):
    await message.answer('Введите название олимпиады:')
    await UserParams.SetOlympiad.set()


@dp.message_handler(state=UserParams.SetOlympiad)
async def take_olympiad(message: types.Message, state: UserParams.SetOlympiad):
    user_id = message.from_user.id
    text = message.text
    users_dict_for_searching_olympiads[user_id] = [str(text)]
    await message.answer(f"Выберете количество олимпиад, которые получите по запросу <b>{text}</b>:",
                         reply_markup=inline.numbers_1_10)
    await state.finish()


@dp.callback_query_handler(text_contains='number_')
async def take_number_1_8(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    user_id = call.from_user.id
    num = int(call.data.split('_')[-1])
    users_dict_for_searching_olympiads[user_id].append(num)
    parser = OlympsParser(number_of_olymps=num)

    await call.message.answer("Начал поиск!")
    olymps = parser.get_olymps_by_request(request=users_dict_for_searching_olympiads[user_id][0])

    if len(olymps) == 0:
        await call.message.answer("По данному запросу ничего не найдено..")
    else:
        for olymp in olymps:
            await call.message.answer(get_message_of_olymp(olymp))

    users_dict_for_searching_olympiads.pop(user_id, None)


@dp.message_handler(ChatType.is_private, text='🔍 Олимпиады по предмету')
async def find_subjects_olympiads(message: types.Message):
    await message.answer('Выберете предмет, об олимпиадах которого вы бы хотели получить информацию:',
                         reply_markup=inline.olympiads)


@dp.callback_query_handler(text_contains='olymp_')
async def take_subject(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.edit_reply_markup(reply_markup=None)
    unicum_num_subject = call.data.split('_')[1]

    parser = OlympsParser(number_of_olymps=6)

    await call.message.answer("Начал поиск!")
    olymps = parser.get_olymps_by_subject(subject_id=unicum_num_subject)
    if len(olymps) == 0:
        await call.message.answer("По данному запросу ничего не найдено..")
    else:
        for olymp in olymps:
            await call.message.answer(get_message_of_olymp(olymp))

    users_dict_for_searching_olympiads.pop(user_id, None)


def get_message_of_olymp(olymp: OlympItem) -> str:
    return f'• <b>Ссылка:</b> <i>{olymp.link}</i>\n' \
           f'• <b>Название:</b> {olymp.olymp_title}\n' \
           f'• <b>Об олимпиаде:</b> {olymp.about_info}\n' \
           f'• <b>Классы:</b> {olymp.forms_participates}\n' \
           f'• <b>Дата регистрации:</b> {olymp.date_info}\n' \
           f'• <b>Рейтинг:</b> {olymp.rating}'
