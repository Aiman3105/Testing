import streamlit as st
import cv2
import time


Button= st.button("Go")

if Button:
    video=cv2.VideoCapture(0)
    check, frame = video.read()
    cv2.imwrite("Test.png", frame)

    st.image("Test.png")