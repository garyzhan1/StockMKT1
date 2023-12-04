import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

st.sidebar.button('显示网页1', key='page1')
st.sidebar.button('显示网页2', key='page2')
# 根据按钮点击状态显示相应内容
if st.sidebar.button('显示网页1', key='page1'):
    st.write('这是网页1的内容')
elif st.sidebar.button('显示网页2', key='page2'):
    st.write('这是网页2的内容')
    
my_slider = st.slider("a pioneering innovation",0,10,0,1)
my_slider2 = st.slider("new market entries",0,20,0,1)
my_slider3 = st.slider("minor updates",0,100,0,1)
my_slider4 = st.slider("advertising for new product introduction (million USD)",0,200,0,1)
my_slider5 = st.slider("qaulity improvement (%)",0,100,0,1)
if my_slider:f"stock price will change by {my_slider * 0.0428 + my_slider2 * 0.0098 + my_slider3 * 0.0055 + my_slider4 * 0.0001 + my_slider5 * 0.042}"

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
