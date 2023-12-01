import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('column %d' % (i+1) for i in range(5))
)

st.dataframe(df.style.highlight_max(axis=0))

my_slider = st.slider("Customer satisfaction",0,100,50,1)
if my_slider:f"stock price changes by {my_slider * 2 + 0.5 + my_slider ** 1.5} when customer satisfaction is {my_slider}"

my_slider = st.slider("new product",0,100,50,1)
if my_slider:f"stock prices by {my_slider * 2 + 0.5 + my_slider ** 1.5} when the firm annanced {my_slider} new products"

my_slider = st.slider("brand",0,100,50,1)
if my_slider:f"stock price rises by {my_slider * 2 + 0.5 + my_slider ** 1.5} when brand value is {my_slider}"

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns = ["a", "b", "c"])
st.bar_chart(chart_data)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
