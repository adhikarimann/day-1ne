import streamlit as st

st.title("DAY-1NE")
st.write("My first AI productivity app")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name} 🚀")

st.sidebar.header("DAY-1NE Menu")

study_hours = st.slider("How many hours will you study today?", 1, 12)

st.write(f"Planned study hours: {study_hours} hrs 📚")