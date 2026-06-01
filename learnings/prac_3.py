import streamlit as st

st.set_page_config(page_title="Practice App")

st.title("🚀 My First Streamlit App")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 1, 100)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")

st.write("This is a practice app.")
st.write("Try changing the inputs above.")
st.write("Streamlit updates instantly when you interact.")
st.caption("End of demo 🎉")
