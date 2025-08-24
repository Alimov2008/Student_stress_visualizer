import os
import sys

import pandas as pd
import plotly.express as px  # type:ignore
import plotly.figure_factory as ff  # type:ignore
import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_query

install()

st.set_page_config(page_title="Stress Dashboard", page_icon="📊", layout="wide")

df = run_query("get_all.sql")


st.title("📊 Academic Stress Analysis Dashboard")
st.markdown(
    "Explore stress patterns, coping strategies, and academic environment influences."
)


avg_stress = df["stress_index"].mean()
common_strategy = df["coping_strategy"].mode()[0]
high_stress_cases = df[df["stress_index"] > 7].shape[0]


col1, col2, col3 = st.columns(3)
col1.metric("Average Stress", f"{avg_stress:.1f}")
col2.metric("Most Common Coping Strategy", common_strategy)
col3.metric("High Stress Cases", high_stress_cases)


# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
stages = df["academic_stage"].unique()
stage_filter = st.sidebar.selectbox("Select Academic Stage", ["All"] + list(stages))


if stage_filter != "All":
    df = df[df["academic_stage"] == stage_filter]


tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Overview", "📈 Trends", "🧠 Coping & Habits", "🔥 Correlations"]
)


with tab1:
    st.subheader("Stress Levels by Academic Stage")
    df_stage = df.groupby("academic_stage", as_index=False)["stress_index"].mean()
    fig_stage = px.bar(
        df_stage,
        x="academic_stage",
        y="stress_index",
        color="stress_index",
        title="Average Stress Index by Stage",
        template="plotly_white",
    )
    st.plotly_chart(fig_stage, use_container_width=True)

    st.subheader("Stress Level Distribution")
    df_dist = df["stress_index"].value_counts().reset_index()
    df_dist.columns = ["stress_index", "count"]  # type:ignore
    fig_dist = px.pie(
        df_dist,
        names="stress_index",
        values="count",
        hole=0.4,
        title="Stress Level Distribution",
        template="plotly_white",
    )
    st.plotly_chart(fig_dist, use_container_width=True)


# Tab 2: Trends
with tab2:
    st.subheader("Stress Trend Over Time")
    df_time = df.groupby("timestamp", as_index=False)["stress_index"].mean()
    fig_line = px.line(
        df_time,
        x="timestamp",
        y="stress_index",
        title="Stress Index Over Time",
        template="plotly_white",
    )
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("Peer Pressure vs Stress Index")
    fig_scatter = px.scatter(
        df,
        x="peer_pressure",
        y="stress_index",
        color="academic_stage",
        size="stress_index",
        hover_data=["study_environment"],
        title="Peer Pressure Impact on Stress",
        template="plotly_white",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


# Tab 3: Coping Strategies & Habits
with tab3:
    st.subheader("Coping Strategies Distribution")
    df_coping = df["coping_strategy"].value_counts().reset_index()
    df_coping.columns = ["coping_strategy", "count"]  # type:ignore
    fig_coping = px.bar(
        df_coping,
        x="coping_strategy",
        y="count",
        color="count",
        title="Most Common Coping Strategies",
        template="plotly_white",
    )
    st.plotly_chart(fig_coping, use_container_width=True)

    st.subheader("Habits Distribution")
    df_habits = df["bad_habits"].value_counts().reset_index()
    df_habits.columns = ["bad_habits", "count"]  # type:ignore
    fig_habits = px.pie(
        df_habits,
        names="bad_habits",
        values="count",
        hole=0.3,
        title="Daily Habits Impact",
        template="plotly_white",
    )
    st.plotly_chart(fig_habits, use_container_width=True)


# Tab 4: Correlation Heatmap
with tab4:
    st.subheader("Correlation Heatmap of Factors")
    corr = df[
        [
            "peer_pressure",
            "home_academic_pressure",
            "academic_competition",
            "stress_index",
        ]
    ].corr()
    fig_heat = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.round(2).values,
        colorscale="Viridis",
        showscale=True,
    )
    st.plotly_chart(fig_heat, use_container_width=True)
