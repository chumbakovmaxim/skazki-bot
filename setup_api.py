"""Fast API"""
from fastapi import FastAPI


def create_app() -> FastAPI:
    application = FastAPI(title='FairyTails', debug=True)

    return application


app = create_app()
