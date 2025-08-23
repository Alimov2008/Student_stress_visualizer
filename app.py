# from config.config import get_engine
import numpy as np
import pandas as pd
import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_query

install()

st.title("📊 Academic Stress Data Explorer")

st.header("Stress Levels by Academic Stage")
df_stage = run_query("avg_stress_by_stage.sql")
st.dataframe(df_stage)

st.header("Stress vs Study Environment")
df_env = run_query("avg_stress_by_environment.sql")
st.bar_chart(df_env.set_index("study_environment")["avg_stress"])

st.header("Stress Distribution")
df_dist = run_query("stress_distribution.sql")
st.bar_chart(df_dist.set_index("stress_index")["student_count"])
