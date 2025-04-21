from aiogram import Dispatcher

from .handlers.user import router_handler_user

routers_list = [
    router_handler_user
]

async def include_routers(dp: Dispatcher):
    for i in routers_list:
        dp.include_router(i)