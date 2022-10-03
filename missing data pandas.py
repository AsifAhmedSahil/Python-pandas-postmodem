#!/usr/bin/env python
# coding: utf-8

# # Pandas - missing data

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn 


# In[3]:


d = {"A":[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,2,3]}


# In[4]:


d


# In[5]:


df = pd.DataFrame(d)


# In[6]:


df


# In[7]:


df.fillna(value = 'Fill')


# In[8]:


df['A'].fillna(value = df["A"].mean())


# In[ ]:




