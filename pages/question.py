import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from components import question_item

df_house_rent = pd.read_csv('./data/HCMHouseRentPreprocessing.csv')

def selected_feture():
   selected_year = st.selectbox('Year', list(reversed(range(2015, 2022))))
   selected_district = st.multiselect('District', df_house_rent['district'].unique(), df_house_rent['district'].unique())
   selected_acreage = st.slider('Acreage', min_value=0, max_value=50, value=(0, 1000), step=20)
   selected_price = st.slider('Price', min_value=0, max_value=100000, value=(0, 150000), step=1000)
   return selected_year, selected_district, selected_acreage, selected_price

def filter_data(df, selected_year, selected_district, selected_acreage, selected_price):
   # df = df[df['published'].dt.year == selected_year]
   df = df[df['district'].isin(selected_district)]
   df = df[(df['acreage'] >= selected_acreage[0]) & (df['acreage'] <= selected_acreage[1])]
   df = df[(df['price'] >= (selected_price[0] * 1000)) & (df['price'] <= (selected_price[1] * 1000))]
   return df

def show_data(df):
   st.subheader('Display data after Selected Feature(s)')
   st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
   st.dataframe(df)

def app():
   st.title("Asking meaningful questions that need to be answered")
   
   st.subheader("Choose select feature to have data insights")
   df_filter = filter_data(df_house_rent, *selected_feture())
   st.markdown('---')
   
   show_data(df_filter)
   st.markdown('---')
   
   st.subheader("Choose question to have data insights")
   option = st.selectbox(
      'How would you like to be contacted? 💔',
      ('Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5')
   )
   st.markdown('---')
   
   if option == 'Question 1':
      question_item.question_one(df_filter)
   elif option == 'Question 2':
      question_item.question_two(df_filter)
   elif option == 'Question 3':
      question_item.question_three(df_house_rent)
   elif option == 'Question 4':
      question_item.question_four(df_house_rent, df_filter)
   elif option == 'Question 5':
      question_item.question_five(df_house_rent)
   st.markdown('---')
   