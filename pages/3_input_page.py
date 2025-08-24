import os
import sys

import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_action, run_query

install()

st.title("📝 Add New Stress Record")

col1, col2 = st.columns(2)


with col1:
    academic_stage = st.selectbox(
        "Academic Stage", ["Undergraduate", "Post-graduate", "High school"]
    )
    stress_index = st.slider("Stress Index", 1, 5, 5)
    peer_pressure = st.slider("Peer Pressure (1-5)", 1, 5, 5)
    home_pressure = st.slider("Home Academic Pressure (1-5)", 1, 5, 5)


with col2:
    competition = st.slider("Academic Competition (1-5)", 1, 5, 5)
    coping_strategy = st.selectbox(
        "Coping Strategy",
        [
            "Emotional breakdown (crying a lot)",
            "Social support (friends, family)",
            "Analyze the situation and handle it with intellect",
        ],
    )
    bad_habits = st.selectbox("Bad Habits", ["Yes", "No", "Prefer not to say"])
    study_env = st.selectbox("Study Environment", ["Disrupted", "Noisy", "Peaceful"])

date = st.date_input("Select date")
d_time = st.time_input("Select time")
timestamp = f"{date} {d_time}"

if st.button("Submit Record", type="primary"):
    params = {
        "timestamp": timestamp,
        "academic_stage": academic_stage,
        "peer_pressure": peer_pressure,
        "home_academic_pressure": home_pressure,
        "study_environment": study_env,
        "coping_strategy": coping_strategy,
        "bad_habits": bad_habits,
        "academic_competition": competition,
        "stress_index": stress_index,
    }
    run_action(
        "insert_record.sql",
    )
    st.success("✅ Record successfully added to the database!")
