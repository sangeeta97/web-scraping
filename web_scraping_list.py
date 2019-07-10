#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re


# In[2]:


def tt(url):
    try:
        r= requests.get(url)
        soup= BeautifulSoup(r.text, 'lxml')
        bb= [text for text in soup.stripped_strings]
        bb= bb[bb.index('Brief Title'): bb.index('Official Title')]
        
    except:
        pass
    finally:
        return bb


# In[ ]:


df.assign('text'= df.map(tt))

