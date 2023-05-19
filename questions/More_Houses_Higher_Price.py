import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.session.index import get_dataset

def More_Houses_Higher_Price_Question():
    plt.figure(figsize=(20, 10))
    df = get_dataset().copy()
    st.header("Is it true that the more houses in the area, the higher the price?")
    st.write("Let's find out!")
    st.write("First, we create dataframe and drop columns that we don't need")
    st.code('''
df = pd.read_csv('../data/processed/VN_housing_dataset.csv')
df.drop(columns=['date','address'], inplace=True)
df''', language='python')
    df.drop(columns=['date','address'], inplace=True)
    st.dataframe(df)
    st.write("Then, we group by district and aggregate price by mean, min, max, count")
    st.code('''
grouped = df.groupby('district').agg({'price': ['mean', 'min', 'max', 'count'], }).reset_index()
grouped''' , language='python')
    grouped = df.groupby('district').agg({'price': ['mean', 'min', 'max', 'count'], }).reset_index()
    st.dataframe(grouped)
    st.write("We sort by count and plot bar chart")
    st.code('''
plt.figure(figsize=(20, 10))
sns.barplot(x='count', y='district', data=grouped.sort_values("count", ascending=False))
plt.show()''', language='python')
    grouped.columns = ['district', 'mean_price', 'min_price', 'max_price', 'count']
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x='count', y='district', data=grouped.sort_values("count", ascending=False), ax=ax)
    st.pyplot(fig)
    st.write("We sort by mean_price and plot bar chart")
    st.code('''
plt.figure(figsize=(20, 10))
sns.barplot(x='mean_price', y='district', data=grouped.sort_values("count", ascending=False))
plt.show()''', language='python')
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x='mean_price', y='district', data=grouped.sort_values("count", ascending=False), ax=ax)
    st.pyplot(fig)
    st.markdown('---')
    st.markdown('##### &#9889; <font color="yellow"><b>Conclusion</b></font>', unsafe_allow_html=True)
    st.markdown('>- As can be seen, The mean of the price fluctuate without any pattern when we sort by number of house. In other words, the price of the house is uncertain and not depend on whether it is a dense house area or not.')
    st.markdown('>- So, the answer is **No**')
    st.markdown('---')
