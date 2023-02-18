from aiogram import Router, types
from aiogram.filters import Text

import messages as msg
import buttons_texts as btn

router = Router()


@router.message(Text(startswith=btn.about_bot_text))
async def info_handler(
        message: types.Message,
) -> None:
    """
    Вывод сообщения с сылками на авторов и общей информацией
    :param message: types.Message
    :return: None
    """
    await message.answer(text=msg.info_message)
