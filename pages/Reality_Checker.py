import streamlit as st

st.set_page_config(
    page_title="Reality Checker",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Reality Checker")

syllabus = st.slider(
    "Syllabus Remaining (%)",
    0,
    100,
    50
)

days = st.number_input(
    "Days Left",
    1,
    365,
    30
)

hours = st.slider(
    "Available Study Hours",
    1,
    15,
    5
)

if st.button("Analyze Reality"):

    if syllabus > 70 and days < 30:
        st.error("""
        Completing everything thoroughly may be unrealistic.

        Prioritize high-weightage topics and PYQs.
        """)

    elif syllabus < 40:
        st.success("""
        You are in a manageable position.

        Focus on consistency and revision.
        """)

    else:
        st.warning("""
        Situation is moderate.

        Structured planning is necessary now.
        """)