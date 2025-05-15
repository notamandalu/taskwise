import streamlit as st

st.set_page_config(page_title="Taskwise", layout="centered")

st.title("🧠 Taskwise")
st.subheader("Plan your day based on how your brain actually works.")

energy = st.radio("How is your energy right now?", ["Low", "Medium", "High"])
task_input = st.text_area("What do you need to get done today?")

if st.button("Generate Plan"):
    st.success("✨ Smart schedule generation coming soon!")
