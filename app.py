import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

st.header('股价预测')

my_slider = st.slider("如果是人类，请向右划动",0,1,0,1)

st.write('根据上市公司情况输入数值，股价预测值在页面底部')

tab0, tab1, tab2, tab3, tab4 = st.tabs(["综合", "产品", "社会责任", "品牌", "广告"])

with tab0:
   st.header('综合', divider='rainbow')
   
   # Create a container to hold the input fields
   with st.container():
      col1, col2 = st.columns(2)
      
      # Create input fields for firm name and stock code
      firm_name = col1.text_input("公司名称")
      stock_code = col2.text_input("股票代码")
   
   # Create sliders for customer satisfaction and CSR
   my_slider9 = st.slider("客户满意度", 0, 100, 0, 1)
   my_slider10 = st.slider("质量改进", 0, 100, 0, 1)
   my_slider11 = st.slider("突破性创新", 0, 100, 0, 1)
   my_slider12 = st.slider("新市场", 0, 100, 0, 1)
   my_slider13 = st.slider("社会责任", 0, 100, 0, 1)
   my_slider14 = st.slider("新注册商标", 0, 100, 0, 1)
 # Create a container to display the result
   with st.container():
        # Check if the sliders have been moved
      if my_slider9 or my_slider10:
            # Calculate the result
         result = (my_slider9 * 0.2 + my_slider10 * 0.15 + my_slider11 * 0.1 + my_slider12 * 0.12 + my_slider13 * 0.11 + my_slider14 * 0.08)
         # Display the result as a metric
         st.metric(f"预测值=", f"{result}%", delta=f"{result}%")
         # Limit the result to a maximum of 100 for the progress bar
         # Display the result as a progress bar
         st.progress(min(result, 100) / 100)
         col1, col2, col3 = st.columns([1, 1, 1])
         if result < 20:
               col1.metric(f"{firm_name} ({stock_code}) 未来一年", f"{result}%", "低")
               col1.info("表现较差")
         elif result < 40:
               col2.metric(f"{firm_name} ({stock_code}) 未来一年", f"{result}%", "中")
               col2.warning("表现中等")
         else:
               col3.metric(f"{firm_name} ({stock_code}) 未来一年", f"{result}%", "高")
               col3.success("表现优秀")
         
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
   
   # Create a container to hold the input fields
   with st.container():
      col1, col2 = st.columns(2)
      
      # Create input fields for firm name and stock code
      firm_name = col1.text_input("Firm Name")
      stock_code = col2.text_input("Stock Code")
   
   # Create sliders for customer satisfaction and CSR
   my_slider7 = st.slider("Customer satisfaction", 0, 100, 0, 1)
   my_slider8 = st.slider("CSR", 0, 100, 0, 1)
   
   # Create a container to display the result
   with st.container(border=True):
      # Check if the sliders have been moved
      if my_slider7 or my_slider8:
         # Display the result
         st.write(f"For each unit of change in customer satisfaction or CSR, {firm_name} ({stock_code}) will change by {my_slider7 * 17 + my_slider8 * 14}%")
   
   # Create columns to display additional information
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
