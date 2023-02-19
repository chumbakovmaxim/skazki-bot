import os
from pypika.terms import Parameter, Interval
import xlsxwriter

from aiogram.types import FSInputFile
from tg_types import ButtonsData, Media, Stat
from db.models import MenuStat, SubMenuStat, FairyTailStat, User


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


async def get_folder_stat() -> Stat:
    stat: Stat = {'menu': {}, 'sub_menu': {}, 'fairy_tail': {}}
    folders_names = get_folders_tree()
    for folder_name in folders_names:
        if len(folder_name) == 4:
            menu_stat = (await MenuStat.all().filter(path=folder_name))
            for menu_item in menu_stat:
                name = get_name_from_path(decode_path(menu_item.path))
                if name not in stat['menu'].keys():
                    stat['menu'][name] = 1
                else:
                    stat['menu'][name] += 1
            if len(menu_stat) == 0:
                name = get_name_from_path(decode_path(folder_name))
                stat['menu'][name] = 0

        if len(folder_name) == 8:
            sub_menu_stat = (await SubMenuStat.all().filter(path=folder_name))
            for sub_menu_item in sub_menu_stat:
                name = get_name_from_path(decode_path(sub_menu_item.path))
                if name not in stat['sub_menu'].keys():
                    stat['sub_menu'][name] = 1
                else:
                    stat['sub_menu'][name] += 1
            if len(sub_menu_stat) == 0:
                name = get_name_from_path(decode_path(folder_name))
                stat['sub_menu'][name] = 0

        if len(folder_name) == 12:
            fairy_tail_stat = (await FairyTailStat.all().filter(path=folder_name))
            for fairy_tail_item in fairy_tail_stat:
                name = get_name_from_path(decode_path(fairy_tail_item.path))
                if name not in stat['fairy_tail'].keys():
                    stat['fairy_tail'][name] = 1
                else:
                    stat['fairy_tail'][name] += 1
            if len(fairy_tail_stat) == 0:
                name = get_name_from_path(decode_path(folder_name))
                stat['fairy_tail'][name] = 0

    print(stat)
    return stat


async def get_users_count() -> int:
    users_count = await User.all().count()
    return users_count


async def get_active_users_count() -> dict[str, int]:
    result = {'per_day': 0, 'per_week': 0}
    active_users_per_day = await User.filter(activity_time__gte=Parameter("CURRENT_DATE") - Interval(days=1)).count()
    active_users_per_week = await User.filter(activity_time__gte=Parameter("CURRENT_DATE") - Interval(days=7)).count()

    result['per_day'] = active_users_per_day
    result['per_week'] = active_users_per_week
    print(result)
    return result


async def get_content_rating() -> []:
    result = []
    # for item in fairy_tails_per_day:
    #     name = get_name_from_path(decode_path(item.path))
    #     if name not in result['per_day'].keys():
    #         result['per_day'][name] = 1
    #     else:
    #         result['per_day'][name] += 1
    #
    # for item in fairy_tails_per_week:
    #     name = get_name_from_path(decode_path(item.path))
    #     if name not in result['per_week'].keys():
    #         result['per_week'][name] = 1
    #     else:
    #         result['per_week'][name] += 1

    folders = get_folders_tree()
    fairy_tails_folders = [x for x in folders if len(x) == 12]
    for fairy_tail in fairy_tails_folders:
        name = get_name_from_path(decode_path(fairy_tail))
        fairy_tails_per_day_count = await FairyTailStat.filter(
            interaction_time__gte=Parameter("CURRENT_DATE") - Interval(days=1)).filter(path=fairy_tail).count()
        fairy_tails_per_week_count = await FairyTailStat.filter(
            interaction_time__gte=Parameter("CURRENT_DATE") - Interval(days=7)).filter(path=fairy_tail).count()

        result.append({
            'name': name,
            'per_day': fairy_tails_per_day_count,
            'per_week': fairy_tails_per_week_count
        })

    print(result)
    return result


async def genetate_excel_stat():
    workbook = xlsxwriter.Workbook('stat.xlsx')
    cell_format = workbook.add_format()
    cell_format.set_text_wrap()

    sheet_count = workbook.add_worksheet("Общее кол-во пользователей").set_column(0, 1, 15)
    sheet_interaction_count = workbook.add_worksheet("Кол-во запусков контента").set_column(0, 1, 15)
    sheet_rating = workbook.add_worksheet("Рейтинг").set_column(0, 5, 15)

    users_count = await get_users_count()
    sheet_count.write(0, 0, 'Общее кол-во пользователей')
    sheet_count.write(0, 1, users_count)

    active_users = await get_active_users_count()
    sheet_count.write(1, 0, 'Кол-во активных пользователей за день')
    sheet_count.write(1, 1, active_users['per_day'])
    sheet_count.write(2, 0, 'Кол-во активных пользователей за неделю')
    sheet_count.write(2, 1, active_users['per_week'])

    content_rating = await get_content_rating()
    sheet_interaction_count.write(0, 1, 'За день')
    sheet_interaction_count.write(0, 2, 'За неделю')
    for index, item in enumerate(content_rating):
        sheet_interaction_count.write(index + 1, 0, item['name'])
        sheet_interaction_count.write(index + 1, 1, item['per_day'])
        sheet_interaction_count.write(index + 1, 2, item['per_week'])

    folders_stat = await get_folder_stat()
    sheet_rating.write(0, 0, 'Проблема')
    sheet_rating.write(0, 2, 'Проблема')
    sheet_rating.write(0, 4, 'Сказка')
    for index, menu_item in enumerate(folders_stat['menu']):
        sheet_rating.write(index + 1, 0, menu_item)
        sheet_rating.write(index + 1, 1, folders_stat['menu'][menu_item])

    for index, sub_menu_item in enumerate(folders_stat['sub_menu']):
        sheet_rating.write(index + 1, 2, sub_menu_item)
        sheet_rating.write(index + 1, 3, folders_stat['sub_menu'][sub_menu_item])

    for index, fairy_tail_item in enumerate(folders_stat['fairy_tail']):
        sheet_rating.write(index + 1, 4, fairy_tail_item)
        sheet_rating.write(index + 1, 5, folders_stat['fairy_tail'][fairy_tail_item])

    workbook.close()
