import streamlit as st
from src.session.index import get_dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def Price_followed_District():
    df = get_dataset().copy()
    
    st.write("The bar chart below shows the number of houses for rent in each district of Ho Chi Minh City.")
    st.bar_chart(df['district'].value_counts())
    st.markdown('---')
    
    st.subheader("The bar chart below shows the number of houses for rent in each district of Ho Chi Minh City in year that have most number house rent in each district.")
    df['published'] = pd.to_datetime(df['published'], format='%Y-%m-%d')
    top1_year = df['published'].dt.year.value_counts().index[0]

    fig, ax = plt.subplots()
    ax.bar(df['district'].value_counts().index, df['district'].value_counts().values, label='All year')
    ax.bar(df[df['published'].dt.year == top1_year]['district'].value_counts().index, df[df['published'].dt.year == top1_year]['district'].value_counts().values, label='2022')
    ax.set_xlabel('District')
    ax.set_ylabel('Number of houses')
    ax.set_title('Number of houses for rent in each district of Ho Chi Minh City in year that have most number house rent in each district')
    ax.set_xticks(df['district'].value_counts().index)
    ax.set_xticklabels(df['district'].value_counts().index, rotation=90)
    ax.legend()
    st.pyplot(fig)
    st.markdown('---')

    st.markdown('##### &#9889; <font color="yellow"><b>Comment</b></font>', unsafe_allow_html=True)
    st.markdown('> - We can see in 2022 have number of rooms published most but in the downtown districts tended to decrease significantly, while in the districts adjacent to the city center, the listings were higher, showing us that the demand for housing in the city near the center is higher than the demand for housing in the city center. ')
    st.markdown('> - In 2022 district `Quận Gò Vấp` and `Quận Tân Phú` and `Quận Bình Tân` and `Quận 7` have high rate rate compared to all previous listing time and the remaining districts show no sign of increasing over the previous years (Because the house prices here are quite high and the demand for accommodation is not much or in the districts too far from the city with poor facilities, ... )')
    st.markdown('---')
    
    st.subheader("The boxplot below shows the price of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent.")
    _top_3_district_highest = df['district'].value_counts().head(3).index
    _top_3_district_lowest = df['district'].value_counts().tail(3).index
    fig, ax = plt.subplots()
    sns.boxplot(x='district', y='price', data=df[df['district'].isin([*_top_3_district_highest, *_top_3_district_lowest])], order=[*_top_3_district_highest, *_top_3_district_lowest], showfliers=False, ax=ax)
    ax.set_title('Price of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent')
    ax.set_xlabel('District')
    ax.set_ylabel('Price')
    ax.set_xticklabels([*_top_3_district_highest, *_top_3_district_lowest], rotation=90)
    st.pyplot(fig)
    st.markdown('---')
    
    st.subheader("The boxplot below shows the acreage of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent.")
    fig, ax = plt.subplots()
    sns.boxplot(x='district', y='acreage', data=df[df['district'].isin([*_top_3_district_highest, *_top_3_district_lowest])], order=[*_top_3_district_highest, *_top_3_district_lowest], showfliers=False)
    ax.set_title('Acreage of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent')
    ax.set_xlabel('District')
    ax.set_ylabel('Acreage')
    ax.set_xticklabels([*_top_3_district_highest, *_top_3_district_lowest], rotation=90)
    st.pyplot(fig)
    st.markdown('---')
    
    