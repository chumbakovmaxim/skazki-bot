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


class Type(Enum):
    RED = '1'
    BLUE = '2'
    GREEN = '3'


class Stat(typing.TypedDict):
    type: typing.Literal['Категория', 'Подкатегория', 'Сказка']
    name: str
    interaction_count: int
