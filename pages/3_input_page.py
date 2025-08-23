import os
import sys

import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_action, run_query

install()

st.title("📝 Add New Stress Record")

with st.form("add_record"):
    date = st.date_input("Select date")
    d_time = st.time_input("Select time")
    timestamp = f"{date} {d_time}"
    st.write(timestamp)
    stage = st.selectbox(
        "Academic Stage", ["undergraduate", "high school", "post-graduate"]
    )
    peer_pressure = st.slider("Peer Pressure", 1, 5, 1)
    home_pressure = st.slider("Home Academic Pressure", 1, 5, 1)
    environment = st.selectbox("Study Environment", ["Noisy", "Peaceful", "disrupted"])
    coping = st.text_area("Coping Strategy")
    if not coping:
        coping == "Unknown"
    bad_habits = st.selectbox("Bad Habits", ["Yes", "No", "Prefer not to say"])
    competition = st.slider("Academic Competition", 1, 5, 1)
    stress_index = st.slider("Stress Index", 1, 5, 1)

    submitted = st.form_submit_button("Submit")

if submitted:
    params = {
        "timestamp": timestamp,
        "academic_stage": stage,
        "peer_pressure": peer_pressure,
        "home_academic_pressure": home_pressure,
        "study_environment": environment,
        "coping_strategy": coping,
        "bad_habits": bad_habits,
        "academic_competition": competition,
        "stress_index": stress_index,
    }
    run_action("insert_record.sql", params)
    st.success("✅ Record inserted successfully!")
