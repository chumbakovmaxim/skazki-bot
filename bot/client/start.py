from aiogram import Router, Bot, types
from aiogram.filters import Command, Text

import messages as msg
from keyboards import start_keyboard

from bot.utils import get_menu_folders, get_folders_tree, get_folder_stat
from db.models import User

router = Router()


@router.callback_query(Text(startswith='start'))
@router.message(Command(commands=["start"]))
async def command_start_handler(
        message: types.Message | types.CallbackQuery,
        bot: Bot,
) -> None:
    """
    This handler receive messages with `/start` command
    """
    get_menu_folders()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if user_name is not None:
        user_name = f', {user_name}'
    else:
        user_name = ''

    await User.update_or_create(tg_user_id=user_id)

    await bot.send_message(
        chat_id=user_id,
        text=msg.start_message.format(name=user_name),
        reply_markup=start_keyboard()
    )
    if isinstance(message, types.CallbackQuery):
        await message.message.delete()
