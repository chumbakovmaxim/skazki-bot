"""Описание типов"""

import typing
from aiogram.types import FSInputFile


class ButtonsData(typing.TypedDict):
    text: str
    path: str


class Media(typing.TypedDict):
    audio: str | FSInputFile
    description: str
    photo: str | FSInputFile
    audio_name: str


class Stat(typing.TypedDict):
    menu: dict[str, int]
    sub_menu: dict[str, int]
    fairy_tail: dict[str, int]
