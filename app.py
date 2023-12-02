import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np


a = st.slider("a pioneering innovation",0,10,0,1)
b = st.slider("new market entries",0,20,0,1)
c = st.slider("minor updates",0,100,0,1)
d = st.slider("advertising for new product introduction (million USD)",0,200,0,1)
e = st.slider("qaulity improvement (%)",0,100,0,1)
if my_slider:f"stock price changes by {a * 4.28% + b*0.98% + c* 0.55% + d* 0.1% +  e* 4.2%+0} when having {c} minor updates"

st.write("data in a table:")
st.write(pd.DataFrame({
    'first column': [1, my_slider, 5, 7],
    'second column': [10, 30, my_slider2, 70]
}))

col1, col2, col3 = st.columns(3)
col1.metric("cusotmer satisfaction", "1.5", "5%")
col2.metric("brand", "2.5", "-8%")
col3.metric("new product development", "3", "4%")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
