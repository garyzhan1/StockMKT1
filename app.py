import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

tab1, tab2, tab3 = st.tabs(["product", "trademark", "cs"])

with tab1:
   st.header('Product-related factor', divider='rainbow')
   my_slider = st.slider("a pioneering innovation *",0,10,0,1)
   my_slider2 = st.slider("new market entries",0,20,0,1)
   my_slider3 = st.slider("minor updates",0,100,0,1)
   my_slider4 = st.slider("advertising for new product introduction (million USD)",0,200,0,1)
   my_slider5 = st.slider("qaulity improvement (%)",0,100,0,1)
   if my_slider:f"stock price will change by {my_slider * 4.28 + my_slider2 * 0.98 + my_slider3 * 0.55 + my_slider4 * 0.01 + my_slider5 * 4.2}%"

with tab2:
   st.header('trademark', divider='rainbow')
   my_slider6 = st.slider("a brand-association trade mark",0,10,0,1)
   if my_slider:f"stock price will change by {my_slider6 * 0.003}"
   col4, col5 = st.columns(2)
   col4.write("Krasnikov, A., Mishra, S., & Orozco, D. (2009).: Evaluating the financial impact of branding using trademarks: A framework and empirical evidence.")
   col5.write("Krasnikov, A., Mishra, S., & Orozco, D. (2009).: Evaluating the financial impact of branding using trademarks: A framework and empirical evidence.")

col1, col2, col3 = st.columns(3)
col1.metric("cusotmer satisfaction", "1.5", "5%")
col2.metric("brand", "2.5", "-8%")
col3.metric("new product development", "3", "4%")



st.write("data in a table:")
st.write(pd.DataFrame({
    'first column': [1, my_slider, 5, 7],
    'second column': [10, 30, my_slider2, 70]
}))


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
