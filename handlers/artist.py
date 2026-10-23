from aiogram import types
from aiogram.dispatcher import Dispatcher


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(lambda message: message.answer("🔎 جاري البحث عن الفنان..."), commands=["artist"])


async def artist_command(message: types.Message):
    query = message.get_args().strip()
    if not query:
        await message.answer("يرجى إدخال اسم الفنان، مثال: محمد السالم")
        return
    await message.answer(f"🔎 جاري البحث عن الفنان: {query}\n\nملاحظة: قد تختلف النتائج حسب مصدر البيانات المتاح.")


dp = None
