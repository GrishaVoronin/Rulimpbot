from loader import dp, types
from data.database import users_db as db
from aiogram.types.chat import ChatType
from markups import reply, inline
from states import UserParams
from core.olymps_parser.olymps_parser import OlympsParser

users_dict_for_searching_olympiads = {}


@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await db.add_new_user(user_id, user_name)
    await message.answer("Приветствую!", reply_markup=reply.default_user_markup)


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
async def take_number_1_8(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    user_id = call.from_user.id
    num = call.data.split('_')[1]
    users_dict_for_searching_olympiads[user_id].append(num)
    parser = OlympsParser(number_of_olymps=int(num))
    olymps = parser.get_olymps_by_request(request=users_dict_for_searching_olympiads[user_id][0])  # list[OlympItem]

    for olymp_item in olymps:
        olymp_title = olymp_item.olymp_title
        olymp_link = olymp_item.link
        message_to_user = f'<b>Название:</b> {olymp_title}\n......'
        await call.message.answer(message_to_user)

    users_dict_for_searching_olympiads.pop(user_id, None)
