import streamlit as st

st.set_page_config(page_title="Columns Demo")

st.title("🎨 Streamlit Columns Practice")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.button("Click Me 1")

with col2:
    st.header("Column 2")
    st.text_input("Enter text")

with col3:
    st.header("Column 3")
    st.slider("Pick a number", 1, 10)
