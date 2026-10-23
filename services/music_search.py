import asyncio
from urllib.parse import quote

import aiohttp


class MusicTrack:
    def __init__(self, title, artist, album=None, duration_ms=None, artwork_url=None, source_url=None, track_id=None, source_name='unknown'):
        self.title = title or 'غير متوفر'
        self.artist = artist or 'غير متوفر'
        self.album = album or 'غير متوفر'
        self.duration_ms = duration_ms
        self.artwork_url = artwork_url
        self.source_url = source_url
        self.track_id = str(track_id or source_name)
        self.source_name = source_name

    def to_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'duration_ms': self.duration_ms,
            'artwork_url': self.artwork_url,
            'source_url': self.source_url,
            'track_id': self.track_id,
            'source_name': self.source_name,
        }


class MusicSearchService:
    def __init__(self, timeout=15):
        self.timeout = timeout

    async def search(self, query: str):
        results = []
        results.extend(await self.search_itunes(query))
        results.extend(await self.search_musicbrainz(query))
        unique = []
        seen = set()
        for item in results:
            key = (item.title.lower(), item.artist.lower(), item.source_name)
            if key not in seen:
                unique.append(item)
                seen.add(key)
        return unique[:10]

    async def search_itunes(self, query: str):
        url = "https://itunes.apple.com/search"
        params = {"term": query, "media": "music", "entity": "song", "limit": 10}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, timeout=self.timeout) as response:
                    if response.status != 200:
                        return []
                    data = await response.json()
        except Exception:
            return []

        items = []
        for entry in data.get("results", []):
            track = MusicTrack(
                title=entry.get("trackName"),
                artist=entry.get("artistName"),
                album=entry.get("collectionName"),
                duration_ms=entry.get("trackTimeMillis"),
                artwork_url=entry.get("artworkUrl100") or entry.get("artworkUrl60"),
                source_url=entry.get("trackViewUrl") or entry.get("collectionViewUrl"),
                track_id=entry.get("trackId") or entry.get("collectionId") or entry.get("artistId"),
                source_name="iTunes",
            )
            items.append(track)
        return items

    async def search_musicbrainz(self, query: str):
        url = "https://musicbrainz.org/ws/2/recording"
        params = {"query": query, "fmt": "json", "limit": 5}
        headers = {"User-Agent": "MusicFinderBot/1.0 (contact@example.com)"}
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url, params=params, timeout=self.timeout) as response:
                    if response.status != 200:
                        return []
                    data = await response.json()
        except Exception:
            return []

        items = []
        for recording in data.get("recordings", []):
            artist_name = "غير متوفر"
            artist_credit = recording.get("artist-credit") or []
            if artist_credit:
                first = artist_credit[0]
                if isinstance(first, dict):
                    artist_name = first.get("name") or artist_name
            item = MusicTrack(
                title=recording.get("title"),
                artist=artist_name,
                album="غير متوفر",
                duration_ms=None,
                artwork_url=None,
                source_url="https://musicbrainz.org/recording/" + str(recording.get("id", "")),
                track_id=recording.get("id"),
                source_name="MusicBrainz",
            )
            items.append(item)
        return items
