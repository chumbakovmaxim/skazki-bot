import os
from aiogram.types import FSInputFile
from tg_types import ButtonsData, Media
from db.models import User, MenuStat, SubMenuStat, FairyTailStat


def decode_callback_data(path: str) -> str:
    """
    Расшифровывает строку типа /000/000/000 в полноценный путь ./Сказки/000Семья/000Дети/000Дело не в точках
    :param path: str
    :return: str
    """

    root_path = './Сказки'
    path_array = path[1:].split('/')
    for path_piece in path_array:
        for folder_name in os.listdir(root_path):
            if folder_name[:3] == path_piece:
                root_path += f'/{folder_name}'
    print('decode_callback_data', root_path)
    return root_path


def get_menu_folders() -> list[ButtonsData]:
    """
    Выводит массив типа ByttonsData. ByttonsData.path - папки вложенные в './Сказки'
    :return: list[ButtonsData]
    """
    data: list[ButtonsData] = []
    root_path = './Сказки'
    # toDo Вынести путь в переменную
    for filename in os.listdir(root_path):
        if filename[:1] != '.':
            data.append({
                'text': filename[3:],
                'path': f'/{filename[:3]}'
            })
    print('get_menu_folders', data)
    return data


def get_sub_menu_folders(path: str) -> list[ButtonsData]:
    """
       Выводит массив типа ByttonsData. ByttonsData.path - папки вложенные в './Сказки/.../'
       :param path: str
       :return: list[ButtonsData]
    """
    data: list[ButtonsData] = []
    for filename in os.listdir(decode_callback_data(path)):
        data.append({
            'text': filename[3:],
            'path': f'{path}/{filename[:3]}'
        })
    print('get_sub_menu_folders', data)
    return data


def get_content_from_folder(path: str) -> Media:
    """
    Выводит изображение, описание сказки и аудиофайл со сказкой в формате Media.
    :param path: str
    :return: Media
    """
    result = {
        'audio': '',
        'description': '',
        'photo': '',
    }

    path = decode_callback_data(path)
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


def get_folders_tree(root_path='./Сказки') -> list[str]:
    result = []
    for filename in os.listdir(root_path):
        if filename[:1] != '.' and os.path.isdir(f'{root_path}/{filename}'):
            result.append(f'{root_path}/{filename}')
            sub_folders = get_folders_tree(root_path + f'/{filename}')
            result += sub_folders

    return result


def get_folder_stat():
    pass
