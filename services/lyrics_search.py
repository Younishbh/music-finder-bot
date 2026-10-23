import aiohttp


class LyricsSearchService:
    async def search(self, query: str):
        return {
            "status": "not_supported",
            "message": "خدمة كلمات الأغاني غير مفعلة حاليًا. استخدم اسم الأغنية أو الفنان، أو رابط المصدر الرسمي.",
            "results": [],
        }

    async def search_genius(self, query: str):
        return await self.search(query)
