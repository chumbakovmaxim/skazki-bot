import typing


class TopicItem(typing.TypedDict):
    text: str
    callback_data: str


class ButtonsData(typing.TypedDict):
    text: str
    path: str

