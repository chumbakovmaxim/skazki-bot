import os
from aiogram.types import FSInputFile
from tg_types import ButtonsData, Media, Stat
from db.models import User, MenuStat, SubMenuStat, FairyTailStat


def decode_path(path: str) -> str:
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

    return root_path


def encrypt_path(path: str) -> str:
    """
    Превращает путь вида
    './Сказки/004Иное/000Взаимопомощь/001Обыкновенный блокнот'
    в закодированный путь
    /004/000/001
    :param path: str
    :return: str
    """
    path = path.split('/')[2:]
    for index, item in enumerate(path):
        path[index] = item[:3]
    path = '/'.join(path)
    path = '/' + path

    return path


def get_name_from_path(path: str) -> str:
    """
    Возращает имя папки из пути
    ./Сказки/004Иное/000Взаимопомощь/001Обыкновенный блокнот
            =>
    Обыкновенный блокнот
    :param path: str
    :return: str
    """
    return path.split('/')[-1:][0][3:]


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

    return data


def get_sub_menu_folders(path: str) -> list[ButtonsData]:
    """
       Выводит массив типа ByttonsData. ByttonsData.path - папки вложенные в './Сказки/.../'
       :param path: str
       :return: list[ButtonsData]
    """
    data: list[ButtonsData] = []
    for filename in os.listdir(decode_path(path)):
        data.append({
            'text': filename[3:],
            'path': f'{path}/{filename[:3]}'
        })

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

    path = decode_path(path)
    for file in os.listdir(path):
        if file[-3:] == 'mp3':
            result['audio'] = FSInputFile(path=path + '/' + file, filename=file[:-4])
        if file[-3:] == 'txt':
            with open(path + '/' + file) as f:
                result['description'] = f.read()
        if file[-3:] == 'jpg':
            result['photo'] = FSInputFile(path=path + '/' + file)

    return result


def get_folders_tree(root_path: str = './Сказки') -> list[str]:
    """
    Возращает список закодированных путей
    ['/001', '/001/003', '/001/003/001', '/001/003/004', '/001/003/000', ... ]
    :param root_path: str
    :return: list[str]
    """
    result = []
    for filename in os.listdir(root_path):
        path = f'{root_path}/{filename}'
        if filename[:1] != '.' and os.path.isdir(path):
            result.append(encrypt_path(path))
            sub_folders = get_folders_tree(path)
            result += sub_folders

    return result


async def get_folder_stat():
    stat: list[Stat] = []
    folders_names = get_folders_tree()
    for folder_name in folders_names:

        if len(folder_name) == 4:
            menu_stat = (await MenuStat.all().filter(path=folder_name))
            if menu_stat is not None:
                print(menu_stat)
                print(len(menu_stat))

        if len(folder_name) == 8:
            sub_menu_stat = (await SubMenuStat.all().filter(path=folder_name))
            if sub_menu_stat is not None:
                print(len(sub_menu_stat))

        if len(folder_name) == 12:
            fairy_tail_stat = (await FairyTailStat.all().filter(path=folder_name))
            if fairy_tail_stat is not None:
                print(len(fairy_tail_stat))
