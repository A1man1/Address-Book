from functools import lru_cache
from typing import Optional
from databases import DatabaseURL
from pydantic import BaseSettings, EmailStr
from starlette.config import Config

config = Config(".env")


class Settings(BaseSettings):
    """System Settings file for app configuration.

    Args:
        BaseSettings (object): Abstract base settings.
    """

    # project declaratives.
    project_name: str = config(
        "PROJECT_NAME", cast=str, default="Folksmedia Reviews Service")
    version: str = config("VERSION", cast=str, default="1.0.0")
    app_domain: str = config("APP_DOMAIN", cast=str, default="localhost")
    app_port: str = config("APP_PORT", cast=str, default="8000")
    api_prefix: str = config("API_PREFIX", cast=str, default="/api")
    docs_prefix: str = config("DOCS_PREFIX", cast=str, default="/docs")
    admin_email: EmailStr = config(
        "APP_ADMIN_EMAIL", cast=EmailStr, default="admin@example.com")
    root_url: str = config("ROOT_URL", cast=str,
                           default=f"http://{ app_domain }:{ app_port }")
    
    minimum_compression_limit: int = config(
        "MIN_COMPRESSION", cast=int, default=200)

    # app settings.
    allowed_hosts: str = config("ALLOWED_HOSTS", cast=str, default="*")
    environment: str = config("ENVIRONMENT", cast=str, default="DEV")
    default_page_limit: int = config(
        "DEFAULT_PAGE_LIMIT", cast=int, default=50)
    
    debug: bool = False
    testing: bool = False
    
    # postgres settings
    database_url: DatabaseURL = config(
        "DATABASE_URL", cast=DatabaseURL,
        default=f"sqlite:///sql.db")

    db_pool_min_size_postgers: int = config(
        "DB_POOL_MIN_SIZE", cast=int, default=2)
    db_pool_max_size_postgers: int = config(
        "DB_POOL_MAX_SIZE", cast=int, default=15)
    db_force_roll_back_postgers: bool = False


class ProdSettings(Settings):
    debug: bool = False


class DevSettings(Settings):
    debug: bool = True


class TestSettings(Settings):
    debug: bool = True
    testing: bool = True
    db_force_rollback: bool = True


class FactoryConfig:
    """
    Returns a config instance depends on the ENV_STATE variable.
    """

    def __init__(self, environment: Optional[str] = "DEV"):
        self.environment = environment

    def __call__(self):
        if self.environment == "PROD":
            return ProdSettings()
        elif self.environment == "TEST":
            return TestSettings()
        return DevSettings()


@lru_cache()
def get_app_settings():
    return FactoryConfig(Settings().environment)()
