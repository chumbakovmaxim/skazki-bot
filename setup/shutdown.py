import db.database as db


async def shutdown() -> None:
    """
    Закрытие базы данных
    """
    print("Shutdown started")
    # Shutdown code here
    await db.close()

    print("Shutdown finished")
