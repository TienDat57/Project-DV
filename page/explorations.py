import streamlit as st
import pandas as pd

def app():
   rented_house_df = pd.read_csv('./data/HCMHouseRentPreprocessing.csv', sep=',')
   
   
   st.title('B. Data explorations (usually interleaved with the data preprocessing phase)')
   st.subheader('The first, we read the data')
   st.code('''
rented_house_df = pd.read_csv('../data/HCMHouseRentPreprocessing.csv', sep=',')
rented_house_df.head()
''', language='python')
   st.dataframe(rented_house_df)
   st.markdown('---')
   st.header('In this phase, we will answer the following questions:')
   
   rented_house_df.index.duplicated(keep='first').sum()
   rented_house_df['published'] = pd.to_datetime(rented_house_df['published'], format='%Y/%m/%d')
   num_cols_df = pd.DataFrame(columns=rented_house_df.columns.drop(['title', 'published', 'street', 'ward', 'district']))
   num_missing_val = rented_house_df[num_cols_df.columns].isnull().sum()
   num_cols_df.loc['missing_ratio'] = num_missing_val / rented_house_df.shape[0] * 100
   rented_house_df = rented_house_df[rented_house_df['acreage'] != 0]
   mean_price_in_district = rented_house_df[rented_house_df['price'] > 0].groupby('district')['price'].mean()
   for district in mean_price_in_district.index:
      rented_house_df.loc[(rented_house_df['price'] < 0) & (rented_house_df['district'] == district), 'price'] = mean_price_in_district[district]
      
   cate_cols_df = pd.DataFrame(columns=rented_house_df.columns.drop(['price', 'acreage']))
   num_missing_val = rented_house_df[cate_cols_df.columns].isnull().sum()
   cate_cols_df.loc['missing_ratio'] = num_missing_val / rented_house_df.shape[0] * 100
   cate_cols_df.loc['num_diff_vals'] = rented_house_df.apply(lambda x: x.nunique())
   cate_cols_df.loc['diff_vals'] = rented_house_df.apply(lambda x: x[~x.isnull()].unique())

   
   with st.expander("How many rows and how many columns?", expanded=True):
      st.code('''
print('Number of rows: ', rented_house_df.shape[0])
print('Number of columns: ', rented_house_df.shape[1])
''', language='python')
      st.write('📜 We have 8877 rows and 8 columns')
   with st.expander("What is the meaning of each row?", expanded=True):
      st.write('📜 A line indicates the information about renting a house in Ho Chi Minh City. Each line provides prices, Acreage in square meter, published date and the address of the house.')
   with st.expander("Are there duplicated rows?", expanded=True):
      st.code('''
num_duplicated_rows = rented_house_df.index.duplicated(keep='first').sum()
num_duplicated_rows
              ''')
      st.write('And then, we can see that there are 0 duplicated rows')
      st.write('📜 There are no duplicated rows')
   with st.expander("What is the meaning of each column?", expanded=True):
      st.write('📜 Each column represents a feature of a customer')
      st.write('📜 The meaning of each column is:')
      st.write('''
            - **id:** The id of the rented houses
            - **title:** The title of the rented houses
            - **price**: price of the rented houses (if price is -1, it mean the owner want to disscuss more)
            - **published**: The published date of the rented houses
            - **acreage:** The acreage of the rented houses
            - **street**: The street of the rented houses
            - **ward**: The ward of the rented houses
            - **district**: The district of the rented houses
      ''')
   with st.expander("What is the current data type of each column? Are there columns having inappropriate data types?", expanded=True):
      st.code('''
col_dtypes = rented_house_df.dtypes
col_dtypes
              ''')
      st.write('📜 Data types of each column:')
      st.write('''
            - **id:** int64
            - **title:** object
            - **price**: int64
            - **published**: object
            - **acreage:** float64
            - **street**: object
            - **ward**: object
            - **district**: object
      ''')
      st.markdown('---')
      st.markdown('📜**<font color="yellow">Comment</font>**', unsafe_allow_html=True)
      st.markdown('- **We can see that the data type of published column is object, we need to convert it to datetime, so we can use it to analyze the data. And there are 4 columns with the datatype of `object`: `street`, `ward`, `district` and `title`.**')
      st.code('''
rented_house_df['published'] = pd.to_datetime(rented_house_df['published'])
rented_house_df.dtypes
               ''')
   with st.expander("With each numerical column, how are values distributed?", expanded=True):
      st.subheader('- What is the percentage of missing values?')
      st.code('''
num_cols_df = pd.DataFrame(columns=rented_house_df.columns.drop(['title', 'published', 'street', 'ward', 'district']))
num_missing_val = rented_house_df[num_cols_df.columns].isnull().sum()
num_cols_df.loc['missing_ratio'] = num_missing_val / num_rows * 100
num_cols_df
              ''')
      st.write('📜 The percentage of missing values:')
      st.write('''
            - **id:** 0.0
            - **price**: 0.0
            - **acreage:** 0.0
            ''')
      st.write("With each numerical column, how are values distributed?")
      st.markdown('---')
      st.subheader('- Min? max? Are they abnormal?')
      st.code('''
rented_house_df.describe()
              ''')
      st.write('📜 The min, max and mean of each numerical column:')
      st.dataframe(rented_house_df.describe())
      st.markdown('---')
      st.markdown('📜 ** <font color="yellow">Comment</font> **', unsafe_allow_html=True)
      st.markdown('- **We can see that the min of price is 500000, the max of price is 150000000, the min of acreage is 5, the max of acreage is 1000.And the acreage of the rented houses can not equal 0. So we need to remove them.**')
      st.code('''
rented_house_df = rented_house_df[rented_house_df['acreage'] != 0]
rented_house_df.describe() 
               ''')
      st.markdown('---')
      st.markdown('📜**<font color="yellow">Comment</font>**', unsafe_allow_html=True)
      st.markdown('- **The price of rented houses exists -1 (means the owner want to disscuss more). So we need to replace -1 with mean of the price in the same district.**')
      st.code('''
mean_price_in_district = rented_house_df[rented_house_df['price'] > 0].groupby('district')['price'].mean()
for district in mean_price_in_district.index:
    rented_house_df.loc[(rented_house_df['price'] < 0) & (rented_house_df['district'] == district), 'price'] = mean_price_in_district[district]
print('The number of rows with price < 0: ', rented_house_df[rented_house_df['price'] < 0].count()['price'])
         ''')
      st.write('📜 The number of rows with price < 0: 0')
      
   with st.expander("With each categorical column, how are values distributed?", expanded=True):
      st.subheader('- What is the percentage of missing values?')
      st.subheader('- How many different values? Show a few Are they abnormal?')
      st.code('''
cate_cols_df = pd.DataFrame(columns=rented_house_df.columns.drop(['price', 'acreage']))
num_missing_val = rented_house_df[cate_cols_df.columns].isnull().sum()
cate_cols_df.loc['missing_ratio'] = num_missing_val / num_rows * 100
cate_cols_df.loc['num_diff_vals'] = rented_house_df.apply(lambda x: x.nunique())
cate_cols_df.loc['diff_vals'] = rented_house_df.apply(lambda x: x[~x.isnull()].unique())
cate_cols_df
              ''')
      st.write('📜 The percentage of missing values:')
      # st.dataframe(cate_cols_df)
      
   st.markdown(
    """
      <style>
      .streamlit-expanderHeader > div > p {
         font-size: x-large;
         font-weight: 700;
      }
      </style>
   """,
    unsafe_allow_html=True,
   )