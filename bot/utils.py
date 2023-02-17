import os
from aiogram.types import FSInputFile
from tg_types import ButtonsData


def get_menu_folders() -> list[ButtonsData]:
    data: list[ButtonsData] = []
    # toDo Вынести путь в переменную
    for filename in os.listdir('Сказки'):
        print(filename)
        data.append({
            'text': filename,
            'path': f'/{filename[2:]}'
        })
    print('get_menu_folders', data)
    return data


def get_sub_menu_folders(path: str) -> list[ButtonsData]:
    data: list[ButtonsData] = []
    for filename in os.listdir('Сказки' + path):
        data.append({
            'text': filename,
            'path': f'/{path[2:]}/{filename[2:]}'
        })
    print('get_sub_menu_folders', data)
    return data


def decode_callback_data(callback_data: ButtonsData) -> ButtonsData:
    # из /Вн/Ле получаем ['', 'Вн', 'Ле']
    path_array = callback_data['path'].split('/')
    path = './Сказки'
    for path_piece in path_array:
        for filename in os.listdir(path):
            if filename[2:] == path_piece and path_piece != '':
                path += f'/{filename}'
    print('decode_callback_data',{
        'text': callback_data['text'],
        'path': path,
    })
    return {
        'text': callback_data['text'],
        'path': path,
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
