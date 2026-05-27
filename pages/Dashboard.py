import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

st.markdown("""
Welcome back.

Clarity over chaos.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Focus Hours", "4.5 hrs")

with col2:
    st.metric("Tasks Completed", "3")

with col3:
    st.metric("Burnout Risk", "Low")

st.divider()

st.subheader("Today's Priority")

st.info("Complete Binary Search + revise Chemical Bonding.")