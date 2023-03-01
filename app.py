import streamlit as st

# Page header
st.title("Luciano Martins Fagundes")

# Main area
st.write("""
    	As an IT support analyst, I have a strong foundation in troubleshooting and problem-solving, 
        with experience in both technical and customer service roles. I am highly skilled in
        using various tools and technologies to diagnose and resolve a wide range of technical issues, 
        and I am committed to providing top-quality support to clients and colleagues. 
        With my strong communication skills and ability to work effectively in a team, 
        I am confident in my ability to contribute to the success of any organization. 
        In addition to my technical skills, I have proven experience in team management and leadership, 
        and am comfortable working in fast-paced and dynamic environments. 
        I am committed to staying current with the latest trends and technologies in the field, and 
        to consistently delivering high-quality work. 
        Here are some of my recent projects:
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
