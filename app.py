import streamlit as st

st.title("DAY-1NE")
st.write("My first AI productivity app")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name} 🚀")

st.sidebar.header("DAY-1NE Menu")