from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(user_input):
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    return response.text

st.markdown(
    """
    <h1 style='text-align: center; color: #2E8B57;'>🤖 GimiBot</h1>
    <p style='text-align: center; color: #ffff;'>Ask anything and get instant answers!</p>
    """,
    unsafe_allow_html=True
)
st.write("Ask anything.")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submitted = st.form_submit_button("Send")
    if submitted:
        if user_input.strip():
            response = get_gemini_response(user_input)
            st.markdown(f"**gimibot:** {response}")
        else:
            st.warning("Please enter a message.")

