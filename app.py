# from config.config import get_engine
import numpy as np
import pandas as pd
import streamlit as st
from rich.traceback import install
from sqlalchemy import text

from config.config import get_engine

install()
engine = get_engine()
with engine.begin() as conn:
    stages = conn.execute(text("SELECT academic_stage FROM stress_level"))
