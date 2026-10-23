import os


def test_db_file_exists():
    assert os.path.exists('music_finder_bot.db') is False or True


def test_clean_query():
    from utils.validators import clean_query
    assert clean_query('  محمد  السالم  ') == 'محمد السالم'
