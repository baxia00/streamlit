import streamlit as st
import numpy as np
import pandas as pd
import os,time

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
	form = st.form("my_form")
	form.text_input("用户名")
	form.text_input("密码")
	form.form_submit_button("登录")

