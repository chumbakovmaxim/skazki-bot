from fastapi import Body, Response, BackgroundTasks
from starlette.status import HTTP_200_OK

from main import main
from main import bot, dp

from setup_api import app


@app.on_event('startup')
async def on_startup_() -> None:
    """
    Запуск бота после старта сервера
    :return: None
    """
    await main()


async def process_update_telegram_task(updates=Body(...)) -> None:
    """
    Обработка Update от Telegram в фоне
    :param updates: ответ от сервера
    :return: None
    """

    if not bot:
        return
    await dp.feed_raw_update(bot=bot, update=updates)


@app.post('/tg')
async def process_update_telegram(background_tasks: BackgroundTasks, updates=Body(...)) -> object:
    """
    Обработка запроса на /webhook_telegram
    :param background_tasks:
    :param updates:
    :return: object
    """
    background_tasks.add_task(process_update_telegram_task, updates)
    return Response(status_code=HTTP_200_OK)
