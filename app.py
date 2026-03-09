import streamlit as st
import pandas as pd

st.set_page_config(page_title="V.Sai Kiran Portfolio", layout="wide")

st.title("V. SAI KIRAN - Data Analyst & AI Developer")
st.write("Welcome to my project dashboard built with Streamlit.")

page = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Projects", "Contact"]
)

# HOME PAGE
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("Here you can explore my AI and Data Analytics projects.")

# PROJECTS PAGE
elif page == "Projects":
    st.title("🚀 My Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 AI Data Analyst System")
        st.write("Automates data analysis and predictions.")

    with col2:
        st.subheader("🎥 AI Security Camera")
        st.write("Detects suspicious activity using YOLOv8.")

    st.image("security_camera_project.png", caption="AI Surveillance System")

    data = {
        "Project": ["AI System", "Security Camera", "SQL Projects"],
        "Completion": [80, 70, 90]
    }

    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Project"))

# CONTACT PAGE
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("Email: saivullangula0303@gmail.com")

    with open("resume.pdf", "rb") as file:
        st.download_button("Download My Resume", file, file_name="Sai_Kiran_Resume.pdf")

st.markdown("## 💡 Skills")

st.write("""
- Python
- SQL
- Machine Learning
- Data Analysis
- Streamlit
""")