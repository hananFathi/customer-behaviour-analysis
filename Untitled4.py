#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


filepath=r"C:\Users\hanan\Downloads\csv-files\ecommerce_customer_data.csv"
data=pd.read_csv(filepath)
data


# In[4]:


grouped=data.groupby('Gender')
data


# In[19]:


purchase=grouped['Total_Purchases'].sum()
purchase


# In[15]:


grrouped=data.groupby('Age')
purchase=grrouped['Total_Purchases'].sum()
purchase


# In[37]:


grrrouped=data.groupby(['Gender','Age','Location'])
purchase=grrrouped['Total_Purchases'].sum()
purchase


# In[ ]:


people of age 21-22 purchase the most and they are male.Feamles viewing the website and purchasing is much lesser male


# In[ ]:




