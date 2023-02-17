from aiogram import Router, types

import messages as msg
from keyboards import keyboard_constructor_fairy_tail
import buttons_texts as btn
from magic_filter import F

from keyboards import MenuCallbackFactory

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

    fairy_tail_number = callback_data.value

    names = btn.fairy_tails[fairy_tail_number]

    try:
        await query.message.edit_text(text=msg.fairy_tails_message,
                                      reply_markup=keyboard_constructor_fairy_tail(btn.fairy_tails, fairy_tail_number))
        await query.answer()
    except Exception as e:
        print(e)
        await query.message.answer(
            text=msg.fairy_tails_message,
            reply_markup=keyboard_constructor_fairy_tail(btn.fairy_tails, fairy_tail_number)
        )
