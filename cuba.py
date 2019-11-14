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


index= list(range(1, 304, 1))


# In[3]:


index= [(str(i)).zfill(3) for i in index]


# In[4]:


url= ["http://registroclinico.sld.cu/en/trials/RPCEC00000" + str(i)+ "-En" for i in index]


# In[5]:


d = {'number': index, 'url': url}


# In[6]:


df = pd.DataFrame(data=d)


# In[49]:


public_title, scientific_title, primary_sponsor, source_monetary, sec_id, sec_id_add, registration_date, intervention, condition, status, country, inclusion, outcome, exclusion, study_type, allocation, reg_id, completion_date, sample_size, phase = list(range(20))


# In[51]:


def text1(url):
    global public_title, scientific_title, primary_sponsor, source_monetary, sec_id, sec_id_add, registration_date, intervention, condition, status, country, inclusion, outcome, exclusion, study_type, allocation, reg_id, completion_date, sample_size, phase
        
    try:
       
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        jp= [k for k in soup.stripped_strings]
        
        public_title= jp[jp.index('Scientific title:')-2: jp.index('Scientific title:')]
        scientific_title= jp[jp.index('Scientific title:'): jp.index('Scientific title:')+4]
        
        primary_sponsor= jp[jp.index('Primary sponsor:'): jp.index('Secondary sponsor:')]
        source_monetary= jp[jp.index('Source(s) of monetary or material support:'): jp.index('Authorization for beginning')]
        sec_id= jp[jp.index('Secondary indentifying numbers:'): jp.index('Issuing authority of the secondary identifying numbers:')]

        sec_id_add= jp[jp.index('Issuing authority of the secondary identifying numbers:'): jp.index('Primary sponsor:')]
        registration_date= jp[jp.index('Date of Registration in Primary Registry:'): jp.index('Record Verification Date:')]
        intervention= jp[jp.index('Intervention(s):'): jp.index('Intervention code:')]
        condition= jp[jp.index('Health condition(s) or Problem(s) studied:'): jp.index('Health condition(s) code:')]
        status= jp[jp.index('Recruitment status:'): jp.index('Date of first enrollment:')]
        country= jp[jp.index('Countries of recruitment:'): jp.index('Clinical sites:')]
        inclusion= jp[jp.index('Inclusion criteria:'): jp.index('Exclusion criteria:')]
        outcome= jp[jp.index('Primary outcome(s):'): jp.index('Key secondary outcomes:')]
        exclusion= jp[jp.index('Exclusion criteria:'): jp.index('Type of population:')]
        study_type= jp[jp.index('Type study:'): jp.index('Purpose:')]
        allocation= jp[jp.index('Allocation:'): jp.index('Phase:')]
        reg_id= jp[jp.index('Unique ID number:'): jp.index('Date of Registration in Primary Registry:')]
        completion_date= jp[jp.index('Study completion date:'): jp.index('Date of available results:')]
        
        sample_size= jp[jp.index('Target sample size:'): jp.index('Contact for public queries')]
        phase= jp[jp.index('Phase:'): jp.index('Target sample size:')]
        
        
    except ValueError as e:
        print(e)
        pass
        
    
    return public_title, scientific_title, primary_sponsor, source_monetary, sec_id, sec_id_add, registration_date, intervention, condition, status, country, inclusion, outcome, exclusion, study_type, allocation, reg_id, completion_date, sample_size, phase 
        
   


# In[52]:


df['data']= df['url'].map(text1)


# In[ ]:


df.to_excel('cuba.xlsx')

