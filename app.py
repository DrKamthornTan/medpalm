import streamlit as st
from streamlit_chat import message
import google.generativeai as palm

st.title("DHV AI Startup Med-PaLM2 Demo")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        key="user_prompt",  # Added key for proper form behavior
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)

    for msg in st.session_state["messages"]:  # Added missing square brackets for accessing the "messages" key
        message(msg["content"], is_user=msg["role"] == "user")  # display message on the screen

palm_api_key = ""

if user_prompt and palm_api_key:

    palm.configure(api_key=palm_api_key)  # set API key

    st.session_state["messages"].append({"role": "user", "content": user_prompt})  # Added missing square brackets for appending to "messages"

    message(user_prompt, is_user=True)

    response = palm.chat(messages=[user_prompt])  # get response from Google's PaLM API

    msg = {"role": "assistant", "content": response.last}  # we are using dictionary to store message and its role. It will be useful later when we want to display chat history on the screen, to show user input at the left and AI's right side of the screen.

    st.session_state["messages"].append(msg)  # add message to the chat history

    message(msg["content"])  # display message on the screen

def clear_chat():
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]  # Added missing square brackets for resetting "messages"

if len(st.session_state["messages"]) > 1:  # Added missing square brackets for accessing the "messages" key
    st.button('Clear Chat', on_click=clear_chat)