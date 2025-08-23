import os
import sys

import streamlit as st
from rich.traceback import install

# from sqlalchemy import text
# from config.config import get_engine
from source.query_runner import run_query

install()

st.write("hello")
