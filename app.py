import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import requests
import pandas_datareader as pdr
import pandas_datareader.data as web

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="股票预测平台 战老师", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="C:\zg\code\streamlit-sales-dashboard-main\supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)


# ---- MAINPAGE ----
st.title("股票预测平台 战老师")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)



freq = st.slider('Frequency', min_value=1, max_value=10, value=1)
amp = st.slider('Amplitude', min_value=1, max_value=5, value=1)

# Create x values
x = np.linspace(0, 2*np.pi, 1000)

# Create y values
y = amp * np.sin(freq * x)

# Plot the graph
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('X')
ax.set_ylabel('Y')
st.pyplot(fig)

my_slider = st.slider("回归结果",0,100,50,1)
if my_slider:f"变量等于{my_slider}时的预测结果是{my_slider * 2 + 0.5 + my_slider ** 1.5}"


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
