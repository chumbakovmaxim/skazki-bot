from __future__ import annotations
from tortoise.models import Model
from tortoise import fields


class FairyTailCache(Model):
    class Meta:
        table = "fairy_tails"

    local_file_id = fields.TextField(pk=True)
    tg_file_id = fields.TextField()


class User(Model):
    class Meta:
        table = 'users'

    tg_user_id = fields.BigIntField(pk=True)
    activity_time = fields.DatetimeField(auto_now=True)


class MenuStat(Model):
    class Meta:
        table = 'menu_stat'

    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path)


class SubMenuStat(Model):
    class Meta:
        tabel = 'sub_menu_stat'

    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path)


class FairyTailStat(Model):
    class Meta:
        table = 'fairy_tail_stat'

    path = fields.TextField()
    interaction_time = fields.DatetimeField(auto_now=True)

    @classmethod
    async def create_record(cls, tg_user_id: str | int, path: str) -> None:
        await User.update_or_create(tg_user_id=tg_user_id)
        await cls.update_or_create(path=path)
