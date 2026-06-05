import streamlit as st

st.title("📚 Streamlit Revision - Day 5")

name = st.text_input("Enter Your Name")

exam = st.selectbox(
    "Select Exam",
    ["JEE", "NEET", "Semester"]
)

hours = st.slider(
    "Study Hours Per Day",
    1,
    12,
    4
)
