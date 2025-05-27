from aiogram import Dispatcher

from .handlers.user import router_handler_user
from .commands.user import router_user_command
from .fsm.fsm_newuser import form_router

routers_list = [
    router_handler_user,
    form_router,
    router_user_command
]

async def include_routers(dp: Dispatcher):
    for i in routers_list:
        dp.include_router(i)