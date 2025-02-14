import streamlit as st
import requests

st.title("AI-Powered Social Scheduler")

# Schedule Post
st.subheader("Schedule a Post")
content = st.text_area("Enter Post Content")
scheduled_time = st.text_input("Enter Scheduled Time (YYYY-MM-DD HH:MM)")
if st.button("Schedule Post"):
    response = requests.post("http://127.0.0.1:8000/schedule/", json={"content": content, "scheduled_time": scheduled_time})
    st.success(response.json()["message"])

# Generate Caption
st.subheader("Generate Caption")
topic = st.text_input("Enter a Topic for Caption")
if st.button("Generate Caption"):
    response = requests.post("http://127.0.0.1:8000/generate_caption/", json={"topic": topic})
    st.write(response.json()["caption"])

# Generate Image
st.subheader("Generate Image")
prompt = st.text_input("Enter an Image Prompt")
if st.button("Generate Image"):
    response = requests.post("http://127.0.0.1:8000/generate_image/", json={"prompt": prompt})
    st.image(response.json()["image_url"])
