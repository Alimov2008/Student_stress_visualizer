import os
import pathlib
import sys

import pandas as pd
from sqlalchemy import text

sys.path.append(
    os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config")
    )
)
from config.config import get_engine

BASE_QUERY_PATH = os.path.join(os.path.dirname(__file__), "..", "queries")


def load_sql(filename: str) -> str:
    filepath = os.path.join(BASE_QUERY_PATH, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def run_query(filename: str, params: dict = None) -> pd.DataFrame:  # type:ignore
    sql = load_sql(filename)
    with get_engine().connect() as conn:
        result = pd.read_sql(text(sql), conn, params=params)
    return result
