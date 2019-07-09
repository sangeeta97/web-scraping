#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import re


# In[2]:


r1= requests.get('https://clinicaltrials.gov/ct2/show/record/NCT00885170?term=NCT00885170&rank=1&view=record')


# In[ ]:


soup1= BeautifulSoup(r1.text, 'html.parser')


# In[ ]:


soup17= soup1.body.contents[17]


# In[ ]:


len(list(soup17.descendants))


# In[ ]:


for string in soup1.stripped_strings:
    print(repr(string))


# In[ ]:


km= [text for text in soup1.stripped_strings]


# In[ ]:


soup1.find_all(string=re.compile("(?sm)(Intervention\r\nICMJE)"))


# In[ ]:


len(list(soup17.children))


# In[ ]:


markup = '<div class="tr-indent2" style="margin-top:0.5ex">Topical VBP-926 solution</div>'


# In[ ]:


soup = BeautifulSoup(markup)


# In[ ]:


th_tag = soup.div


# In[ ]:


i_tag = soup.div.extract()

