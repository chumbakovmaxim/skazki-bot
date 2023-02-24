import typing
from typing import Union
from aiogram.types import FSInputFile
from enum import Enum


class ButtonsData(typing.TypedDict):
    text: str
    path: str


class Media(typing.TypedDict):
    audio: str | FSInputFile
    description: str
    photo: str | FSInputFile


class Stat(typing.TypedDict):
    menu: dict[str, int]
    sub_menu: dict[str, int]
    fairy_tail: dict[str, int]
