from services.music_search import MusicSearchService


def test_music_service_instantiation():
    service = MusicSearchService(timeout=5)
    assert service.timeout == 5
