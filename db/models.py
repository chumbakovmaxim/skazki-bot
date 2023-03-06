from __future__ import annotations
from tortoise.models import Model
from tortoise import fields
from uuid import uuid4


class FairyTailCache(Model):
    """
    Сохранение file_id аудиофайлов сказок.
    При повторной отправке аудиофайла бот берет file_id из этой таблицы
    """

    class Meta:
        table = "fairy_tails"

    local_file_id = fields.TextField(pk=True)
    tg_file_id = fields.TextField()


class ImageCache(Model):
    """
    Сохранение file_id картинок.
    При повторной отправке аудиофайла бот берет file_id из этой таблицы

    local_file_id = Сокращенный путь до файла
    tg_file_id = file_id файла на серверах telegram
    """

    class Meta:
        table = "images"

    local_file_id = fields.TextField(pk=True)
    tg_file_id = fields.TextField()


class User(Model):
    """
    Сущность пользователя

    tg_user_id = Телеграм id пользователя
    is_admin = Является ли админом
    activity_time = Время и дата, когда в последний раз пользователь нажимал на кнопки в боте
    """

    class Meta:
        table = 'users'

    tg_user_id = fields.BigIntField(pk=True)
    is_admin = fields.BooleanField(default=False)
    activity_time = fields.DatetimeField(auto_now=True)


class MenuStat(Model):
    """
    Статистика по папкам меню

    id = uuid
    path = сокращенный путь до папки
    interaction_time = время и дата когда пользователь в последний раз нажимал на эту папку
    """
    class Meta:
        table = 'menu_stat'

    id = fields.TextField(pk=True)
    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path, id=uuid4())


class SubMenuStat(Model):
    """
    Статистика по папкам подменю

    id = uuid
    path = сокращенный путь до папки
    interaction_time = время и дата когда пользователь в последний раз нажимал на эту папку
    """
    class Meta:
        tabel = 'sub_menu_stat'

    id = fields.TextField(pk=True)
    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path, id=uuid4())


class FairyTailStat(Model):
    """
    Статистика по папкам cо сказками

    id = uuid
    path = сокращенный путь до папки
    interaction_time = время и дата когда пользователь в последний раз нажимал на эту папку
    """
    class Meta:
        table = 'fairy_tail_stat'

    id = fields.TextField(pk=True)
    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path, id=uuid4())
