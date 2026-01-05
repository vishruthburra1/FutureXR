import streamlit as st
import os 

# # Load environment variables from secrets
# os.environ["AWS_ACCESS_KEY_ID"] = st.secrets["aws"]["AWS_ACCESS_KEY"]
# os.environ["AWS_SECRET_ACCESS_KEY"] = st.secrets["aws"]["AWS_SECRET_KEY"]
# os.environ["AWS_REGION"] = st.secrets["aws"]["REGION_NAME"]
# os.environ["ENV"] = st.secrets["aws"]["ENV"]

# # dynamodb table name
# TABLE_NAME = os.getenv("ENV") + "_user_info"



# check if user info is in session state
if "user_info" not in st.session_state:
    st.session_state.user_info = {}


# Page Configuration
st.set_page_config(
    page_title="FutureFrameXR- Find Your Career",
    page_icon="🤖",
    layout="centered")

if not st.user.is_logged_in:
    st.error("Please Login", icon= "‼️")
    st.stop()


st.title("👤 Your Profile")
st.markdown("Tell us about yourself to get personalized career recommendations.")

# User Information Form
with st.form("user_info_form"):
    st.markdown("### Basic Information")
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("First Name", placeholder="John")
    with col2:
        last_name = st.text_input("Last Name", placeholder="Doe")
    
    email = st.text_input("Email", placeholder="john.doe@example.com")
    
    st.markdown("### Academic Information")
    education_level = st.selectbox(
        "Current Education Level",
        ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD", "Other"]
    )
    
    field_of_study = st.text_input("Field of Study/Major", placeholder="e.g., Computer Science, Business, etc.")
    
    st.markdown("### Career Interests")
    interests = st.multiselect(
        "Select your areas of interest (select up to 3)",
        ["Technology", "Business", "Healthcare", "Arts & Design", "Engineering", 
         "Education", "Science & Research", "Marketing", "Finance", "Other"],
        max_selections=5
    )

    skills = st.text_area("Current Skills (comma-separated)", 
                         placeholder="e.g., Python, Data Analysis, Project Management, etc.")
    
    career_goals = st.text_area("What are your career goals? (Optional)", 
                               placeholder="Where do you see yourself in 5 years?")
    
    submitted = st.form_submit_button("Save Profile")

    if submitted:
        if not all([first_name, last_name, email, education_level, field_of_study, interests]):
            st.error("Please fill in all required fields.")
        else:
            # Here you would typically save this information to a database
            st.session_state.user_info = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "education_level": education_level,
                "field_of_study": field_of_study,
                "interests": ", ".join(interests),
                "skills": ", ".join([s.strip() for s in skills.split(",") if s.strip()]),
                "career_goals": career_goals
            }

        # redirect to another page after saving
        st.switch_page("pages/01_Career_Recommendations.py")