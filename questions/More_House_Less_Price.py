import streamlit as st
from src.session.index import get_dataset


def More_House_Less_Price():
    df = get_dataset().copy()
    
    df.drop(columns=['date','address'], inplace=True)
    st.write(df)
    st.markdown("***")
    
    grouped = df.groupby('district').agg({'price': ['mean', 'min', 'max', 'count'], }).reset_index()
    st.write(grouped)
    st.markdown("***")
    
    grouped.columns = ['district', 'mean_price', 'min_price', 'max_price', 'count']
    st.write(grouped.sort_values("count", ascending=True).plot.barh(x='district', y='count', figsize=(20, 10)))
    st.markdown("***")
    
    st.write(grouped.sort_values("count", ascending=True).plot.barh(x='district', y='mean_price', figsize=(20, 10)))
    
    st.markdown('##### &#9889; <font color="yellow"><b>Conclusion</b></font>', unsafe_allow_html=True)
    st.markdown('>   - As can be seen, The mean of the price fluctuate without any pattern when we sort by number of house. In other words, the price of the house is uncertain and not depend on whether it is a dense house area or not.')
    st.markdown('---')
    