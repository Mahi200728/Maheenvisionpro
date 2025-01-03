from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Google API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Foto")

st.header("Foto Powered by Gemini")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

# Button variables
tell_me_button = st.button("Tell me about the image")
historical_context_button = st.button("What is the historical context")
brief_summary_button = st.button("Give me a brief summary")
similar_looking_button = st.button("Pull up similar looking pictures")

# Button logic
if tell_me_button:
    response = get_gemini_response(input_prompt, image)
    st.subheader("The Response is")
    st.write(response)

if historical_context_button:
    response = get_gemini_response("What is the historical context of this image?", image)
    st.subheader("The Response is")
    st.write(response)

if brief_summary_button:
    response = get_gemini_response("Give me a brief summary of this image.", image)
    st.subheader("The Response is")
    st.write(response)

if similar_looking_button:
    response = get_gemini_response("Show me similar looking pictures.", image)
    st.subheader("The Response is")
    st.write(response)
