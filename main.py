import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', )

if name == 'main':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp)