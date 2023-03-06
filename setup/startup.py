import db.database as db

async def startup() -> None:
    """
    Запуск функций для подключения к БД
    """
    print("Init started")
    # Init code here
    await db.migrate()
    await db.init()
    
    print ("Init finished")