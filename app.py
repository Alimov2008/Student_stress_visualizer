import streamlit as st
from rich.traceback import install

install()

st.set_page_config(page_title="random name", layout="wide")
st.title("welcome to My streamlit app")
st.write("use sidebard to navigate")
