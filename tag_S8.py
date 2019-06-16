#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from lxml import html


# In[4]:


import requests


# In[16]:


def scrape_responsible(url):
    buyers= []
    page = requests.get(url)
    tree = html.fromstring(page.content)
    buyers.extend(tree.xpath('//*[@id="responsibleparty"]/text()'))
    
    return buyers


# In[17]:


def scrape_sponsor(url):
    buyers= []
    page = requests.get(url)
    tree = html.fromstring(page.content)
    buyers.extend(tree.xpath('//*[@id="sponsor"]/text()'))
    
    return buyers


# In[8]:


combined= pd.read_csv('combined.csv')


# In[ ]:


combined['responsible_party']= combined.urllist.map(scrape_responsible)


# In[ ]:


combined['sponsor']= combined.urllist.map(scrape_sponsor)


# In[ ]:


combined.to_csv('combined_1.csv')

