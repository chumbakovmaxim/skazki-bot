from tortoise import Tortoise
from aerich import Command
import config

TORTOISE_ORM = {
    "connections": {"default": config.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init() -> None:
    """
    Инициалищация БД и генерация сущностей
    :return: None
    """
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def close() -> None:
    """
    Дисконнект с базой данных
    :return:
    """
    await Tortoise.close_connections()


async def migrate() -> None:
    command = Command(tortoise_config=TORTOISE_ORM)
    await command.init()
    await command.upgrade()
