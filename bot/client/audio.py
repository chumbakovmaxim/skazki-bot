from aiogram import Router, types, Bot
from aiogram.types import FSInputFile
from magic_filter import F

from keyboards import MenuCallbackFactory
from db.models import FairyTail
from buttons_texts import fairy_tails

router = Router()


@router.callback_query(MenuCallbackFactory.filter(F.action == "audio"))
async def fairy_tail_handler(
        query: types.CallbackQuery,
        callback_data: MenuCallbackFactory,
        bot: Bot
) -> None:
    """
    Отправка аудио файла по его 'id' из fairy_tails
    :param query: types.CallbackQuery
    :param callback_data: MenuCallbackFactory
    :param bot: Bot
    :return: None
    """
    user_id = query.from_user.id
    fairy_tail_number = callback_data.value
    fairy_tail_name = 'сказка'

    for index in fairy_tails:
        for item in fairy_tails[index]:
            if item['callback_data'] == fairy_tail_number:
                fairy_tail_name = item['text']

    audio = FSInputFile(path=f"./audio/{fairy_tail_number}.mp3", filename=f'{fairy_tail_name}.mp3')

    try:
        file = await FairyTail.get_or_none(local_file_id=fairy_tail_number)
        # Если аудио уже было отправлено и есть на серверах ТГ, то отправляем файл по file_id
        if file is not None:
            await bot.send_audio(chat_id=user_id, audio=file.tg_file_id, performer='Сказки для жизни')
        else:
            audio_message: types.Message = await bot.send_audio(chat_id=user_id, audio=audio)
            await FairyTail.update_or_create(local_file_id=fairy_tail_number, tg_file_id=audio_message.audio.file_id)
    except Exception as e:
        print(e)
        await query.message.answer(text='Упс! Что-то пошло не так')
    await query.answer()
