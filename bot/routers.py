from aiogram import Dispatcher

from .commands.user import router_user_command

from .callbacks.callback_response import callback_router

routers_list = [
    router_user_command,
    callback_router
]

async def include_routers(dp: Dispatcher):
    for i in routers_list:
        dp.include_router(i)