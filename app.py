import streamlit as st
import ollama

st.set_page_config(
    page_title="Nexus AI",
    layout="wide"
)

st.title("Nexus AI")
st.caption("Intelligent Conversational Assistant")

with st.sidebar:
    st.header("Nexus AI")
    st.write("Powered by Ollama and Python")

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = ollama.chat(
                model="gemma:2b",
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]

            st.write(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )