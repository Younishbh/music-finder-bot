import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_TOKEN, ADMIN_ID
from database.db import init_db, upsert_user
from handlers.start import start_command
from handlers.search import search_command
from handlers.artist import artist_command
from handlers.history import history_command, delete_history_command
from handlers.favorites import favorites_command
from handlers.admin import admin_command

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("""📘 طريقة الاستخدام:

- أرسل اسم الأغنية أو اسم الفنان.
- أرسل كلمات الأغنية.
- أرسل رابط YouTube أو TikTok أو Instagram عند التوفر.
- استخدم /search و /artist.
- استخدم /history و /favorites.
""")


@dp.message_handler(commands=['settings'])
async def settings_command(message: types.Message):
    await message.answer("⚙️ الإعدادات:\n- اللغة: العربية\n- البحث: اسم الأغنية، اسم الفنان، كلمات الأغنية\n- سجل البحث: محفوظ محليًا")


@dp.message_handler(commands=['privacy'])
async def privacy_command(message: types.Message):
    await message.answer("""🔒 سياسة الخصوصية:

- يتم حفظ سجل البحث داخل قاعدة SQLite المحلية.
- لا يتم حفظ الملفات الصوتية إلا عند الحاجة ووفق إذن مناسب.
- لا يتم نشر بياناتك أو مشاركتها دون ضرورة.
""")


@dp.callback_query_handler(lambda c: c.data == 'start')
async def callback_start(callback_query: types.CallbackQuery):
    await start_command(callback_query.message)
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'search_song')
async def callback_search_song(callback_query: types.CallbackQuery):
    await callback_query.message.answer("أرسل اسم الأغنية أو اسم الفنان الآن.")
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'search_artist')
async def callback_search_artist(callback_query: types.CallbackQuery):
    await callback_query.message.answer("أرسل اسم الفنان الآن.")
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'history')
async def callback_history(callback_query: types.CallbackQuery):
    await history_command(callback_query.message)
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'help')
async def callback_help(callback_query: types.CallbackQuery):
    await help_command(callback_query.message)
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'settings')
async def callback_settings(callback_query: types.CallbackQuery):
    await settings_command(callback_query.message)
    await callback_query.answer()


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    pass


@dp.message_handler()
async def default_handler(message: types.Message):
    if message.text and message.text.startswith('/'):
        return
    if message.text:
        await message.answer("📌 أرسل اسم أغنية أو اسم فنان، أو استخدم /search")


async def on_startup(_):
    init_db()
    logging.info("Bot started successfully.")


if __name__ == '__main__':
    from handlers.start import register_handlers as register_start
    from handlers.search import register_handlers as register_search
    from handlers.artist import register_handlers as register_artist
    from handlers.history import register_handlers as register_history
    from handlers.favorites import register_handlers as register_favorites
    from handlers.admin import register_handlers as register_admin

    register_start(dp)
    register_search(dp)
    register_artist(dp)
    register_history(dp)
    register_favorites(dp)
    register_admin(dp)
    executor.start_polling(dp, on_startup=on_startup)
