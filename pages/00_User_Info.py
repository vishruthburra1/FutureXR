import streamlit as st


# Page Configuration
st.set_page_config(
    page_title="FutureFrameXR- Find Your Career",
    page_icon="🤖",
    layout="centered")

if not st.user.is_logged_in:
    st.error("Please Login", icon= "‼️")
    st.stop()