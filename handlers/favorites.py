from aiogram import types
from aiogram.dispatcher import Dispatcher

from database.db import get_favorites


async def favorites_command(message: types.Message):
    rows = get_favorites(message.from_user.id)
    if not rows:
        await message.answer("لا توجد أغاني مفضلة حتى الآن.")
        return
    text = "💖 المفضلة:\n\n"
    for row in rows:
        text += f"• {row['track_title']} — {row['artist_name']}\n🔗 {row['source_url']}\n\n"
    await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(favorites_command, commands=["favorites"])
