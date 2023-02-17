from aiogram import Router, types

import messages as msg
from keyboards import keyboard_constructor_sub_menu
import buttons_texts as btn
from magic_filter import F

from keyboards import MenuCallbackFactory
from bot.utils import get_sub_menu_folders

router = Router()


@router.callback_query(MenuCallbackFactory.filter(F.action == "sub_menu"))
async def sub_menu_handler(
        query: types.CallbackQuery,
        callback_data: MenuCallbackFactory
) -> None:
    """
    Выводит пункты подменю (меню второго уровня вложенности)
    :param query: types.CallbackQuery
    :param callback_data: MenuCallbackFactory
    :return: None
    """
    path = callback_data.value

    sub_menu_folders = get_sub_menu_folders(path)
    try:
        await query.message.edit_text(text=msg.fairy_tails_message,
                                      reply_markup=keyboard_constructor_sub_menu(sub_menu_folders))
        await query.answer()
    except Exception as e:
        print(e)
        await query.message.answer(
            text=msg.fairy_tails_message,
            reply_markup=keyboard_constructor_sub_menu(sub_menu_folders)
        )
