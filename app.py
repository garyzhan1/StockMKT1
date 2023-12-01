import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

my_slider = st.slider("Customer satisfaction",0,100,50,1)
if my_slider:f"stock price changes by {my_slider * 2 + 0.5 + my_slider ** 1.5} when customer satisfaction is {my_slider}"

my_slider = st.slider("new product",0,100,50,1)
if my_slider:f"stock prices by {my_slider * 2 + 0.5 + my_slider ** 1.5} when the firm annanced {my_slider} new products"

my_slider = st.slider("brand",0,100,50,1)
if my_slider:f"stock price rises by {my_slider * 2 + 0.5 + my_slider ** 1.5} when brand value is {my_slider}"


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
