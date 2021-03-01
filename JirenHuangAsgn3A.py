#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


tables = pd.read_html('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield')


# In[4]:




# In[9]:


df = tables[1]


# In[15]:


df = df.set_index('Date')



# In[55]:


tyr = list(df['30 yr'])


# In[56]:



# In[45]:


time = list(df.index)


# In[48]:


date = []


# In[49]:


for i in time:
    x = i[0:5]
    date.append(x)


# In[50]:




# In[52]:


plt.scatter(date,tyr,c='blue')
plt.show()


# In[58]:


fyr = list(df['1 yr'])
syr = list(df['2 yr'])


# In[59]:


plt.scatter(date,fyr,c='blue')
plt.show()


# In[60]:


plt.scatter(date,syr,c='blue')
plt.show()

