import plotly.express as px  # type:ignore
import streamlit as st

from source.query_runner import run_query

st.set_page_config(page_title="User Profile", layout="wide")

user_name = "Ali"
user_stage = "Sophomore"
user_email = "alimovmuhammadali01222008@gmail.com"

col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "https://ui-avatars.com/api/?name=Ali&size=200", caption=user_name, width=150
    )
    st.markdown(f"**🎓 Stage:** {user_stage}")
    st.markdown(f"**📧 Email:** {user_email}")

with col2:
    st.title(f"👤 {user_name}'s Profile Dashboard")

    df = run_query("undergraduate.sql")

    avg_stress = df["stress_index"].mean()
    fav_strategy = df["coping_strategy"].mode()[0]
    habits = df["bad_habits"].value_counts().idxmax()

    kpi1, kpi2 = st.columns(2)
    kpi1.metric("📊 Avg Stress", f"{avg_stress:.1f}")
    kpi2.metric("⚠️ Bad Habit", habits)

    st.write("🧘 Coping Strategy", fav_strategy)

    st.subheader("Stress Trend Over Time")
    if not df.empty:
        fig = px.line(
            df,
            x="timestamp",
            y="stress_index",
            title="Stress Index Over Time",
            template="plotly_white",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No records found for this user.")
