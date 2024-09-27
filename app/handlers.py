from aiogram import Bot, Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from app import states

user_router = Router()

@user_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager, bot: Bot):
    await dialog_manager.start(state=states.StartSG.start, mode=StartMode.RESET_STACK)

