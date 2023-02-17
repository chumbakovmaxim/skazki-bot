from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from tg_types import TopicItem, ButtonsData
import buttons_texts as btn
from aiogram.filters.callback_data import CallbackData
from bot.utils import decode_callback_data


class MenuCallbackFactory(CallbackData, prefix="fmenu"):
    action: str
    value: str


# def keyboard_constructor_menu(buttons: list[TopicItem]):
#     """
#     Генерация inline клавиатуры по массиву с элементами типа KeyboardData
#     :return: InlineKeyboardMarkup
#     """
#     markup = []
#     for button in buttons:
#         markup.append(
#             [InlineKeyboardButton(text=button['text'],
#                                   callback_data=MenuCallbackFactory(action="sub_menu",
#                                                                     value=button['callback_data']).pack()), ])
#
#     markup.append([InlineKeyboardButton(text=btn.back_text, callback_data='start')])
#     kb = InlineKeyboardMarkup(inline_keyboard=markup)
#     return kb

# def keyboard_constructor_sub_menu(buttons: dict[str, list[TopicItem]], sub_topic_number: str):
#     """
#     Генерация inline клавиатуры по массиву с элементами типа KeyboardData
#     :return: InlineKeyboardMarkup
#     """
#     markup = []
#
#     buttons = buttons[sub_topic_number]
#
#     for button in buttons:
#         markup.append(
#             [InlineKeyboardButton(text=button['text'],
#                                   callback_data=MenuCallbackFactory(action="fairy_tail",
#                                                                     value=button['callback_data']).pack()), ])
#
#     markup.append([InlineKeyboardButton(text=btn.back_text, callback_data='menu')])
#     kb = InlineKeyboardMarkup(inline_keyboard=markup)
#     return kb


def keyboard_constructor_menu(buttons: list[ButtonsData]):
    """
    Генерация inline клавиатуры по массиву с элементами типа KeyboardData
    :return: InlineKeyboardMarkup
    """

    markup = []
    for button in buttons:
        markup.append(
            [InlineKeyboardButton(text=button['text'],
                                  callback_data=MenuCallbackFactory(action="sub_menu",
                                                                    value=button['path']).pack()), ])

    markup.append([InlineKeyboardButton(text=btn.back_text, callback_data='start')])
    kb = InlineKeyboardMarkup(inline_keyboard=markup)
    return kb


def keyboard_constructor_sub_menu(buttons: list[ButtonsData]):
    """
    Генерация inline клавиатуры по массиву с элементами типа KeyboardData
    :return: InlineKeyboardMarkup
    """
    markup = []

    for button in buttons:
        print('keyboard_constructor_sub_menu', button)
        markup.append(
            [InlineKeyboardButton(text=button['text'],
                                  callback_data=MenuCallbackFactory(action="fairy_tail",
                                                                    value=button['path']).pack()), ])

    markup.append([InlineKeyboardButton(text=btn.back_text, callback_data='menu')])
    kb = InlineKeyboardMarkup(inline_keyboard=markup)
    return kb


def keyboard_constructor_fairy_tail(buttons: list[ButtonsData]):
    """
    Генерация inline клавиатуры по массиву с элементами типа KeyboardData
    :return: InlineKeyboardMarkup
    """
    markup = []

    for button in buttons:
        markup.append(
            [InlineKeyboardButton(text=button['text'],
                                  callback_data=MenuCallbackFactory(action="audio",
                                                                    value=button['path']).pack()), ])

    markup.append([InlineKeyboardButton(text=btn.back_text,
                                        callback_data=MenuCallbackFactory(action="sub_menu",
                                                                          value=buttons[0]['path'][1:-4]).pack())])
    kb = InlineKeyboardMarkup(inline_keyboard=markup)
    return kb


def start_keyboard():
    """
    Генерация клавиатуры для стартового сообщения
    :return: ReplyKeyboardMarkup
    """
    markup = [
        [KeyboardButton(text=btn.fairy_tail_text)],
        [KeyboardButton(text=btn.about_bot_text)],
    ]
    kb = ReplyKeyboardMarkup(keyboard=markup, resize_keyboard=True)
    return kb
