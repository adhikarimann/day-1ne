import streamlit as st
import random

st.set_page_config(page_title="Emoji Generator")

st.title("🎲 Random Emoji Generator")

if "emoji" not in st.session_state:
    st.session_state.emoji = "🙂"

if st.button("Generate New Emoji"):
    emojis = ["😀","😎","🤖","🐱","🚀","🍕","⚡","🎶","🔥","🌈"]
    st.session_state.emoji = random.choice(emojis)

st.markdown(f"### Your Emoji: {st.session_state.emoji}")
