from .db import init_db, get_connection, add_search_history, get_search_history, delete_search_history, add_favorite, get_favorites, upsert_user, stats_search_count, stats_users_count

__all__ = [
    "init_db",
    "get_connection",
    "add_search_history",
    "get_search_history",
    "delete_search_history",
    "add_favorite",
    "get_favorites",
    "upsert_user",
    "stats_search_count",
    "stats_users_count",
]
