#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import string
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[56]:


import xlrd


# In[2]:


def tokenize2(text_series):
          
      
    sw = stopwords.words('english')
    
    return  [word for word in text_series.split() if word not in sw]


# In[3]:


jj= pd.read_excel('ctri_27june.xlsx')


# In[6]:


jj.columns


# In[8]:


ak= jj[['study_design', 'scientific_title', 'sponsor_1', 'sponsor_2', 'condition', 'intervention', 'primary_outcome', 'ctri_id']]


# In[9]:


ak.set_index('ctri_id', inplace= True)


# In[33]:


ak['all']= ak.astype(str).apply(lambda x: ','.join(x), axis= 1)


# In[24]:


ak['m1']= ak['all'].map(tokenize2).values


# In[25]:


df11= pd.read_excel('nct_real.xlsx')


# In[ ]:


ka= df11[['nct_no', 'Study_Designs_ct', 'Title', 'sponsor_ct', 'conditions_ct', 'intervention_ct', 'primary_outcome_final']]


# In[29]:


ka.set_index('nct_no', inplace= True)


# In[32]:


ka['all']= ka.astype(str).apply(lambda x: ','.join(x), axis= 1)


# In[34]:


ka['m1']= ka['all'].map(tokenize2).values


# In[41]:


def score1(text):
    text= process.extract(text, ak.m1, scorer= fuzz.token_set_ratio)[0:3]
    score= []
    for i in text:
        score.append(i[1])
        
   
    return score


# In[42]:


def score2(text):
    text= process.extract(text, ak.m1, scorer= fuzz.token_set_ratio)[0:3]
    score= []
    for i in text:
        score.append(i[0])

    
    return score
    


# In[48]:


import multiprocessing as mp


# In[49]:


from multiprocessing.dummy import Pool as ThreadPool


# In[50]:


pool = ThreadPool(mp.cpu_count())


# In[55]:


io10= ka['m1'].astype(str).tolist()


# In[52]:


results1 = pool.map(score2, io10)


# In[ ]:


results2 = pool.map(score1, io10)


# In[ ]:


ka['text']= results1


# In[ ]:


ka['match']= results2


# In[ ]:


ka.to_excel('old_27june.xlsx')


# In[ ]:


ak.to_excel('new_27june.xlsx')


# In[ ]:




