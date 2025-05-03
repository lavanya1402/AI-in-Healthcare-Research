import streamlit as st
from app import crew

st.title("🧠 AI in Healthcare Research")
topic = st.text_input("Enter a healthcare topic", "AI in Healthcare")

if st.button("Run Research Agents"):
    result = crew.kickoff(inputs={"topic": topic})
    st.markdown(result)
