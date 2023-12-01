import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="股票预测平台 战老师", page_icon=":bar_chart:", layout="wide")

# ---- MAINPAGE ----
st.title("股票预测平台 战老师")
st.markdown("##")


my_slider = st.slider("回归结果",0,100,50,1)
if my_slider:f"变量等于{my_slider}时的预测结果是{my_slider * 2 + 0.5 + my_slider ** 1.5}"


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
