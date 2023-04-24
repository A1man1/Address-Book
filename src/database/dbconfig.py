import sqlalchemy
from databases import Database
from starlette.requests import Request
from sqlalchemy.ext.declarative import declarative_base

from src.core.config import settings

def get_database(request: Request) -> Database:
    """Get current database from app state.

    Args:
        request (Request): HTTP Request object through API.

    Returns:
        Database: Apps database.
    """
    return request.app.state._db


def get_db() -> Database:
    """Configure database for the application.

    Returns:
        Database: Current DB for the application.
    """
    options = {
        "min_size": settings.db_pool_min_size_postgers,
        "max_size": settings.db_pool_max_size_postgers,
        "force_rollback": settings.db_force_roll_back_postgers,
    }
    return Database(settings.database_url, **options)


URL_DB = str(settings.database_url)
db: Database = get_db()
Base = declarative_base()
metadata = sqlalchemy.MetaData()
