from aiogram import Router, types, Bot
from magic_filter import F

from keyboards import MenuCallbackFactory
from db.models import FairyTailCache, FairyTailStat
from bot.utils import get_content_from_folder


router = Router()


@router.callback_query(MenuCallbackFactory.filter(F.action == "audio"))
async def fairy_tail_handler(
        query: types.CallbackQuery,
        callback_data: MenuCallbackFactory,
        bot: Bot
) -> None:
    """
    Отправка аудио файла и картинки с описанием сказки
    :param query: types.CallbackQuery
    :param callback_data: MenuCallbackFactory
    :param bot: Bot
    :return: None
    """
    user_id = query.from_user.id
    fairy_tail_path = callback_data.value
    media = get_content_from_folder(fairy_tail_path)

    await FairyTailStat.create_record(user_id, fairy_tail_path)

    audio = media['audio']
    description = media['description']
    image = media['photo']
    print(audio)

    try:
        file = await FairyTailCache.get_or_none(local_file_id=fairy_tail_path)
        await bot.send_photo(
            chat_id=user_id,
            photo=image,
            caption=description
        )
        # Если аудио уже было отправлено и есть на серверах ТГ, то отправляем файл по file_id
        if file is not None:
            print('AUDION FROM DB')
            await bot.send_audio(
                chat_id=user_id,
                audio=file.tg_file_id,
                performer='Сказки для жизни'
            )
        else:
            print('AUDION FROM FILE')
            audio_message: types.Message = await bot.send_audio(chat_id=user_id, audio=audio)
            await FairyTailCache.update_or_create(
                local_file_id=fairy_tail_path,
                tg_file_id=audio_message.audio.file_id
            )
    except Exception as e:
        print(e)
        await query.message.answer(text='Здесь будут сказки!')
    await query.answer()
