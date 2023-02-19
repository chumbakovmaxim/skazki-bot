from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters import CommandObject

from config import ADMIN_PASSWORD
from db.models import User
import messages as msg
from bot.utils import get_folder_stat, get_active_users_count, get_content_rating, genetate_excel_stat
from tg_types import Stat

router = Router()


@router.message(Command('admin'))
async def admin_authorization(message: types.Message, command: CommandObject) -> None:
    """
    Авторизация администратора

    :param message:
    :param command: Аргументы из сообщения (user_id)
    :return: None
    """
    if command.args == ADMIN_PASSWORD:
        # Регистрация админа
        await User.filter(tg_user_id=message.from_user.id).update(is_admin=True)
        await message.answer(msg.admin_success_message)


@router.message(Command('stat'))
async def stat(message: types.Message) -> None:
    """
    Функция для вывода статистики
    :param message:
    :return: None
    """
    try:
        is_admin: bool = (await User.get_or_none(tg_user_id=message.from_user.id)).is_admin
    except Exception as e:
        print(e)
        is_admin = False

    if not is_admin:
        return

    text = ''
    statistic: Stat = await get_folder_stat()
    active_users = await get_active_users_count()
    await get_content_rating()
    await genetate_excel_stat()

    await message.answer(f'{active_users["per_day"]}  {active_users["per_week"]}')
