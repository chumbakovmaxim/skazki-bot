from aiogram import Router, Bot, types
from aiogram.filters import Text

import messages as msg
from keyboards import keyboard_constructor_menu
import buttons_texts as btn
from bot.utils import get_menu_folders

router = Router()


@router.callback_query(Text(startswith='menu'))
@router.message(Text(startswith=btn.fairy_tail_text))
async def menu_handler(
        message: types.Message | types.CallbackQuery,
        bot: Bot
) -> None:
    """
    Выводит пункты главного меню
    :param message: types.Message | types.CallbackQuery
    :param bot: Bot
    :return: None
    """
    user_id = message.from_user.id
    menu_folders = get_menu_folders()
    print(menu_folders)

    if isinstance(message, types.Message):
        await bot.send_message(
            chat_id=user_id,
            text=msg.fairy_tails_message,
            reply_markup=keyboard_constructor_menu(menu_folders)
        )
    else:
        try:
            await bot.edit_message_text(
                message_id=message.message.message_id,
                chat_id=user_id,
                text=msg.fairy_tails_message,
                reply_markup=keyboard_constructor_menu(menu_folders)
            )
        except Exception as e:
            print(e)
            await bot.send_message(
                chat_id=user_id,
                text=msg.fairy_tails_message,
                reply_markup=keyboard_constructor_menu(menu_folders)
            )