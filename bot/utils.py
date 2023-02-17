import os
from aiogram.types import FSInputFile
from tg_types import ButtonsData


def get_menu_folders() -> list[ButtonsData]:
    data: list[ButtonsData] = []
    root_path = './Сказки'
    # toDo Вынести путь в переменную
    for filename in os.listdir(root_path):
        data.append({
            'text': filename[3:],
            'path': f'/{filename[:3]}'
        })
    return data


def get_sub_menu_folders(path: str) -> list[ButtonsData]:
    data: list[ButtonsData] = []
    root_path = './Сказки'
    for filename in os.listdir(root_path + path):
        data.append({
            'text': filename[3:],
            'path': f'/{path}/{filename[:3]}'
        })
    print('get_sub_menu_folders', data)
    return data


def decode_callback_data(callback_data: ButtonsData) -> ButtonsData:
    root_path = './Сказки'
    path_array = callback_data['path'][1:].split('/')
    for path_piece in path_array:
        for folder_name in os.listdir(root_path):
            if folder_name[:3] == path_piece:
                root_path += f'/{folder_name}'

    return {
        'text': callback_data['text'],
        'path': root_path,
    }


def get_fairy_tails_content(path: str) -> dict[FSInputFile | str]:
    content = {}
    for filename in os.listdir('./Сказки' + path):
        if filename[-3:] == 'jpg':
            content['image'] = filename
        if filename[-3:] == 'txt':
            content['description'] = filename
        if filename[-3:] == 'mp3':
            content['audio'] = filename

    text_file = open(path + content['description'])
    audio = FSInputFile(path=path + content['audio'], filename=content['audi'])
    description = text_file.read()
    image = FSInputFile(path=path + content['image'])

    return {'audio': audio, 'description': description, 'image': image}
