from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
import asyncio
from app import states
from app.handlers import user_router
from app import dialogs
import config



bot = Bot(config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



async def main():
    dp.include_router(user_router)
    dp.include_router(dialogs.start_dialog)
    dp.include_router(dialogs.menu_dialog)
    dp.include_router(dialogs.monday_dialog)
    dp.include_router(dialogs.tuesday_dialog)
    dp.include_router(dialogs.wednesday_dialog)
    dp.include_router(dialogs.thursday_dialog)
    dp.include_router(dialogs.friday_dialog)
    dp.include_router(dialogs.saturday_dialog)
    dp.include_router(dialogs.help_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())