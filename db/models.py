from __future__ import annotations
from tortoise.models import Model
from tortoise import fields
from datetime import datetime


class FairyTail(Model):
    class Meta:
        table = "fairy_tails"

    local_file_id = fields.TextField(pk=True)
    tg_file_id = fields.TextField()
