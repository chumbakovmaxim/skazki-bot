import typing
from aiogram.types import FSInputFile


class ButtonsData(typing.TypedDict):
    text: str
    path: str


class Media(typing.TypedDict):
    audio: str | FSInputFile
    description: str
    photo: str | FSInputFile
