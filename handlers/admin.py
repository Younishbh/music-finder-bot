from aiogram import types
from aiogram.dispatcher import Dispatcher

from config import ADMIN_ID
from database.db import stats_search_count, stats_users_count


async def admin_command(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("🚫 ليس لديك صلاحية الوصول إلى لوحة الإدارة.")
        return

    text = f"""📊 لوحة الإدارة

- عدد المستخدمين: {stats_users_count()}
- عدد عمليات البحث: {stats_search_count()}
- حالة خدمات البحث: تعمل عبر iTunes وMusicBrainz
- حالة البوت: online
- وقت التشغيل: مستمر
"""
    await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_command, commands=["admin"])
