#!/usr/bin/env python
# coding: utf-8

# # DataFrame - 2

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from numpy.random import randn 


# In[4]:


np.random.seed(101)


# In[5]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[6]:


df


# In[7]:


#logic in data frame


# In[8]:


df > 0


# In[9]:


df[df>0]


# In[10]:


df['W']


# In[12]:


df["W"] > 0


# In[13]:


df[df['W']>0][['Y','X']]


# In[16]:


boolser = df["W"]>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]


# In[15]:


boolser


# In[17]:


# can not use python and operator , you can use & ****


# In[18]:


df[(df['Y']>0) & (df['W']>1)]


# In[19]:


df[(df['Y']>0) | (df['W']>1)]


# In[20]:


df.reset_index()


# In[21]:


newind = 'CA NT WY OR CO'.split()


# In[22]:


newind


# In[23]:


df['state'] = newind


# In[24]:


df


# In[25]:


df.set_index('state')


# In[ ]:




