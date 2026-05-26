import streamlit as st

st.set_page_config(
    page_title="DAY-1NE",
    page_icon="🚀",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("DAY-1NE")

page = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Study Planner", "Focus Tracker"]
)

# MAIN CONTENT
st.title("DAY-1NE Dashboard")

if page == "Home":
    st.subheader("Welcome Mann 👋")
    st.write("Start right. Stay consistent.")

elif page == "Study Planner":
    st.subheader("AI Study Planner 📚")
    st.write("Generate realistic study plans.")

elif page == "Focus Tracker":
    st.subheader("Focus Session Tracker ⏳")
    st.write("Track deep work sessions.")