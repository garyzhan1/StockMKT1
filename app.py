import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np

st.header('Armstock上市公司股价预测工具：产品、消费者、品牌对股价的影响')

my_slider = st.slider("人机测试：如果你是人类，请滑到右边，否则无法使用本工具",0,1,0,1)

st.write('请根据您关注的上市公司情况选择以下各维度的数值，股价变化将展示在本页下方')

tab1, tab2, tab3 = st.tabs(["Product产品", "消费者满意度和CSR", "Trademark商标"])

with tab1:
   st.header('Product-related factor产品相关变量', divider='rainbow')
   my_slider1 = st.slider("a pioneering innovation开创性创新的数量",0,20,0,1)
   my_slider2 = st.slider("new market entries进入了几个新产品市场",0,20,0,1)
   my_slider3 = st.slider("minor updates微创新的数量",0,100,0,1)
   my_slider4 = st.slider("advertising for new product introduction (million USD) 用于新产品推广的广告费（百万美金）",0,200,0,1)
   my_slider5 = st.slider("qaulity improvement (%)产品质量改进百分比",0,100,0,1)
   with st.container(border=True):
      if my_slider:f"stock price will change by 股价将会变动 {my_slider1 * 4.28 + my_slider2 * 0.98 + my_slider3 * 0.55 + my_slider4 * 0.01 + my_slider5 * 4.2}%"
   col6, col7 = st.columns(2)
   col6.write("The parameter used in the prediction was developed on the basis of: 预测模型中的参数来自论文：")
   col7.write("Krasnikov, A., Mishra, S., & Orozco, D. (2009). Evaluating the financial impact of branding using trademarks: A framework and empirical evidence. Journal of Marketing, 73(6), 154-166.")

with tab2:
   st.header('Customer satisfaction & CSR消费者满意度和企业社会责任', divider='rainbow')
   my_slider7 = st.slider("Customer satisfaction 消费者满意度",0,100,0,1)
   my_slider8 = st.slider("CSR 企业社会责任",0,100,0,1)
   with st.container(border=True):
      if my_slider:f"for each unit of change in customer satisfaction or CSR, stock price will change by 股价将会变动 {my_slider7 * 17 + my_slider8 * 14}%"
   col6, col7 = st.columns(2)
   col6.write("The parameter used in the prediction was developed on the basis of the American Customer Satisfaction Index (ACSI), Fortune America's Most Admired Corporations (FAMA).预测模型中的参数来自美国消费者满意度指数和福布斯美国最受赞赏公司榜单")
   col7.write("Source: Luo, X., & Bhattacharya, C. B. (2006). Corporate social responsibility, customer satisfaction, and market value. Journal of marketing, 70(4), 1-18.")

with tab3:
   st.header('Trademark 商标', divider='rainbow')
   my_slider6 = st.slider("number of trademarks specifying brand attribute or image 带有品牌属性或形象的商标数量",0,50,0,1)
   with st.container(border=True):
      if my_slider:f"stock price will change by股价将会变动 {my_slider6 * 0.3}%"

   col4, col5 = st.columns(2)
   col4.write("The parameter used in the prediction was developed on the basis of: 预测模型中的参数来自论文：")
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
