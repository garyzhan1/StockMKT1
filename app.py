import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np
if 'chat' not in st.session_state:
    st.session_state.chat = [('A','Hello.')]

def submit():
    st.session_state.chat.append(('B',st.session_state.B))
    st.session_state.chat.append(('A','Some response.'))
    # Clear the text input widget for convenience
    st.session_state.B = ''

for entry in st.session_state.chat:
    st.write(f'{entry[0]}: {entry[1]}')

st.text_input('B\'s Response', key='B', on_change=submit)


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
