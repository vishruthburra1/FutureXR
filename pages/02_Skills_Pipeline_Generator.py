import streamlit as st


from llm import skill_pipeline


# Page Configuration 
st.set_page_config(
    page_title="Skills Pipeline Generator",
    page_icon="🤖",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .skill-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5em;
        margin-bottom: 1.5em;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
    }
    .skill-tag {
        display: inline-block;
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 4px 12px;
        border-radius: 15px;
        margin: 3px;
        font-size: 0.85em;
    }
    .duty-item {
        margin: 5px 0;
        padding-left: 1.2em;
        position: relative;
    }
    .duty-item:before {
        content: "•";
        position: absolute;
        left: 0;
        color: #4CAF50;
    }
    .section-title {
        color: #2e7d32;
        margin-top: 1em;
        margin-bottom: 0.5em;
        font-weight: 600;
    }
    .header-section {
        background: linear-gradient(135deg, #4CAF50, #81C784);
        color: white;
        padding: 2em 1.5em;
        border-radius: 10px;
        margin-bottom: 2em;
    }
</style>
""", unsafe_allow_html=True)


# Login Check
if not st.user.is_logged_in:
    st.error("Login to view page", icon= "🚨")
    st.stop()


# Main header
st.markdown("""
<div class="header-section">
    <h1 style="color: white; margin: 0;">📊 Skills Pipeline Generator</h1>
    <p style="opacity: 0.9; margin: 0.5em 0 0 0;">
        Generate a detailed learning path for any job role. Enter a job title to get started.
    </p>
</div>
""", unsafe_allow_html=True)


with st.container():
    #Creating the Container
    job_title = st.text_input("Enter Job Title", placeholder="Machine learning engineer, UX Designer, ...etc")
    
    if st.button("View Skills", type="primary", use_container_width=True):
        if not job_title.strip():
            st.error("Please Enter Job Title", icon="🚨")
        else: 
            with st.spinner("Loading"):
                try:
                    skill_pipeline_result = skill_pipeline(job_title)
                    st.session_state.skill_dict = {}
                    for skill_needed in skill_pipeline_result.skills:
                        st.session_state.skill_dict[skill_needed.skill] = {
                            "description": skill_needed.description,
                            "skills": skill_needed.skills.split(",") if isinstance(skill_needed.skills, str) else skill_needed.skills,
                            "daily_duties": skill_needed.daily_duties.split(",") if isinstance(skill_needed.daily_duties, str) else skill_needed.daily_duties
                        }
                    st.session_state.generated = True
                    st.rerun()
                except Exception as e:
                    st.error("❌ An error occurred while generating the skills pipeline. Please try again.")
                    st.error(str(e))
                
# Display the skills pipeline if available
if st.session_state.get('generated') and st.session_state.get('skill_dict'):
    st.markdown(f"### 🎯 Skills Pipeline for: {job_title}")
    st.markdown("---")
    
    for i, (skill, details) in enumerate(st.session_state.skill_dict.items(), 1):
        with st.container():
            
            # Skill title with counter
            st.markdown(f"#### {i}. {skill}")
            
            # Description
            st.markdown("<div class='section-title'>📝 Description</div>", unsafe_allow_html=True)
            st.markdown(details["description"])
            
            # Skills
            if details["skills"]:
                st.markdown("<div class='section-title'>🔑 Key Skills</div>", unsafe_allow_html=True)
                cols = st.columns(3)
                for i, skill in enumerate(details["skills"][:6]):  # Show max 6 skills
                    if skill.strip():
                        with cols[i % 3]:
                            st.markdown(f"<span class='skill-tag'>{skill.strip()}</span>", unsafe_allow_html=True)
            
            # Daily Duties
            if details["daily_duties"]:
                st.markdown("<div class='section-title'>📋 Daily Duties</div>", unsafe_allow_html=True)
                for duty in details["daily_duties"]:
                    if duty.strip():
                        st.markdown(f"<div class='duty-item'>{duty.strip()}</div>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# More information in the sidebar
with st.sidebar:
    st.markdown("### ℹ️ How It Works")
    st.markdown("""
    1. Enter a job title in the search box
    2. Click 'Generate Skills Pipeline'
    3. Get a detailed breakdown of required skills
    4. Understand daily duties and responsibilities
    """)


    st.markdown("### 💡 Tips")
    st.markdown("""
    - Be Specific with the job title for better accuracy
    - Review the Skills you need and find the gaps in your skillset
    - Focus on 1-2 skills at a time and build them before moving to the rest
    - Use this as a learning Roadmap
    """)

if st.session_state.get("generated"):
    if st.button("🟥 Reset", use_container_width=True):
        st.session_state.generated = False
        st.session_state.skill_dict = None
        st.rerun()