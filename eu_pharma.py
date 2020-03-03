#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


# In[3]:


url= "https://www.clinicaltrialsregister.eu/ctr-search/trial/2006-005668-21/GB"


# In[6]:


r= requests.get(url, verify=False)


# In[ ]:


soup = BeautifulSoup(r.text, 'lxml')
io= re.compile("E.6.12</td><td\W.*\W.*")
for tr in (soup.find_all('table')[12]).find_all("tr", "tricell"):
    if not re.search(io, str(tr))== None:
        return tr.text


# In[7]:


soup = BeautifulSoup(r.text, 'lxml')


# In[89]:


import re


# In[120]:


io= re.compile("E.6.12</td><td\W.*\W.*")


# In[123]:


for tr in (soup.find_all('table')[12]).find_all("tr", "tricell"):
    if not re.search(io, str(tr))== None:
        print(tr.text)


# In[ ]:





# In[ ]:





# In[ ]:




