#!/usr/bin/env python
# coding: utf-8

# ### <center>📜 **<font color="cyan">Question 5:</font> Is it true that the more houses in the area, the higher the price?** </center>

# #### 📙**Import the necessary libraries**

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('../data/processed/VN_housing_dataset.csv')
df.drop(columns=['date','address'], inplace=True)
df


# In[24]:


grouped = df.groupby('district').agg({'price': ['mean', 'min', 'max', 'count'], }).reset_index()
grouped


# In[26]:


grouped.columns = ['district', 'mean_price', 'min_price', 'max_price', 'count']


# In[33]:


grouped.sort_values("count", ascending=True).plot.barh(x='district', y='count', figsize=(20, 10))


# In[34]:


grouped.sort_values("count", ascending=True).plot.barh(x='district', y='mean_price', figsize=(20, 10))


# #### Conclusion
# - As can be seen, The mean of the price fluctuate without any pattern when we sort by number of house. In other words, the price of the house is uncertain and not depend on whether it is a dense house area or not.
