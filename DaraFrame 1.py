#!/usr/bin/env python
# coding: utf-8

# # DataFrame 1

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


from numpy.random import randn


# In[5]:


np.random.seed(101)


# In[9]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[10]:


df


# In[11]:


df['W']


# In[13]:


type(df['W'])


# In[14]:


type(df)


# In[15]:


df[['W','X']]


# In[16]:


type(df[['W','X']])


# In[17]:


df['new'] = df["W"]+df["Y"]


# In[18]:


df


# In[20]:


df.drop("new",axis=1)


# In[21]:


df.drop('E',axis = 0)


# In[22]:


#azis means holo shape dile tupple ashe [5,4] mane axis 0 == 5 && axis 1 = 4


# In[23]:


df.shape


# In[24]:


df


# In[25]:


#Row ber kora jai 2 ways e


# In[26]:


df.loc['C']


# In[27]:


df.iloc[2]


# In[28]:


df.loc['B','Y']


# In[29]:


df.loc[['A','B'],['X','Y']]


# In[ ]:




