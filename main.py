# from config.config import get_engine
from rich.traceback import install
from sqlalchemy import text

from config.config import get_engine

install()
engine = get_engine()
with engine.begin() as conn:
    stages = conn.execute(text("SELECT academic_stage FROM stress_level"))
    print(stages.fetchall())
