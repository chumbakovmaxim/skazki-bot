from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram.types import FSInputFile
import os

from config import ADMIN_PASSWORD
from db.models import User
import messages as msg
from bot.utils import generate_excel_stat

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
async def stat(message: types.Message, bot: Bot) -> None:
    """
    Функция для вывода статистики
    :param message:
    :param bot: Bot
    :return: None
    """
    try:
        is_admin: bool = (await User.get_or_none(tg_user_id=message.from_user.id)).is_admin
    except Exception as e:
        print(e)
        is_admin = False

    if not is_admin:
        return

    await generate_excel_stat()

    stat_file = FSInputFile(path='stat.xlsx')
    try:
        await bot.send_document(chat_id=message.from_user.id, document=stat_file)
    except Exception as e:
        print(e)
    try:
        os.remove('stat.xlsx')
    except Exception as e:
        print(e)
