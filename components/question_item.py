import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from constants.index import list_questions
from components import tab_sections

def question_one(df):
   st.markdown(list_questions[0], unsafe_allow_html=True)
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
   
   tab_sections.make_tab_sections(0)
   
def question_two(df):
   st.markdown(list_questions[1], unsafe_allow_html=True)
   
   df['month'] = pd.DatetimeIndex(df['published']).month
   df['year'] = pd.DatetimeIndex(df['published']).year
   
   df['month_year'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
   df['month_year'] = pd.to_datetime(df['month_year']).dt.strftime('%Y-%m')

   # group by month and count number of houses
   df['month_year'].groupby(df['month']).count()

   # calculate number of houses in month for each year
   month_each_year = df['month_year'].groupby([df['month'], df['year']]).count()
   month_each_year.head(12)   
   
   sum_each_month = month_each_year.groupby(month_each_year.index.get_level_values(0)).sum().reindex(range(1,13)).reindex(range(1,13), fill_value=0)
   # create a dataframe with month and sum_each_month column
   sum_each_month_df = pd.DataFrame({'month': sum_each_month.index, 'sum_each_month': sum_each_month.values})
   sum_each_month_df['average'] = sum_each_month_df['sum_each_month'] / (df['year'].unique().size)
   st.write("Dataframe with month, total number of houses and average number of houses.")
   st.dataframe(sum_each_month_df) 
   
   st.write("The bar chart below shows the Average number of houses rented in each month.")
   
   fig, ax = plt.subplots()
   ax.bar(sum_each_month.index , sum_each_month_df['average'].values, label='All year')
   ax.set_xlabel('Month')
   ax.set_ylabel('Average')
   ax.set_title('Average number of houses rented in each month')
   ax.legend()
   st.pyplot(fig)
   st.markdown('---')
   
   tab_sections.make_tab_sections(1)
   
def question_three(df):
   st.markdown(list_questions[2], unsafe_allow_html=True)
   st.markdown('---')
   st.markdown('### ✨ **1. Get data by year**')
   df['published'] = pd.DatetimeIndex(df['published'])
   df.set_index('id')
   st.dataframe(df)
   st.markdown('> 📙 Get mean price per year')
   df_group_by_year = {}
   df_group_by_year['published'] = df.groupby(df['published'].dt.year, axis=0)['price'].mean()
   st.dataframe(df_group_by_year)
   st.markdown('### 🎖 **2. Visualization by the price of each year.**')
   fig, ax = plt.subplots(figsize=(10, 5))
   ax.plot(df_group_by_year['published'].index , df_group_by_year['published'].values, label='All year')
   ax.set_xlabel('Year')
   ax.set_ylabel('Average rent')
   ax.set_title('Price of accommodation by year')
   ax.legend()
   st.pyplot(fig)
   st.subheader('#### Within 5 years from 2018-2022, the rental price is stable year by year, it does not go up or down, then the market is gradually stabilizing and has a specific price.')
   st.markdown('---')
   
   st.markdown('##### &#9889; <font color="yellow"><b>What are benefits of finding the answer?</b></font>', unsafe_allow_html=True)
   st.markdown('>   - Evaluate the price of accommodation every year.')
   st.markdown('>   - We can know  the rental rates fluctuated in HCM City.')
   st.markdown('>   - As we can see, during the years (2018 - 2020) of the covid epidemic, the price of accommodation has decreased significantly.')
   st.markdown('---')
   
   st.markdown('### 🎖 3. Which month is the best time to rent ?')
   st.markdown('> Group by data by month')
   grouped = df.groupby(df['published'].dt.month)
   st.dataframe(grouped['price'].describe())
   st.markdown('---')
   st.subheader("Draw boxplot to check which month has an addorable price")
   fig, ax = plt.subplots()
   grouped.boxplot(subplots=False, rot=45, fontsize=8, column='price', figsize=(15,10), ax=ax)
   ax.set_title('Which has an addorable price')
   ax.set_xlabel('month')
   ax.set_ylabel('price')
   st.pyplot(fig)
   st.markdown('#### ✨**As we can see in the data, February, September and October are the best time to rent by the affordable price**')


def question_four(df, df_filter):
   st.markdown(list_questions[3], unsafe_allow_html=True)
   st.markdown('---')
   st.markdown('### 🔥**Statistics on average price and area of ​​each district.**')
   df['price_per_square_meter'] = df['price'] / df['acreage']
   price_per_square_meter = round(df.groupby('district').price_per_square_meter.mean().sort_values(ascending=False), 3)
   new_df = pd.DataFrame({'district':price_per_square_meter.index, 'price_per_square_meter': price_per_square_meter.values})
   new_df = new_df.sort_values(by='price_per_square_meter', ascending=False)
   st.bar_chart(new_df, x='district', y='price_per_square_meter', width=0, height=0, use_container_width=True)
   st.markdown('##### &#9889; <font color="yellow"><b>Comment</b></font>', unsafe_allow_html=True)
   st.markdown('>   - Based on the chart above, we can see that the rent of accommodation in `District 1`, `District 3` is quite high compared to other districts (average 180000-190000/m^2). This may be due to the location of these districts in the city center, so many people rent rooms here.')
   st.markdown('>   - `Hoc Mon` and `Cu Chi` districts are located far from the city center, with few schools and industrial parks, so the demand for rental accommodation here is quite small, so the rental price here is lower than other districts.(only) about 60000-80000/m^2)')
   st.markdown('>   - The rest, the rental price in other districts is at the average level with the income of the people of the City. Because these districts are located near the city center, it is also convenient for students, students as well as workers.')
   st.markdown('---')
   st.markdown('### 📌 **For each district, show the percentage of acreage** ')
   df_filter = df_filter.sort_values(by='acreage', ascending=False)
   percent = df_filter['acreage'].value_counts(normalize=True) * 100
   percent = percent.sort_values(ascending=False)
   top_10_percent = percent.head(20)
   top_10_percent = pd.DataFrame({'acreage':top_10_percent.index, 'percent': top_10_percent.values}).sort_values(by='percent', ascending=False)
   st.markdown('<center>Percents of acreage</center>', unsafe_allow_html=True)
   st.bar_chart(top_10_percent, x='acreage', y='percent', width=0, height=0, use_container_width=True)
   st.markdown('##### &#9889; <font color="yellow"><b>Comment</b></font>', unsafe_allow_html=True)
   st.markdown('>   - Knowing the price of accommodation in each district, combined with the area, we will know how different each district will be.')
   st.markdown(">   - From there, you can find the right accommodation for each person's needs.")
   st.markdown('---')
   st.markdown('### 📌 **For chosen district, price analysis by street** ')
   grouped = df_filter.groupby('street')
   ward_mean = grouped['price'].mean()
   df_ward = pd.DataFrame(ward_mean)
   df_ward = df_ward.sort_values(by='price', ascending=True)
   top_10_ward = df_ward.head(10)
   # visualize top 10 ward with barh chart
   fig, ax = plt.subplots()
   fig.set_size_inches(10, 5)
   ax.barh(top_10_ward.index, top_10_ward['price'])
   ax.set_title('Top 10 streets with the cheapest price in the district you have chosen')
   ax.set_xlabel('Price')
   ax.set_ylabel('Street')
   st.pyplot(fig)
   st.markdown('##### &#9889; <font color="yellow"><b>Comment</b></font>', unsafe_allow_html=True)
   st.markdown('>   - The chart above shows the top 10 streets with the cheapest price in the district you have chosen.')
   st.markdown('>   - Helps tenants find addresses with rents that fit their budget because statistics by street in the district help tenants have a more intuitive view.')
   st.markdown('---')
   tab_sections.make_tab_sections(3)


def question_five(df_house_rent):
   st.markdown(list_questions[4], unsafe_allow_html=True)
   st.markdown('---')
   
   st.subheader('**📌Get the last 5 years and group by acreage and get the lowest price for each year**')
   
   df_house_rent['year'] = pd.DatetimeIndex(df_house_rent['published']).year
   df_house_rent['year'] = df_house_rent[df_house_rent['year'] > 2017]['year'].astype(int)

   # group by acreage and get the lowest price for each year > 2017
   grouped = df_house_rent.groupby(['acreage', 'year'])
   df2 = grouped['price'].min().reset_index()
   st.dataframe(df2)
   
   st.markdown('### ✨ **Create a new dataframe and calculate mean price per squared meter**')
   df_acreage = pd.DataFrame(grouped['price'].min())
   df_acreage = df_acreage.unstack(level=1)
   df_acreage = df_acreage.sort_index(ascending=True)
   df_acreage['min_price'] = df_acreage.min(axis=1)
   df_acreage = df_acreage.sort_values(by='acreage', ascending=True)
   df_acreage.head(30)

   # Name the columns
   df_acreage.columns = ['2018', '2019', '2020','2021','2022', 'min_price']

   # mean of min price per acreage
   st.markdown('Mean of min price per acreage')
   df_acreage['mean_per_acreage'] = round(df_acreage['min_price'] / df_acreage.index, 0)
   st.dataframe(df_acreage.tail(30))
   
   st.markdown('### ✨ **Outlier**')
   outlier = df_acreage[df_acreage['mean_per_acreage'] < 10000]
   st.dataframe(outlier)
   
   st.markdown('---')
   tab_sections.make_tab_sections(4)