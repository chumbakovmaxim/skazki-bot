"""Fast API"""
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Инициализация FastApi
    """
    application = FastAPI(title='FairyTails', debug=True)

    return application


app = create_app()
