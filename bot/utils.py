import os
from aiogram.types import FSInputFile
from tg_types import ButtonsData, Media


def decode_callback_data(path: str) -> str:
    root_path = './Сказки'
    path_array = path[1:].split('/')
    for path_piece in path_array:
        for folder_name in os.listdir(root_path):
            if folder_name[:3] == path_piece:
                root_path += f'/{folder_name}'

    return root_path


def get_menu_folders() -> list[ButtonsData]:
    data: list[ButtonsData] = []
    root_path = './Сказки'
    # toDo Вынести путь в переменную
    for filename in os.listdir(root_path):
        if filename[:1] != '.':
            data.append({
                'text': filename[3:],
                'path': f'/{filename[:3]}'
            })
    return data


def get_sub_menu_folders(path: str) -> list[ButtonsData]:
    data: list[ButtonsData] = []
    for filename in os.listdir(decode_callback_data(path)):
        data.append({
            'text': filename[3:],
            'path': f'{path}/{filename[:3]}'
        })
    return data


def get_content_from_folder(path: str) -> Media:
    result = {
        'audio': '',
        'description': '',
        'photo': '',
    }

    path = decode_callback_data(path)
    print('PATH get_content_from_folder', path)
    for file in os.listdir(path):
        if file[-3:] == 'mp3':
            result['audio'] = FSInputFile(path=path + '/' + file, filename=file[:-4])
        if file[-3:] == 'txt':
            with open(path + '/' + file) as f:
                result['description'] = f.read()
        if file[-3:] == 'jpg':
            result['photo'] = FSInputFile(path=path + '/' + file)
    print('RESULT get_content_from_folder', result)
    return result
