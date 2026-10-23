from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def home_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🔎 البحث عن أغنية", callback_data="search_song"),
        InlineKeyboardButton("🎤 البحث عن فنان", callback_data="search_artist"),
        InlineKeyboardButton("🕘 آخر عمليات البحث", callback_data="history"),
        InlineKeyboardButton("❓ طريقة الاستخدام", callback_data="help"),
        InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
    )
    return keyboard


def result_keyboard(items):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for idx, item in enumerate(items[:5], 1):
        keyboard.add(InlineKeyboardButton(f"{idx}. {item.title[:15]}", callback_data=f"track_{idx}"))
    keyboard.add(InlineKeyboardButton("↩️ رجوع", callback_data="start"))
    return keyboard
