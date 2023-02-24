import logging

import uvicorn

from aiogram import Bot, Dispatcher

import bot as botsource
import config as cnf
import setup

from config import WEBHOOK_URL
from db.database import init as db_init

dp = Dispatcher()

bot = Bot(cnf.TOKEN, parse_mode="HTML")


async def set_webhook() -> None:
    """
    Установка веб хука
    :return: None
    """
    await bot.set_webhook(url=WEBHOOK_URL,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)

    await bot.session.close()


async def main() -> None:
    """
    Импорт роутеров, подключение к БД, установка веб хука
    :return: None
    """
    dp.include_router(botsource.router)

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(__name__)

    dp.startup.register(setup.startup)
    dp.shutdown.register(setup.shutdown)

    await db_init()  # Подключение к БД

    await bot.delete_webhook()
    await bot.get_updates(offset=-1)
    await set_webhook()


if __name__ == "__main__":
    uvicorn.run('api.api:app', host='0.0.0.0', port=8443, loop='asyncio', use_colors=True, reload=False)
