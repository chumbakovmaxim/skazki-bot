from aiogram import Router, types, Bot
from aiogram.filters import Text
from aiogram.types import FSInputFile

import messages as msg
import buttons_texts as btn

router = Router()


@router.message(Text(startswith=btn.about_tails_text))
async def info_tails_handler(
        message: types.Message,
        bot: Bot,
) -> None:
    """
    Вывод сообщения с описанием проекта
    :param message: types.Message
    :param bot: Bot
    :return: None
    """
    image = FSInputFile(path='./images/tails.jpg')

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=image,
        caption=msg.about_tails_message
    )


@router.message(Text(startswith=btn.about_authors_text))
async def info_authors_handler(
        message: types.Message,
        bot: Bot,
) -> None:
    """
    Вывод сообщения с сылками на авторов и общей информацией
    :param message: types.Message
    :param bot: Bot
    :return: None
    """

    image = FSInputFile(path='./images/authors.jpg')

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=image,
        caption=msg.about_authors_message
    )
