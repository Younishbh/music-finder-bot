from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.db import add_search_history, get_search_history
from services.music_search import MusicSearchService
from utils.validators import clean_query


async def start_command(message: types.Message):
    text = """👋 مرحبًا بك في بوت البحث عن الموسيقى!

🎶 أستطيع مساعدتك في العثور على الأغاني والمعلومات الموسيقية. أرسل لي أحد الخيارات التالية:

🎵 اسم الأغنية أو اسم الفنان
🔤 كلمات من الأغنية
🎙 تسجيل صوتي للتعرّف على الأغنية، عند دعم هذه الميزة
📹 مقطع فيديو يحتوي على موسيقى، عند دعم هذه الميزة
🔗 رابط أغنية أو فيديو من منصة مدعومة
🔍 ابحث عن أغنيتك المفضلة واستمتع!
"""
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🔎 البحث عن أغنية", callback_data="search_song"),
        InlineKeyboardButton("🎤 البحث عن فنان", callback_data="search_artist"),
        InlineKeyboardButton("🕘 آخر عمليات البحث", callback_data="history"),
        InlineKeyboardButton("❓ طريقة الاستخدام", callback_data="help"),
        InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
    )
    await message.answer(text, reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
