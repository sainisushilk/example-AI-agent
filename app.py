import streamlit as st
from langchain_core.messages import SystemMessage
from agent.graph import run_agent
from agent.prompts import SYSTEM_PROMPT

st.set_page_config(
    page_title="HR Leave Policy Agent",
    page_icon="🧾",
    layout="centered"
)

st.title("🧾 HR Leave Policy Agent")
st.caption("Ask about casual, sick, maternity, or paternity leave policies.")

# Session state for multi-turn memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = [SystemMessage(content=SYSTEM_PROMPT)]

# Show previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask a leave policy question..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer, new_history = run_agent(prompt, st.session_state.history)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                st.session_state.history = new_history
            except Exception as e:
                st.error(f"Error: {e}")