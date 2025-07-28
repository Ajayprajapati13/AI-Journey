'''#Python
import streamlit as st
import openai
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
# Set OpenAI API key
client = openai.Client()
client.api_key = os.getenv("OpenAI_Api_Key")

st.title("AI Chatbot with GPT")
user_input = st.text_input("Hello Ajay:", "")
if user_input:
    response = client.chat.completions.create(
  model="gpt-4o-mini", #or "gpt-4" if you have access
  messages=[{"role": "user", "content": user_input}]
    )
    reply = response['choices'][0]['message']['content']
    st.text_area("bot:", reply, height=200) '''
    
# app.py

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit app title
st.title("AI Chatbot with GPT")

# User input
user_input = st.text_input("Hello Ajay:")

# If there's user input, get response from OpenAI
if user_input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    # Display the assistant's reply
    st.write(response.choices[0].message.content)
