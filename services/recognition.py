class RecognitionService:
    def __init__(self, api_key=None):
        self.api_key = api_key

    async def recognize_audio(self, file_path: str):
        return {
            "status": "not_available",
            "message": "ميزة التعرف على الأغنية من الصوت غير متاحة حاليًا لأن الخدمة تتطلب مفتاح API خارجي.",
            "results": [],
        }
