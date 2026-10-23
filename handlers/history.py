from aiogram import types
from aiogram.dispatcher import Dispatcher

from database.db import get_search_history, delete_search_history


async def history_command(message: types.Message):
    rows = get_search_history(message.from_user.id, limit=10)
    if not rows:
        await message.answer("لا توجد عمليات بحث سابقة.")
        return
    text = "🕘 آخر عمليات البحث:\n\n"
    for row in rows:
        text += f"• {row['query']} | {row['search_type']} | {row['created_at']}\n"
    await message.answer(text)


async def delete_history_command(message: types.Message):
    delete_search_history(message.from_user.id)
    await message.answer("✅ تم حذف سجل البحث الخاص بك.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(history_command, commands=["history"])
    dp.register_message_handler(delete_history_command, commands=["delete_history"])
