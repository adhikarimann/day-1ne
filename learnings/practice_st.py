import streamlit as st

st.title("DAY-1NE Practice")

name = st.text_input("Enter your name")
subject = st.text_input("What are you studying today?")
hours = st.slider("How many hours will you study?", 1, 12)

if st.button("Submit"):

    st.write(f"Welcome {name}")
    st.write(f"Today's subject: {subject}")
    st.write(f"Planned study hours: {hours}")

    if hours >= 5:
        st.success("Strong study day 🔥")
    else:
        st.warning("Try increasing focus time 📚")