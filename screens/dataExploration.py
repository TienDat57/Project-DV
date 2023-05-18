import streamlit as st
import pandas as pd
import re
import math
import seaborn as sns
import matplotlib.pyplot as plt

def nan_to_0(value):
    result = 0
    try:
        result = re.findall(r"[-+]?\d*\,?\d+|\d+", value)[0].replace(",", ".")
        result = int(result) if result.find(".") == -1 else float(result) 

    except:
        result = 0
    return result

def nan_to_0_or_1(value):
    result = 0
    
    try:
        float(value)
        result = 0
    except:
        result = 1
    
    return result

def draw_category_with_offset_limit(category, offset, limit):
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x = category.index, y = category.values, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 50)

    ax.set_xlim(offset * 40, limit * 40)
    st.pyplot(fig)

def Exploration_Screen():
    df = pd.read_csv("./data/raw/VN_housing_dataset.csv")
    df = df.iloc[:-1, 1:]
    df_without_pre_proccessing = df
    
    st.title("B. Data exploration.")
    st.subheader('The first, we read the data')
    st.code('''
df = pd.read_csv ('../data/raw/VN_housing_dataset.csv')
df_without_pre_proccessing = df
df.head()
''', language='python')
    st.dataframe(df)
    st.markdown('---')
    
    st.header('In this phase, we will answer the following questions:')
    with st.expander(''' **1. How many rows and how many columns?**''', expanded=True):
        n_rows, n_cols = df.shape
        st.code('''
num_rows, num_cols = df_without_pre_proccessing.shape
print('Number of rows: ', num_rows)
print('Number of columns: ', num_cols)
''', language='python')
        st.write("Number of rows: " + str(n_rows))
        st.write("Number of columns: " + str(n_cols))
    with st.expander(''' **2. What is the meaning of each row?**''', expanded=True):
        st.write('📜 Each row is management some significant information of a house like address, number of rooms, number of floors, squares, price,..etc')
    with st.expander(''' **3. Are there duplicated rows?**''', expanded=True):
        st.code('''
num_duplicated_rows = df.duplicated().sum()
num_duplicated_rows)
''', language='python')
        num_duplicated_rows = df.duplicated().sum()
        st.write("Number of duplicated rows: " + str(num_duplicated_rows))
        st.write('There are 815 duplicated rows.')
        st.write('📜 We will remove them.')
        st.code('''
df = df.drop_duplicates()
df
''', language='python')
        df = df.drop_duplicates()
        st.dataframe(df)
    with st.expander(''' **4. What is the meaning of each column?**''', expanded=True):
        st.code('''
rename_lst = ['date', 'address', 'district', 'town', 'house_type', 'paper_type', 'num_floors', 'num_rooms', 
              'squares', 'length', 'width', 'price_per_m2']
df.columns = rename_lst
df''', language='python')
        rename_lst = ['date', 'address', 'district', 'town', 'house_type', 'paper_type', 'num_floors', 'num_rooms',
                        'squares', 'length', 'width', 'price_per_m2']
        df.columns = rename_lst
        st.dataframe(df)
        st.write('''
>The meaning of all columns:
>- **date**: The date the house is published to sell. 
>- **address**: House's address. 
>- **district**: House's district. 
>- **town**: House's town. 
>- **house_type**: House's type
>- **paper_type**: House's paper work
>- **num_floors**: How many floors are there in this house?
>- **num_rooms**: How many rooms are there in this house?
>- **squares**: Houes's squares
>- **length**: House's length
>- **width**: House's width
>- **price_per_m2**: price per m2
        ''')
    with st.expander(''' **5. What is the current data type of each column? Are there columns having inappropriate data types?**''', expanded=True):
        st.code('''
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                df.dtypes
                ''', language='python')
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
        st.write(df.dtypes)
        st.code('''
num_floors = df["num_floors"].tolist()
num_rooms = df["num_rooms"].tolist()
squares = df["squares"].tolist()
length = df["length"].tolist()
width = df["width"].tolist()
price_per_m2 = df["price_per_m2"].tolist()
paper_type = df["paper_type"].tolist()


num_floors = map(nan_to_0, num_floors)
num_rooms = map(nan_to_0, num_rooms)
squares =  map(nan_to_0, squares)
length =  map(nan_to_0, length)
width =  map(nan_to_0, width) 
price_per_m2 =  map(nan_to_0, price_per_m2)
paper_type = map(nan_to_0_or_1, paper_type)


df["num_floors"] = list(num_floors)
df["num_rooms"] = list(num_rooms)
df["squares"] = list(squares)
df["length"] = list(length)
df["width"] = list(width)
df["price_per_m2"] = list(price_per_m2)
df["paper_type"] = df["paper_type"].fillna("Chưa có sổ")
''', language='python')
        num_floors = df["num_floors"].tolist()
        num_rooms = df["num_rooms"].tolist()
        squares = df["squares"].tolist()
        length = df["length"].tolist()
        width = df["width"].tolist()
        price_per_m2 = df["price_per_m2"].tolist()
        paper_type = df["paper_type"].tolist()


        num_floors = map(nan_to_0, num_floors)
        num_rooms = map(nan_to_0, num_rooms)
        squares =  map(nan_to_0, squares)
        length =  map(nan_to_0, length)
        width =  map(nan_to_0, width) 
        price_per_m2 =  map(nan_to_0, price_per_m2)
        paper_type = map(nan_to_0_or_1, paper_type)


        df["num_floors"] = list(num_floors)
        df["num_rooms"] = list(num_rooms)
        df["squares"] = list(squares)
        df["length"] = list(length)
        df["width"] = list(width)
        df["price_per_m2"] = list(price_per_m2)
        df["paper_type"] = df["paper_type"].fillna("Chưa có sổ")
        st.code('''
indexAge = df[ (df['length'] >= 1000) | (df['width'] >= 1000) | (df['squares'] >= 1000)].index
df.drop(indexAge , inplace=True)

df = df[(df['price_per_m2'] != 0.00)]

#Drop Length and width
df.drop(['length', 'width'], axis=1, inplace=True)

df''', language='python')
        indexAge = df[ (df['length'] >= 1000) | (df['width'] >= 1000) | (df['squares'] >= 1000)].index
        df.drop(indexAge , inplace=True)
        df = df[(df['price_per_m2'] != 0.00)]
        #Drop Length and width
        df.drop(['length', 'width'], axis=1, inplace=True)
        st.dataframe(df)
    with st.expander('''**What is the percentage of missing values?**''', expanded=True):
        st.code('''
percent_missing = df_without_pre_proccessing.isnull().sum() * 100 / len(df_without_pre_proccessing)
missing_value_df = pd.DataFrame({'column_name': df_without_pre_proccessing.columns,
                                 'percent_missing': percent_missing,
                                 'num_missing': df_without_pre_proccessing.isnull().sum()})
missing_value_df''', language='python')
        percent_missing = df_without_pre_proccessing.isnull().sum() * 100 / len(df_without_pre_proccessing)
        missing_value_df = pd.DataFrame({'column_name': df_without_pre_proccessing.columns,
                                        'percent_missing': percent_missing,
                                        'num_missing': df_without_pre_proccessing.isnull().sum()})
        st.dataframe(missing_value_df)
        st.write("🔥 Drop missing rows")
        st.code('''
df = df.dropna()
percent_missing = df.isnull().sum() * 100 / len(df_without_pre_proccessing)
missing_value_df = pd.DataFrame({'column_name': df.columns,
                                 'percent_missing': percent_missing,
                                 'num_missing': df.isnull().sum()})
missing_value_df''', language='python')
        df = df.dropna()
        percent_missing = df.isnull().sum() * 100 / len(df_without_pre_proccessing)
        missing_value_df = pd.DataFrame({'column_name': df.columns,
                                        'percent_missing': percent_missing,
                                        'num_missing': df.isnull().sum()})
        st.dataframe(missing_value_df)
    with st.expander('''**6. With each numerical column, how are values distributed?**''', expanded=True):
        st.code('''
fig, axs = plt.subplots(4)

columns = ['price_per_m2', 'num_floors', 'num_rooms', 'squares', '']
for i, ax in enumerate(axs):
    sns.histplot(x=df[columns[i]], ax=ax)
    
fig.set_size_inches(15, 30)
plt.show()''', language='python')
        fig, axs = plt.subplots(4)

        columns = ['price_per_m2', 'num_floors', 'num_rooms', 'squares', '']
        for i, ax in enumerate(axs):
            sns.histplot(x=df[columns[i]], ax=ax)
            
        fig.set_size_inches(15, 30)
        st.pyplot(fig)
        st.write("🔥 Min? max? Are they abnormal?")
        st.code('''
num_floors_max = df['num_floors'].max()
num_rooms_max = df['num_rooms'].max()
squares_max = df['squares'].max()
price_per_m2_max = df['price_per_m2'].max()

max_values = [num_floors_max, num_rooms_max, squares_max, price_per_m2_max]

header = ["num_floors(num)", "num_rooms(num)", "squares(m2)", "price_per_m2(VND)"]

max_df = pd.DataFrame(max_values, header, columns=["Max"])
max_df''', language='python')
        num_floors_max = df['num_floors'].max()
        num_rooms_max = df['num_rooms'].max()
        squares_max = df['squares'].max()
        price_per_m2_max = df['price_per_m2'].max()

        max_values = [num_floors_max, num_rooms_max, squares_max, price_per_m2_max]

        header = ["num_floors(num)", "num_rooms(num)", "squares(m2)", "price_per_m2(VND)"]

        max_df = pd.DataFrame(max_values, header, columns=["Max"])
        st.dataframe(max_df)
        st.code('''
num_floors_min = df['num_floors'].min()
num_rooms_min = df['num_rooms'].min()
squares_min = df['squares'].min()
price_per_m2_min = df['price_per_m2'].min()

min_values = [num_floors_min, num_rooms_min, squares_min, price_per_m2_min]

header = ["num_floors(num)", "num_rooms(num)", "squares(m2)", "price_per_m2(VND)"]

min_df = pd.DataFrame(min_values, header, columns=["Min"])
min_df''', language='python')
        num_floors_min = df['num_floors'].min()
        num_rooms_min = df['num_rooms'].min()
        squares_min = df['squares'].min()
        price_per_m2_min = df['price_per_m2'].min()

        min_values = [num_floors_min, num_rooms_min, squares_min, price_per_m2_min]

        header = ["num_floors(num)", "num_rooms(num)", "squares(m2)", "price_per_m2(VND)"]

        min_df = pd.DataFrame(min_values, header, columns=["Min"])
        st.dataframe(min_df)
    
    with st.expander('''**7. With each categorical column, how are values distributed?**''', expanded=True):
        st.code('''
categories = df.loc[:,df.dtypes=="object"]
categories''' , language='python')
        categories = df.loc[:,df.dtypes=="object"]
        st.dataframe(categories)
        st.code('''
house_type_category = categories.groupby('house_type')["house_type"].count()

draw_category_with_offset_limit(house_type_category, 0, 1)
''' , language='python')
        house_type_category = categories.groupby('house_type')["house_type"].count()
        draw_category_with_offset_limit(house_type_category, 0, 1)
        st.code('''
district_category = categories.groupby('district')["district"].count()

draw_category_with_offset_limit(district_category, 0, 1)
''' , language='python')
        district_category = categories.groupby('district')["district"].count()
        draw_category_with_offset_limit(district_category, 0, 1)
        st.code('''
town_category = categories.groupby('town')["town"].count()

draw_category_with_offset_limit(town_category, 0, 1)
draw_category_with_offset_limit(town_category, 1, 2)
draw_category_with_offset_limit(town_category, 2, 3)
draw_category_with_offset_limit(town_category, 3, 4)
draw_category_with_offset_limit(town_category, 4, 5)
draw_category_with_offset_limit(town_category, 5, 6)
draw_category_with_offset_limit(town_category, 6, 7)
''' , language='python')
        town_category = categories.groupby('town')["town"].count()

        draw_category_with_offset_limit(town_category, 0, 1)
        draw_category_with_offset_limit(town_category, 1, 2)
        draw_category_with_offset_limit(town_category, 2, 3)
        draw_category_with_offset_limit(town_category, 3, 4)
        draw_category_with_offset_limit(town_category, 4, 5)
        draw_category_with_offset_limit(town_category, 5, 6)
        draw_category_with_offset_limit(town_category, 6, 7)
    st.subheader('Save the cleaned data')
    st.code('''
df.to_csv("../data/processed/VN_housing_dataset.csv", index=False)
''', language='python')