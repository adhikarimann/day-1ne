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


if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase Counter"):
    st.session_state.count += 1

st.write("Counter:", st.session_state.count)


with st.form("revision_form"):

    confidence = st.slider(
        "Confidence Level",
        1,
        10,
        5
    )

    submitted = st.form_submit_button(
        "Generate Summary"
    )

if submitted:

    st.success("Summary Generated!")

    st.write(f"👤 Name: {name}")
    st.write(f"🎯 Exam: {exam}")
    st.write(f"⏰ Study Hours: {hours}")
    st.write(f"🔥 Confidence: {confidence}/10")