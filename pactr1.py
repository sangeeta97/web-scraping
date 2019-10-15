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


index= list(range(86, 10000, 1))


# In[3]:


url= ["https://pactr.samrc.ac.za/TrialDisplay.aspx?TrialID="+str(i)for i in index]


# In[4]:


d = {'number': index, 'url': url}


# In[5]:


df = pd.DataFrame(data=d)




# In[ ]:


def text1(url):
    aw= []
    try:
        r = requests.get(url, verify = False)
        soup = BeautifulSoup(r.text, 'lxml')
        pt= (page_html1.find_all('table')[2]).find_all('td')[2].get_text()
        p1= (soup.find_all('table')[2]).find_all('td')[9].get_text()
        s1= (page_html1.find_all('table')[2]).find_all('td')[11].get_text()
        
        n1= [str(td.text) for td in (soup.find_all('table')[4]).find_all('td')]
        time.sleep(2)
        aw.append(pt, p1, s1, str(n1))
        
    except:
        aw.append('no_value')
        
    finally:
        
        return aw


# In[ ]:


import multiprocessing as mp


# In[9]:


from multiprocessing.dummy import Pool as ThreadPool


# In[10]:


pool = ThreadPool(mp.cpu_count())


# In[11]:


io= df.url.tolist()


# In[ ]:


results = pool.map(text1, io)
df2 = pd.DataFrame(np.array(results), columns=['all'])
pool.close()
pool.join()


# In[ ]:


df2= df.merge(df2, how='outer', left_index= True, right_index= True)


# In[ ]:


df2.to_excel('pac_28sept.xlsx')



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




