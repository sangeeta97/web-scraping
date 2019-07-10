#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import random 
import xlrd


# In[2]:


import json


# In[15]:


dfv= pd.read_excel('mk1.xlsx')


# In[17]:


dfv['url']= ["http://ctri.nic.in/Clinicaltrials/pmaindet2.php?trialid="+str(i)+"&EncHid=&userName=CTRI" for i in dfv.number]


# In[19]:


def ctri(url):
    aw= []
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.find('table', border="0", cellpadding="2")
        
        time.sleep(2)
        aw.append((':%').join([str((pd.read_html(str(table))[2]).to_dict('records')[0][1]), str((pd.read_html(str(table))[2]).to_dict('records')[5][1]), str((pd.read_html(str(table))[2]).to_dict('records')[6][1]), str((pd.read_html(str(table))[2]).to_dict('records')[7][1]), str((pd.read_html(str(table))[2]).to_dict('records')[15][1]), str((pd.read_html(str(table))[2]).to_dict('records')[28][1]), str((pd.read_html(str(table))[2]).to_dict('records')[29][1]), str((pd.read_html(str(table))[2]).to_dict('records')[3][1]), str((pd.read_html(str(table))[8]).to_dict('records')[0][1]), str((pd.read_html(str(table))[7]).to_dict('records')[0:]), str((pd.read_html(str(table))[13]).to_dict('records')[1][1]), str((pd.read_html(str(table))[14]).to_dict('records')[0:]), str((pd.read_html(str(table))[17]).to_dict('records')[1])])) 
        
        
        
    except:
        pass
        
        
    finally:
        return aw


# In[ ]:


dfv['all'] = dfv.url.map(ctri)


# In[ ]:


dfv.to_excel('results_5july.xlsx')


# In[ ]:





# In[ ]:




