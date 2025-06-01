from aiogram import Dispatcher

from .handlers.user import router_handler_user
from .commands.user import router_user_command
from .fsm.support_message import form_router
from .callbacks.callback_response import callback_router

routers_list = [
    router_handler_user,
    form_router,
    router_user_command,
    callback_router
]

async def include_routers(dp: Dispatcher):
    for i in routers_list:
        dp.include_router(i)