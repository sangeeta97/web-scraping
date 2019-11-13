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


# In[199]:


index= list(range(1, 2719, 1))


# In[200]:


url= ["http://www.chictr.org.cn/searchprojen.aspx?title=&officialname=&subjectid=&secondaryid=&applier=&studyleader=&ethicalcommitteesanction=&sponsor=&studyailment=&studyailmentcode=&studytype=0&studystage=0&studydesign=0&minstudyexecutetime=&maxstudyexecutetime=&recruitmentstatus=0&gender=0&agreetosign=&secsponsor=&regno=&regstatus=0&country=&province=&city=&institution=&institutionlevel=&measure=&intercode=&sourceofspends=&createyear=0&isuploadrf=&whetherpublic=&btngo=btn&verifycode=&page="+ str(i) for i in index]


# In[201]:


d = {'number': index, 'url': url}


# In[202]:


df = pd.DataFrame(data=d)


# In[210]:


def get_url(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    q1= [(str(k)).split('>')[0] for k in soup.find_all(href= re.compile('^showprojen'))]
    q1= [(x.split('=', 1)[-1]).strip('"') for x in q1]
    q1= ['http://www.chictr.org.cn/'+ str(x) for x in q1]
        
    return q1


# In[217]:


def newlist():
    io= []
    df['yu']= df['url'].map(get_url)
    ij= df['yu'].values.flatten()
    for p in ij:
        for u in p:
            io.append(u)
        
     
    return io


# In[ ]:


lk= pd.DataFrame(newlist())


# In[159]:


from time import sleep
from random import randint
from time import time
start_time = time()
from IPython.core.display import clear_output
from warnings import warn


# In[185]:


def cc(url):
    start_time = time()
    quests = 0
    for page in range(3):
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")
        sleep(randint(2,8))
        quests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(quests, quests/elapsed_time))
        clear_output(wait = True)
        
        if html.status_code != 200:
            warn('Request: {}; Status code: {}'.format(quests, html.status_code))

        # Break the loop if the number of requests is greater than expected
        if quests > 72:
            warn('Number of requests was greater than expected.')
            break
            
        try:
                               
            number= [td.text.strip() for td in (soup.find_all('table')[0]).find_all('td')][1]
            Date_of_Registration = [td.text.strip() for td in (soup.find_all('table')[0]).find_all('td')][5]
            Registration_Status = [td.text.strip() for td in (soup.find_all('table')[0]).find_all('td')][9]
            j1= [td.text.strip() for td in (soup.find_all('table')[0]).find_all('td')]
            public_title = j1[j1.index('Public title：'): j1.index('Scientific title：')][1]
            scititle = j1[j1.index('Public title：'): (j1.index('Scientific title：'))+2][-1]
            sec_id = j1[j1.index('Public title：'): (j1.index('Scientific title：'))+6][-1]
            j2= [td.text.strip() for td in (soup.find_all('table')[3]).find_all('td')]
            primary_sponsor = j2[j2.index('Primary sponsor：'): (j2.index('Primary sponsor\'s address：')+2)][1]
            primary_sponsor_address = j2[j2.index('Primary sponsor：'): (j2.index('Primary sponsor\'s address：')+2)][5]
            source_of_funding = j2[j2.index('Source(s) of funding：'): (j2.index('Target disease：'))][1]
            condition = j2[j2.index('Target disease：'): (j2.index('Target disease code：'))][1]
            study_type = j2[j2.index('Study type：'): (j2.index('Study phase：'))][1]
            study_phase = j2[j2.index('Study phase：'): (j2.index('Study phase：')+2)][1]
            study_objective = j2[j2.index('Objectives of Study：'): (j2.index('Objectives of Study：')+2)][1]
            study_design = j2[j2.index('Study design：'): (j2.index('Study design：')+2)][1]
            inclusion = j2[(j2.index('Exclusion criteria：'))-2: (j2.index('Exclusion criteria：'))][0]
            exclusion_criteria = j2[j2.index('Exclusion criteria：'): (j2.index('Exclusion criteria：')+2)][1]
            study_period = j2[j2.index('Exclusion criteria：'): (j2.index('Exclusion criteria：')+5)][-1]
            intervention_group = [td.text.strip() for td in (soup.find_all('table')[6]).find_all('td')]
            control_group = [td.text.strip() for td in (soup.find_all('table')[7]).find_all('td')]
            sample_intervention = intervention_group[3]
            intervention_type = intervention_group[-2]
            control_intervention = control_group[3]
            control_type = control_group[-2]
            tk= [td.text.strip() for td in (soup.find_all('table')[8]).find_all('td')]
            t= [re.findall('(\w+)', t) for t in tk]
            country = [re.findall(r'(Country\W+[A-Za-z]+)', str(m[1])) for m in tk]
            sk= soup.text.strip()
            recruitment_status = re.findall('[A-Za-z]+', sk[sk.index('Recruiting status：'): sk.index('Participant age：')])
        
      
        except:
            
            pass
        
            
        
        
    return number, Date_of_Registration, Registration_Status, public_title, scititle, sec_id, primary_sponsor, primary_sponsor_address, source_of_funding, condition, study_type, study_phase, study_objective, study_design, inclusion, exclusion_criteria, study_period, intervention_group, control_group, sample_intervention, intervention_type, control_intervention, control_type, t, country, recruitment_status 


# In[ ]:


import concurrent.futures


# In[ ]:


from concurrent.futures import ThreadPoolExecutor
import threading
import random


# In[ ]:


def download_many():
    
    with ThreadPoolExecutor(max_workers=5) as executor:  
        result= executor.map(cc, lk[0].tolist())
        return result


# In[ ]:


def data():
    
    lk['data_new']= download_many()
    gf= lk[['data_new']]
    gf= gf.stack().apply(pd.Series).unstack()
    return gf


# In[191]:


pm= data()


# In[ ]:


pm.to_excel('chi.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




