from fastapi import FastAPI
import sqlalchemy
from src.database.dbconfig import db, metadata, URL_DB
from src.core.config import log


async def connect_to_db(app: FastAPI) -> None:
    """Function to create a database connection for current app.

    Args:
        app (FastAPI App)

    Raises:
        Exception: DB CONNECTION ERROR.

    Returns:
        None (Opens DB Connection)
    """
    try:
        log.info("connecting to a database")
        if not db.is_connected:
            await db.connect()
        engine = sqlalchemy.create_engine(str(URL_DB))
        metadata.create_all(engine)

        app.state._db = db
        log.info("Database connection - successful")
    except Exception as e:
        log.warn("--- DB CONNECTION ERROR ---")
        log.warn(e)
        log.warn("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    """Function to close a database connection for current app.

    Args:
        app (FastAPI App)

    Raises:
        Exception: DB DISCONNECT ERROR.

    Returns:
        None (Close DB Connection)
    """

    try:
        log.info("Closing connection to database")
        if app.state._db.is_connected:
            await app.state._db.disconnect()
        log.info("Database connection - closed")
    except Exception as e:
        log.warn("--- DB DISCONNECT ERROR ---")
        log.warn(e)
        log.warn("--- DB DISCONNECT ERROR ---")
