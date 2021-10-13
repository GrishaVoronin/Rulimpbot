from loader import dp, types
from data.database import users_db as db
from aiogram.types.chat import ChatType


@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await db.add_new_user(user_id, user_name)
