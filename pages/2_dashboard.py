import os
import sys

import plotly.express as px  # type:ignore
import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_query

install()

st.set_page_config(page_title="Stress Dashboard", page_icon="📊", layout="wide")

st.title("📊 Academic Stress Dashboard")
st.markdown("Explore patterns and insights from student stress data.")

df_stage = run_query("avg_stress_by_stage.sql")
fig_stage = px.bar(
    df_stage,
    x="academic_stage",
    y="avg_stress",
    color="avg_stress",
    title="Average Stress Index by Academic Stage",
)
st.plotly_chart(fig_stage, use_container_width=True)

df_dist = run_query("distribution_stress_index.sql")
fig_dist = px.bar(
    df_dist, x="stress_index", y="count", title="distribution of tress Index Ratings"
)
st.plotly_chart(fig_dist, use_container_width=True)

df_pressure = run_query("stress_vs_pressure.sql")
fig_scatter = px.scatter(
    df_pressure,
    x="peer_pressure",
    y="home_academic_pressure",
    size="stress_index",
    color="stress_index",
    title="Peer Pressure vs Home Academic Pressure vs Stress Index",
)
st.plotly_chart(fig_scatter, use_container_width=True)

df_coping = run_query("coping_strategy_counts.sql")
fig_coping = px.pie(
    df_coping,
    values="count",
    names="coping_strategy",
    title="Coping Strategies Distribution",
)
st.plotly_chart(fig_coping, use_container_width=True)

df_habits = run_query("bad_habits_comparison.sql")
fig_habits = px.bar(
    df_habits,
    x="bad_habits",
    y="avg_stress",
    color="bad_habits",
    title="Average Stress Index by Bad Habits",
)
st.plotly_chart(fig_habits, use_container_width=True)
