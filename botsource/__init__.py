from aiogram import Router
from botsource.client import start, menu, sub_menu, fairy_tail, info, audio
from botsource.admin import main as admin
from botsource import utils

router = Router()
router.include_router(start.router)
router.include_router(menu.router)
router.include_router(sub_menu.router)
router.include_router(fairy_tail.router)
router.include_router(info.router)
router.include_router(audio.router)
router.include_router(admin.router)
