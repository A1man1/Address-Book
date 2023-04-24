from typing import Callable
from fastapi import FastAPI
from src.core.config import settings
from src.database.dbconnect import close_db_connection, connect_to_db


def create_start_app_handler(app: FastAPI) -> Callable:
    """Decorator to handle app startup event along with DB connection.

    Returns:
        start_app (DB connected App Object)
    """
    async def start_app() -> None:
        await connect_to_db(app)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    """Decorator to handle app shutdown event after closed DB connection.

    Returns:
        stop_app (DB disconnect App Object)
    """
    async def stop_app() -> None:
        await close_db_connection(app)
    return stop_app
