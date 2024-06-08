from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """Base config"""

    environment: str
    db_uri: str
    super_email: str
    super_password: str
    access_token_expires_in_minutes: str
    secret_key: str
    jwt_algorithm: str
    openai_api_key: str
    secure_token: str

    class Config:
        """Config class"""

        env_file = ".env"
        _env_file_encoding = "utf-8"


class ProductionSettings(BaseConfig):
    """production settings"""

    db_uri: str


class DevelopmentSettings(BaseConfig):
    """development settings"""

    db_uri: str


class TestSettings(BaseConfig):
    """test settings"""

    db_uri: str = Field(alias="TEST_DB_URI")


@lru_cache
def get_settings():
    """Get settings"""
    configs = {
        "production": ProductionSettings,
        "development": DevelopmentSettings,
        "testing": TestSettings,
    }
    environment = BaseConfig().environment

    return configs[environment]()


settings = get_settings()
