import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "15"))
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "20"))
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
ENABLE_YOUTUBE_SEARCH = os.getenv("ENABLE_YOUTUBE_SEARCH", "false").lower() == "true"
ITUNES_BASE_URL = os.getenv("ITUNES_BASE_URL", "https://itunes.apple.com/search")
MUSICBRAINZ_BASE_URL = os.getenv("MUSICBRAINZ_BASE_URL", "https://musicbrainz.org/ws/2")
DEEZER_BASE_URL = os.getenv("DEEZER_BASE_URL", "https://api.deezer.com")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
