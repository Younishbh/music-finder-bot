from config import ADMIN_ID, BOT_TOKEN


def test_config_values():
    assert isinstance(ADMIN_ID, int)
    assert isinstance(BOT_TOKEN, str)
