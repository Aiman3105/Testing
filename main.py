import streamlit as st

Button= st.button("Go")

if Button:
    st.camera_input("Camera")