import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('rate %d' % (i+1) for i in range(5))
)

df2 = pd.read_excel(r'supermarkt_sales.xlsx')
print(df2)

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
