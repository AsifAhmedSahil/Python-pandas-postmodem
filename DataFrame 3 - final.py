#!/usr/bin/env python
# coding: utf-8

# # DataFrame - 3 (final)

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#index level
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[3]:


hier_index


# In[4]:


inside


# In[5]:


from numpy.random import randn 


# In[6]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[7]:


df


# In[8]:


df.index.names=['Groups','Num']


# In[9]:


df


# In[12]:


df.loc['G2'].loc[2]['B']


# In[13]:


# advanced cross section method***


# In[14]:


df.xs(1,level='Num')


# In[ ]:




