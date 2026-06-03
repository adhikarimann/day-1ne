import streamlit as st

st.set_page_config(
    page_title="DAY-1NE",
    page_icon="🧠",
    layout="wide"
)

st.title("DAY-1NE")

st.markdown("""
### A Calm Academic Operating System

Built for students who feel overwhelmed by chaos,
fake productivity, and unrealistic planning.

DAY-1NE focuses on:
- clarity over confusion
- realistic execution
- intelligent prioritization
- calm systems
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Go to Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

with col2:
    if st.button("🧠 Go to Planner", use_container_width=True):
        st.switch_page("pages/Planner.py")

with col3:
    if st.button("⚡ Go to Reality Checker", use_container_width=True):
        st.switch_page("pages/Reality_Checker.py")

st.divider()

st.subheader("🚀 Current Features")

st.info("""
🧠 AI-Powered Study Planner

📚 Dynamic Subject Management

🎯 Realistic Academic Strategies

⚡ Academic Reality Assessment

🔄 Continuous Improvements
""")

st.caption("Built with ❤️ & a bit of 🐍 & Streamlit!")