import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

my_slider = st.slider("a pioneering innovation",0,10,0,1)
my_slider2 = st.slider("new market entries",0,20,0,1)
my_slider3 = st.slider("minor updates",0,100,0,1)
my_slider4 = st.slider("advertising for new product introduction (million USD)",0,200,0,1)
my_slider5 = st.slider("qaulity improvement (%)",0,100,0,1)
if my_slider:f"stock price will change by {my_slider * 0.0428 + my_slider2 * 0.0098 + my_slider3 * 0.0055 + my_slider4 * 0.0001 + my_slider5 * 0.042}"

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
