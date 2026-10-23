from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.db import add_search_history
from services.music_search import MusicSearchService
from utils.validators import clean_query


async def search_command(message: types.Message):
    query = clean_query(message.get_args())
    if not query:
        await message.answer("يرجى إدخال اسم الأغنية أو اسم الفنان، مثال: محمد السالم")
        return

    await message.answer("🔎 جاري البحث...")
    service = MusicSearchService(timeout=15)
    results = await service.search(query)

    if not results:
        await message.answer("لم أجد نتائج مطابقة من المصادر المتاحة. جرّب اسمًا مختلفًا أو أرسل رابطًا/مقطعًا صوتيًا.")
        return

    add_search_history(message.from_user.id, query, "search", len(results))

    text = f"🎵 نتائج البحث عن: {query}\n\n"
    for idx, item in enumerate(results[:5], 1):
        duration = ""
        if item.duration_ms:
            total_seconds = item.duration_ms / 1000
            minutes = int(total_seconds // 60)
            seconds = int(total_seconds % 60)
            duration = f"⏱️ {minutes}:{seconds:02d}"
        text += f"{idx}. {item.title}\n"
        text += f"🎤 الفنان: {item.artist}\n"
        if item.album:
            text += f"💿 الألبوم: {item.album}\n"
        if duration:
            text += f"{duration}\n"
        if item.source_url:
            text += f"🔗 {item.source_url}\n"
        text += "\n"

    keyboard = InlineKeyboardMarkup(row_width=2)
    for idx, item in enumerate(results[:5], 1):
        keyboard.add(InlineKeyboardButton(f"{idx}. {item.title[:15]}", callback_data=f"track_{idx}"))
    keyboard.add(InlineKeyboardButton("↩️ رجوع", callback_data="start"))
    await message.answer(text, reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(search_command, commands=["search"])
