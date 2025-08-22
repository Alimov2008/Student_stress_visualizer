import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")

    @staticmethod
    def get_db_url() -> str:
        return (
            f"postgresql://{Config.DB_USER}:{Config.DB_PASS}"
            f"@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
        )


def get_engine(echo: bool = False):
    return create_engine(
        Config.get_db_url(),
        echo=echo,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
    )
