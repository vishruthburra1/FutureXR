import streamlit as st
import authlib



# Page Configuration
st.set_page_config(
    page_title="FutureFrameXR- Find Your Career",
    page_icon="🤖",
    layout="centered")


# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subheader {
        font-size: 1.2em;
        color: #424242;
        text-align: center;
        margin-bottom: 2em;
    }
    .feature-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5em;
        margin-bottom: 1em;
        border-left: 4px solid #1E88E5;
    }
    .feature-title {
        font-weight: 600;
        color: #1E88E5;
        margin-bottom: 0.5em;
    }
</style>
""", unsafe_allow_html=True)


# header section
st.markdown('<h1 class="main-title">FutureFrameXR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Find Your Career</p>', unsafe_allow_html=True)


# Main part
col1, col2 = st.columns([1.2, 1])


with col1:
    st.markdown("""
    ### Why Future Frame XR?
    FutureFrameXR is a virtual Simulation Tool for experiencing new Jobs. 
                
    ### How it Works?
    1. Share your Academic Background and Interests
    2. 
    """)

with col2:
    with st.container(border=True):
        st.markdown("### Get Started")
        if not st.user.is_logged_in:
            if st.button("🔑 Log in / Sign up", use_container_width=True, type="primary"):
                st.login()
        else:
            st.success(f"Welcome back, {st.user.name}!")
            if st.button("🚪 Log out", use_container_width=True):
                st.logout()


# Features Section
st.markdown('---')
st.markdown("### 🚀 Features That Help You Succeed")

col1, col2= st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">📊 Career Matching</div>', unsafe_allow_html=True)
        st.markdown('Discover careers that align with your studies and interests')
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown('<div class="feature-title">📊 Skill Roadmap</div>', unsafe_allow_html=True)
        st.markdown('Find Skills relevant to your job')
        st.markdown('</div>', unsafe_allow_html=True)


# Call to Action 
st.markdown("---")
st.markdown("### Ready to discover your future career path?")
if st.button("Get Started Now", type="primary"):
    if not st.user.is_logged_in:
        st.login()
    else:
        st.success("Go to the Next Page")
        #st.switch_page("pages/00_User_Info.py")