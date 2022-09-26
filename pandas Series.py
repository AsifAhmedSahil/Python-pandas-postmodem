#!/usr/bin/env python
# coding: utf-8

# # pandas
# 

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[6]:


labels = ['a','b','c']
my_list = [1,2,3]
arr = np.array(my_list)
d = {'a':10,'b':20,'c':30}

d
# In[8]:


labels


# In[9]:


pd.Series(my_list)


# In[10]:


pd.Series(my_list,labels)


# In[11]:


pd.Series(arr,labels)


# In[12]:


ser1 = pd.Series([1,2,3],['USA','Japan','Germany'])


# In[13]:


ser1


# In[14]:


ser2 = pd.Series([1,5,3],['USA','Japan','Germany'])


# In[15]:


ser2


# In[16]:


ser2['USA']


# In[17]:


ser3 = pd.Series(data = labels)


# In[18]:


ser3


# In[19]:


ser3[0]


# In[20]:


ser1+ser2


# In[ ]:




