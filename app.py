import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="DAY-1NE",
    page_icon="🚀",
    layout="wide"
)

# HEADER
st.title("🚀 DAY-1NE")
st.caption("Start right. Stay consistent.")

st.divider()

# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "home"

# HOME PAGE
if st.session_state.page == "home":

    st.subheader("Choose Your Space")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ⏳ Focus")
        st.write("Deep work sessions without noise.")

        if st.button("Open Focus"):
            st.session_state.page = "focus"

    with col2:
        st.markdown("### 📚 Planner")
        st.write("Turn remaining days into a realistic plan.")

        if st.button("Open Planner"):
            st.session_state.page = "planner"

    with col3:
        st.markdown("### 📈 Dashboard")
        st.write("Track consistency and study hours.")

        if st.button("Open Dashboard"):
            st.session_state.page = "dashboard"

# FOCUS PAGE
elif st.session_state.page == "focus":

    st.subheader("⏳ Focus Session")

    subject = st.text_input("What are you studying?")

    hours = st.slider("Focus Duration", 1, 5)

    if st.button("Start Session"):
        st.success(f"{hours} hr focus session started for {subject} 🚀")

    if st.button("← Back Home"):
        st.session_state.page = "home"

# PLANNER PAGE
elif st.session_state.page == "planner":

    st.subheader("📚 Study Planner")

    days = st.slider("Days left for exam", 1, 60)

    st.info(f"You still have {days} days remaining.")

    if st.button("← Back Home"):
        st.session_state.page = "home"

# DASHBOARD PAGE
elif st.session_state.page == "dashboard":

    st.subheader("📈 Daily Dashboard")

    name = st.text_input("Enter your name")

    study_hours = st.slider(
        "How many hours will you study today?",
        1,
        12
    )

    if st.button("Save Progress"):

        st.success(f"Welcome {name} 🔥")

        st.write(f"Planned Study Hours: {study_hours}")

        if study_hours >= 5:
            st.success("Strong study day ahead 🚀")
        else:
            st.warning("Try increasing focus time 📚")

    if st.button("← Back Home"):
        st.session_state.page = "home"