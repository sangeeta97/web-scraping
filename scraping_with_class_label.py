#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re





# In[8]:


def tt(url):
    try:
        r= requests.get(url)
        soup= BeautifulSoup(r.text, 'lxml')
        bb= [text for text in soup.stripped_strings]
        bb= bb[bb.index('Intervention'): bb.index('Study Arms')]
        bb= bb.text.strip()
        
    except:
        pass
    finally:
        return bb


# In[ ]:


html(/body/div[3]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody/tr[3]/td[4])


# In[ ]:


def cc(url):
    html = requests.get(b).text
    soup = BeautifulSoup(html, "html.parser")
#identify table we want to scrape
   officer_table = soup.find('table', {"class" : "dataTable"})

#try clause to skip any companies with missing/empty board member tables
try:
#loop through table, grab each of the 4 columns shown (try one of the links yourself to see the layout)
    for row in officer_table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 3:
            board_members.append((b, cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(), cols[3].text.strip()))
except: pass  


# In[95]:


kb= []


# In[198]:


def ctri(url):
    pk= []
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    officer_table = soup.find('table')
    
    try:
        for row in officer_table.find_all('tr'):
            cols = row.find_all('td')
            for col in cols:
                pk.append(col.text.strip())
                
            
            
            
            
    except:
            pass
    finally:
            return pk
            
        


# In[9]:


url= 'https://clinicaltrials.gov/ct2/show/record/NCT00128102?view=record'


# In[10]:


tt(url)


# In[ ]:




