#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


import random 


# In[4]:


from random import sample


# In[5]:


import re


# In[6]:


df2= pd.read_csv('S8nested6feb.csv')


# In[7]:


df1= pd.read_csv('sk_S116feb19.csv')


# In[8]:


s8= list(df2.nct_id.values)


# In[9]:


s8random= sample(s8, 211)


# In[10]:


s11= list(df1.nct_id.values)


# In[11]:


s11random= sample(s11, 422)


# In[12]:


total8= pd.DataFrame(s8random)


# In[13]:


total8.columns= ['nct_id']


# In[14]:


total11= pd.DataFrame(s11random)


# In[15]:


total11.columns= ['nct_id']


# In[16]:


total8['urllist']= ["https://clinicaltrials.gov/ct2/history/"+str(i)+"?V_1=View#StudyPageTop" for i in total8.nct_id]


# In[17]:


total11['urllist']= ["https://clinicaltrials.gov/ct2/history/"+str(i)+"?V_1=View#StudyPageTop" for i in total11.nct_id]


# In[18]:


def get_number(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    nl= soup.find_all(href=re.compile("\?V\_"))
    return len(nl)


# In[19]:


total8['number']= total8.urllist.map(get_number)


# In[20]:


total8['num6']= total8.number.map(lambda x: list(range(1, x+1)))


# In[21]:


nw= list(total8.nct_id*total8.number)


# In[22]:


gg= pd.DataFrame(nw, total8.num6)


# In[23]:


gg.reset_index(inplace= True)


# In[24]:


gg.columns= ['first', 'second']


# In[25]:


gg['second']= gg.second.map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))


# In[26]:


gg['second']= gg.second.str.split(',')


# In[27]:


newgg= gg.stack().apply(pd.Series).stack().unstack(1)


# In[28]:


newgg['ff']= list(zip(newgg['first'].astype(str), newgg['second'].astype(str)))


# In[29]:


newgg['nurl']= ["https://clinicaltrials.gov/ct2/history/"+i[1]+"?V_"+i[0]+"=View#StudyPageTop" for i in newgg.ff]


# In[ ]:


def scrape_PI(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    h1 = soup.findAll('div',attrs={"id":"ContactsLocationsBody"})
    title= soup.title
    result = []
    
    for th in h1:
        result.extend(th.find_all('td'))
        result = [ele.text.strip() for ele in result]
        return result[1]


# In[ ]:


newgg['History_Contacts']= newgg.nurl.astype(str).map(lambda x: scrape_PI(x))


# In[ ]:


newgg.to_csv('S8_07.csv')


# In[ ]:


total11['number']= total11.urllist.map(get_number)


# In[ ]:


total11['num6']= total11.number.map(lambda x: list(range(1, x+1)))


# In[ ]:


n11= list(total11.nct_id*total11.number)


# In[ ]:


g11= pd.DataFrame(n11, total11.num6)


# In[ ]:


g11.reset_index(inplace= True)


# In[ ]:


g11.columns= ['first', 'second']


# In[ ]:


g11['second']= g11.second.map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))


# In[ ]:


g11['second']= g11.second.str.split(',')


# In[ ]:


newg11= g11.stack().apply(pd.Series).stack().unstack(1)


# In[ ]:


newg11['ff']= list(zip(newg11['first'].astype(str), newg11['second'].astype(str)))


# In[ ]:


newg11['nurl']= ["https://clinicaltrials.gov/ct2/history/"+i[1]+"?V_"+i[0]+"=View#StudyPageTop" for i in newg11.ff]


# In[ ]:


newg11['History_Contacts']= newg11.nurl.astype(str).map(lambda x: scrape_PI(x))


# In[ ]:


newg11.to_csv('S11_07.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




