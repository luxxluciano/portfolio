import streamlit as st

# Page header
st.title("My Portfolio")

# Main area
st.write("""
    Hi there! Welcome to my portfolio. I'm a software engineer with a passion for building innovative solutions 
    that solve real-world problems. Here are some of my recent projects:
""")

# Project gallery with embedded YouTube videos
col1, col2, col3, col4 = st.beta_columns(4)
with col1:
    st.video("https://youtu.be/3J7-0ZbHIic")
with col2:
    st.video("https://youtu.be/R9PhxG3XsJ0")
with col3:
    st.video("https://youtu.be/SDRqJIHOSMk")
with col4:
    st.video("https://youtu.be/O4OWpJsPmXc")

# Footer
st.write("""
    © 2023 My Portfolio. All rights reserved.
""")
