import streamlit as st
from src.session.index import get_dataset
from sklearn.preprocessing import OrdinalEncoder

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def Regression():
    df = get_dataset().copy()
    
    st.write(df.head())
    st.markdown('---')
    
    st.header("1. Drop irrelevant columns")
    df = df.drop(['date', 'address', 'town', 'paper_type'], axis=1)
    st.markdown('---')
    
    oe = OrdinalEncoder()
    df[['district', 'house_type']] = oe.fit_transform(df[['district', 'house_type']]).astype(int)
    st.markdown('---')
    
    st.header("2. Log transformation")
    df_log = df.copy()
    df_log[['price_per_m2', 'squares']] = np.log(df[['price_per_m2', 'squares']])
    df_log.hist(bins=50, figsize=(15,10))
    st.write(plt.show())
    st.markdown('---')
    
    st.header("3. Regression Model")
    X = df_log.drop(['price_per_m2'], axis=1)
    y = df_log['price_per_m2']
    model1 = sm.OLS(y, X).fit()
    st.write(model1.summary())
    st.markdown('---')
    
    st.markdown('##### &#9889; <font color="yellow"><b>Conclusion</b></font>', unsafe_allow_html=True)
    st.markdown('>   - **P(>|t|)**: p-value for these variables are less than 0.05 there are statistically significant association between price and there variables.')
    st.markdown('>   - **p_value**: The model fits well with the observed data statistically.(p_value = 0.00)')
    st.markdown('>   - **R-squared**: 0.983, which means that 98.3% of the variation in price is explained by these variables in the model.')
    st.markdown('>   - **log(price_per_m2) = 0.06 * district + 0.16 * house_type + 0.02 * num_floors + 0.06 * num_rooms + 0.73 * squares**')
    st.markdown('---')
    