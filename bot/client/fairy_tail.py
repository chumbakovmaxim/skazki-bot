from aiogram import Router, types

import messages as msg
from bot.utils import get_sub_menu_folders
from keyboards import keyboard_constructor_fairy_tail
from magic_filter import F

from keyboards import MenuCallbackFactory
from db.models import SubMenuStat

router = Router()


@router.callback_query(MenuCallbackFactory.filter(F.action == "fairy_tail"))
async def fairy_tail_handler(
        query: types.CallbackQuery,
        callback_data: MenuCallbackFactory
) -> None:
    """
    Выводит кнопки для выбора сказки
    :param query: types.CallbackQuery
    :param callback_data: MenuCallbackFactory
    :return: None
    """

    path = callback_data.value
    fairy_tail_path = get_sub_menu_folders(path)

    await SubMenuStat.create_record(query.from_user.id, path)

    try:
        await query.message.edit_text(text=msg.fairy_tails_message,
                                      reply_markup=keyboard_constructor_fairy_tail(fairy_tail_path))
        await query.answer()
    except Exception as e:
        print(e)
        await query.message.answer(
            text=msg.fairy_tails_message,
            reply_markup=keyboard_constructor_fairy_tail(fairy_tail_path)
        )
