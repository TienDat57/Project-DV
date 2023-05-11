import streamlit as st
import pandas as pd

def app():
   st.title("A. Data Collection")

   st.markdown('### ***What subject is data about? What is the source of the data?***')
   st.markdown('''>- The issue of housing prices and rent is one of the issues students and workers are very concerned about at present. In this study, all prices of hostels and houses in Ho Chi Minh City from 2015 to present will be examined. To understand how prices change year over year, each region was examined. After that, it will help us find accommodation and housing depending on each person's needs
>- We will use the dataset that has already been collected and is attached as "HCMHouseRent.csv" in this assignment. This is information about **Vietnam House Rent Dataset**. This data is fetched from [here](https://www.kaggle.com/datasets/vanviethieuanh/vietnam-house-rent-dataset?select=hcm.csv).''')

   st.markdown('### ***Do authors of this data allow you to use like this?***')
   st.markdown('''>- Yes, we can use this data like this. Because this data is open source and we can use it for free
>- Data files VĂN VIẾT HIẾU ANH Authors
>- Published on 13/08/2022''')

   st.markdown('### ***How did authors collect data?***')
   st.markdown('>- The data is collected from the State Governments.')
   st.markdown('---')

   st.title("Data Cleaning and Preparation")
   st.markdown('### **Reading the data**')
   st.code('''HCMHouseRent = pd.read_csv('../data/HCMHouseRent.csv')''', language='python')
   HCMHouseRent = pd.read_csv('./data/HCMHouseRent.csv')
   st.dataframe(HCMHouseRent)
   st.code('''HCMHouseRent.info()''', language='python')
   st.write(''' Index| Column|     Non-Null Count|  Dtype''')
   st.write(''' 0|   title|      9733 non-null|   object ''')
   st.write(''' 1|   price|      9733 non-null|   float64''')
   st.write(''' 2|   published|  9733 non-null|   object ''')
   st.write(''' 3|   acreage|    9733 non-null|   float64''')
   st.write(''' 4|   address|    9733 non-null|   object ''')
   st.markdown('---')
   st.markdown(">We see, published column is date time but now it's object. So, we need change to datetime")
   st.write(''' Index| Column|     Non-Null Count|  Dtype''')
   st.write(''' 0|   title|      9733 non-null|   object ''')
   st.write(''' 1|   price|      9733 non-null|   float64''')
   st.write(''' 2|   published|  9733 non-null|   datetime64[ns] ''')
   st.write(''' 3|   acreage|   9733 non-null|   float64''')
   st.write(''' 4|   address|    9733 non-null|   object ''')
   st.markdown('---')
   st.markdown(">Because the price column has a format of 2.2 instead of 2,200,000. Computational difficulty. So I'll convert it to millions")
   st.code('''HCMHouseRent['price'] = HCMHouseRent['price']*1000000''', language='python')
   HCMHouseRent['price'] = HCMHouseRent['price']*1000000
   st.dataframe(HCMHouseRent)
   st.dataframe(HCMHouseRent.describe())
   st.markdown('---')
   st.markdown('>Due to address is too long, we will split it into 3 column: street, wart and district')
   st.markdown('> I will delete the row that has price < 500k and area is 0 m2')
   HCMHouseRent1 = pd.read_csv('./data/HCMHouseRentPreprocessing.csv')
   st.dataframe(HCMHouseRent1)

   st.markdown('---')
   st.markdown('<center>Complete preprocessing<center>', unsafe_allow_html=True)

