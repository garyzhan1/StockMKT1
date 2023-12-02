import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('rate %d' % (i+1) for i in range(5))
)

st.dataframe(df.style.highlight_max(axis=0))

data = pd.read_csv('supermarkt_sales.csv')
st.sidebar.header("请在这里筛选:")
country = st.sidebar.selectbox(
    "选择国家:",
    options=sorted(data['City'].unique()), # 单选框内容为location列数据
)


my_slider = st.slider("Customer satisfaction",0,100,50,1)
my_slider2 = st.slider("new product",0,20,10,1)
my_slider3 = st.slider("brand",0,100,50,1)
if my_slider:f"stock price changes by {my_slider * 2 + 0.5 + my_slider2 ** 1.5/my_slider3} when customer satisfaction is {my_slider}"

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
    'first column': [1, my_slider, 5, 7],
    'second column': [10, 30, my_slider2, 70],
    '3ond column': [10, 30, my_slider2, 70],
    columns = ["a", "b", "c"])
st.bar_chart(chart_data)

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
