import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

st.header('股价预测')

my_slider = st.slider("Human-Robot Testing: If you are a human, please slide to the right. Otherwise you will not be able to use this tool",0,1,0,1)

st.write('Please select the values for the following dimensions based on the situation of the listed company you are interested in, and the changes in stock prices will be displayed at the bottom of this page')

tab1, tab2, tab3, tab4 = st.tabs(["Product", "Customer satisfaction & CSR", "Brand", "Advertising"])

with tab1:
   st.header('Product-related factor', divider='rainbow')
   my_slider1 = st.slider("a pioneering innovation",0,20,0,1)
   my_slider2 = st.slider("new market entries",0,20,0,1)
   my_slider3 = st.slider("minor updates",0,100,0,1)
   my_slider4 = st.slider("advertising for new product introduction (million USD) ",0,200,0,1)
   my_slider5 = st.slider("qaulity improvement (%)",0,100,0,1)
   with st.container(border=True):
      if my_slider:f"stock price will change by {my_slider1 * 4.28 + my_slider2 * 0.98 + my_slider3 * 0.55 + my_slider4 * 0.01 + my_slider5 * 4.2}%"
   col6, col7 = st.columns(2)
   col6.write("The parameter used in the prediction was developed on the basis of:")
   col7.write("Krasnikov, A., Mishra, S., & Orozco, D. (2009). Evaluating the financial impact of branding using trademarks: A framework and empirical evidence. Journal of Marketing, 73(6), 154-166.")

with tab2:
   st.header('Customer satisfaction & CSR', divider='rainbow')
   my_slider7 = st.slider("Customer satisfaction",0,100,0,1)
   my_slider8 = st.slider("CSR",0,100,0,1)
   with st.container(border=True):
      if my_slider:f"for each unit of change in customer satisfaction or CSR, stock price will change by {my_slider7 * 17 + my_slider8 * 14}%"
   col6, col7 = st.columns(2)
   col6.write("The parameter used in the prediction was developed on the basis of the American Customer Satisfaction Index (ACSI) and Fortune America's Most Admired Corporations (FAMA).")
   col7.write("Source: Luo, X., & Bhattacharya, C. B. (2006). Corporate social responsibility, customer satisfaction, and market value. Journal of marketing, 70(4), 1-18.")

with tab3:
   st.header('Trademark', divider='rainbow')
   my_slider6 = st.slider("number of trademarks specifying brand attribute or image",0,50,0,1)
   with st.container(border=True):
      if my_slider:f"stock price will change by {my_slider6 * 0.3}%"

   col4, col5 = st.columns(2)
   col4.write("The parameter used in the prediction was developed on the basis of:")
   col5.write("Krasnikov, A., Mishra, S., & Orozco, D. (2009). Evaluating the financial impact of branding using trademarks: A framework and empirical evidence. Journal of Marketing, 73(6), 154-166.")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
