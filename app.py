import streamlit as st

# Page header
st.title("My Portfolio")

# Main area
st.write("""
    Hi there! Welcome to my portfolio. I'm a software engineer with a passion for building innovative solutions 
    that solve real-world problems. Here are some of my recent projects:
""")

# Project gallery with embedded YouTube videos
st.video("https://youtu.be/3J7-0ZbHIic")
st.video("https://youtu.be/R9PhxG3XsJ0")
st.video("https://youtu.be/SDRqJIHOSMk")
st.video("https://youtu.be/O4OWpJsPmXc")

# Contact form
st.write("""
    If you'd like to get in touch with me, please fill out the form below and I'll get back to you as soon as possible:
""")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
    st.success("Thanks for your message! I'll be in touch soon.")
