import streamlit as st

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

    submitted = st.form_submit_button("Generate Plan")

if submitted:

    st.session_state.exam = exam
    st.session_state.subjects = subjects
    st.session_state.hours = hours
    st.session_state.confidence = confidence

    st.success("Study profile saved successfully.")

    st.subheader("Your Study Profile")

    st.write(f"📘 Exam: {exam}")
    st.write(f"📚 Subjects: {subjects}")
    st.write(f"⏰ Hours/Day: {hours}")
    st.write(f"🎯 Confidence: {confidence}")