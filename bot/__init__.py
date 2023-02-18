from aiogram import Router
from bot.client import start, menu, sub_menu, fairy_tail, info, audio
from bot.admin import main as admin

router = Router()
router.include_router(start.router)
router.include_router(menu.router)
router.include_router(sub_menu.router)
router.include_router(fairy_tail.router)
router.include_router(info.router)
router.include_router(audio.router)
