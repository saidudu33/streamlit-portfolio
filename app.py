import streamlit as st
st.title("Welcome to the AI Data World")
st.write("Here you can sort the AI data")

st.set_page_config(page_title="V.Sai Kiran Portfolio", layout="wide")

st.title("V. SAI KIRAN - Data Analyst & AI Developer")

st.write("Welcome to my project dashboard built with Streamlit.")

st.header("🚀 My Projects")

st.subheader("1. AI Data Analyst System")
st.write("An AI system that analyzes company data and generates reports.")

st.subheader("2. AI Security Camera")
st.write("A YOLOv8-based surveillance system that detects unusual activities.")

st.subheader("3. Hospital Management System (MySQL)")
st.write("Database system to manage doctors, patients, and appointments.")

st.subheader("4. Food Delivery Database")
st.write("A MySQL project with ER diagram and SQL queries.")


page = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Projects", "Contact"]
)

if page == "Home":
    st.title("Welcome to My Portfolio")

elif page == "Projects":
    st.title("My Projects")
    st.write("List of my AI and Data Analytics projects.")

elif page == "Contact":
    st.title("Contact Me")
    st.write("Email: example@email.com")

    col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 AI Data Analyst System")
    st.write("Automates data analysis and predictions.")

with col2:
    st.subheader("🎥 AI Security Camera")
    st.write("Detects suspicious activity using YOLOv8.")
    

