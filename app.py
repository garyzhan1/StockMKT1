import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="StockMKT", page_icon=":bar_chart:", layout="wide")

# ---- MAINPAGE ----
st.title("StockMKT")
st.markdown("##")

def create_table(n=7):
    df = pd.DataFrame({"x": range(1, 11), "y": n})
    df['x*y'] = df.x * df.y
    return df

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
