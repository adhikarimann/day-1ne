import streamlit as st

from utils.ai_helper import generate_study_plan

st.set_page_config(
    page_title="Planner",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Study Planner")

with st.form("planner_form"):

    exam = st.text_input("Exam Name")

    subjects = st.multiselect(
        "Select Subjects",
        ["Physics", "Chemistry", "Maths", "DSA"]
    )

    hours = st.slider(
        "Study Hours Per Day",
        1,
        12,
        4
    )

    confidence = st.selectbox(
        "Confidence Level",
        ["Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Generate AI Plan")

if submitted:

    with st.spinner("Generating realistic study strategy..."):

        ai_response = generate_study_plan(
            exam,
            subjects,
            hours,
            confidence
        )

    st.success("AI Study Plan Generated")

    st.subheader("📘 Your AI Guidance")

    st.write(ai_response)