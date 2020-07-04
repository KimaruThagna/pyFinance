import streamlit as st


st.sidebar.markdown("Welcome to Picture-lytics.")
page = st.sidebar.selectbox("Choose task", ["DCF", "NPV Cashflow"])# pages

if page == "DCF":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Plant Leaf Disease Classification Example")
    st.write("Upload plant leaf images for quick analysis")
    # file upload and handling logic


elif page == "NPV Cashflow":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Brain Tumor MRI Classification Example")
    st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")
