import streamlit as st
import pandas as pd

def Collection_Screen():
    df = pd.read_csv("data/raw/VN_housing_dataset.csv")
    df = df.iloc[:-1, 1:]
    
    st.title("A. Data Collection")
    st.dataframe(df)
    st.markdown('### ***What subject is data about? What is the source of the data?***')
    st.markdown('''>- The issue of housing prices and rent is one of the issues students and workers are very concerned about at present. In this study, all prices of hostels and houses in Ha Noi in 2020 will be examined. To understand how prices of each region, it will help us find accommodation and housing depending on each person's needs
>- We will use the dataset that has already been collected and is attached as "VN_housing_dataset.csv" in this assignment. This is information about **Vietnam Housing Dataset (Hanoi)**. This data is fetched from [here](https://www.kaggle.com/datasets/ladcva/vietnam-housing-dataset-hanoi?select=VN_housing_dataset.csv&fbclid=IwAR1rf0QHrY45ycc8gA_GeFE9NuRlh41_RIkrNbSB5-0t_vYw79L6PVljvGs).''')
    
    st.markdown('### ***Do authors of this data allow you to use like this?***')
    st.markdown('>- Data files LE ANH DUC Authors')
    st.markdown('>- Data files VĂN VIẾT HIẾU ANH Authors')
    st.markdown('>- Published on 2021')
    st.markdown('>- License: CC BY-NC-SA 4.0')
    st.markdown('### ***How did authors collect data?***')
    st.markdown('>- The data is collected from the State Governments.')
    st.markdown('---')