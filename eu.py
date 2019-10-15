#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import time
import random 
import xlrd
import pandas as pd
import numpy as np
import re


# In[2]:


index= list(range(1, 645, 1))


# In[3]:


url= ["https://www.clinicaltrialsregister.eu/ctr-search/search?query=&resultsstatus=trials-with-results&page"+str(i)for i in index]


# In[4]:


d = {'number': index, 'url': url}


# In[5]:


df = pd.DataFrame(data=d)


# In[10]:


for a in df['url']:
    bh=[]
    r9= requests.get(a)
    p9 = BeautifulSoup(r9.text, 'html.parser')
    for g in p9.find_all(href= re.compile('/ctr-search/trial/')):
        kl=[]
        kl.append((str(g)))
    for e in kl:
        oi= []
        oi.append((str(''.join(re.findall('/ctr-search/trial/.*[A-Z]{2}"', e)))).replace('"', ''))
    for x in oi:
        lm= []
        if len(x)> 6:
            lm.append('https://www.clinicaltrialsregister.eu'+ str(x))
    bh.extend(lm)


# In[ ]:


df2 = pd.DataFrame(np.array(bh), columns=['all'])


# In[ ]:


def scrape(url):
    r1= requests.get(url)
    p1 = BeautifulSoup(r1.text, 'html.parser')
    result= [(str(td.text)).splitlines() for td in p1.find_all("td", "third", limit=7)]
    return result
    


# In[ ]:


import multiprocessing as mp


# In[9]:


from multiprocessing.dummy import Pool as ThreadPool


# In[10]:


pool = ThreadPool(mp.cpu_count())


# In[11]:


io= df2.all.tolist()


# In[ ]:


results = pool.map(scrape, io)
df3 = pd.DataFrame(np.array(results), columns=['data'])
pool.close()
pool.join()


# In[ ]:


df3= df2.merge(df3, how='outer', left_index= True, right_index= True)


# In[ ]:


df3.to_excel('eu123.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




