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


index= list(range(1, 34000, 1))


# In[3]:


url= ["http://ctri.nic.in/Clinicaltrials/pmaindet2.php?trialid="+str(i)+"&EncHid=&userName=CTRI" for i in index]


# In[4]:


d = {'number': index, 'url': url}


# In[5]:


df = pd.DataFrame(data=d)


# In[6]:


lk= re.compile(r'\\[nrt]')


# In[7]:


def text1(url):
    aw= []
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'xml')
        table = soup.find('table')
        aa= re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', table.text)
        aa= lk.sub(' ', str(aa))
        bb= re.findall(r'(?sm)(?<=Last Modified On:)[^A-Za-z]*(\w+\W+.*)(?=Post Graduate Thesis)', table.text)
        bb= lk.sub(' ', str(bb))
        cc= re.findall(r'(?sm)(?<=Post Graduate Thesis)[^A-Za-z]*(\w+\W+.*)(?=Type of Trial)', table.text)
        cc= lk.sub(' ', str(cc))
        dd= re.findall(r'(?sm)(?<=Type of Trial)[^A-Za-z]*(\w+\W+.*)(?=Type of Study)', table.text)
        dd= lk.sub(' ', str(dd))
        ee= re.findall(r'(?sm)(?<=Type of Study)[^A-Za-z]*(\w+\W+.*)(?=Study Design)', table.text)
        ee= lk.sub(' ', str(ee))
        ff= re.findall(r'(?sm)(?<=Study Design)[^A-Za-z]*(\w+\W+.*)(?=Public Title of Study)', table.text)
        ff= lk.sub(' ', str(ff))
        gg= re.findall(r'(?sm)(?<=Public Title of Study)[^A-Za-z]*(\w+\W+.*)(?=Scientific Title of Study)', table.text)
        gg= lk.sub(' ', str(gg))
        hh= re.findall(r'(?sm)(?<=Scientific Title of Study)[^A-Za-z]*(\w+\W+.*)(?=Secondary IDs if Any)', table.text)
        hh= lk.sub(' ', str(hh))
        ii= re.findall(r'(?sm)(?<=Secondary IDs if Any)[^A-Za-z]*(\w+\W+.*)(?=Details of Principal Investigator)', table.text)
        ii= lk.sub(' ', str(ii))
        jj= re.findall(r'(?sm)(?<=Secondary IDs if Any)[^A-Za-z]*(\w+\W+.*)(?=Details of Principal Investigator)', table.text)
        jj= lk.sub(' ', str(jj))
        kk= re.findall(r'(?sm)(?<=Details of Principal Investigator)[^A-Za-z]*(\w+\W+.*)(?=Scientific Query)', table.text)
        kk= lk.sub(' ', str(kk))
        ll= re.findall(r'(?sm)(?<=Public Query)[^A-Za-z]*(\w+\W+.*)(?=Source of Monetary or Material Support)', table.text)
        ll= lk.sub(' ', str(ll))
        mm= re.findall(r'(?sm)(?<=Source of Monetary or Material Support)[^A-Za-z]*(\w+\W+.*)(?=Primary Sponsor)', table.text)
        mm= lk.sub(' ', str(mm))
        nn= re.findall(r'(?sm)(?<=Primary Sponsor)[^A-Za-z]*(\w+\W+.*)(?=Details of Secondary Sponsor)', table.text)
        nn= lk.sub(' ', str(nn))
        oo= re.findall(r'(?sm)(?<=Details of Secondary Sponsor)[^A-Za-z]*(\w+\W+.*)(?=Countries of Recruitment)', table.text)
        oo= lk.sub(' ', str(oo))
        pp= re.findall(r'(?sm)(?<=Countries of Recruitment)[^A-Za-z]*(\w+\W+.*)(?=Sites of Study)', table.text)
        pp= lk.sub(' ', str(pp))
        qq= re.findall(r'(?sm)(?<=Sites of Study)[^A-Za-z]*(\w+\W+.*)(?=Details of Ethics Committee)', table.text)
        qq= lk.sub(' ', str(qq))
        rr= re.findall(r'(?sm)(?<=Details of Ethics Committee)[^A-Za-z]*(\w+\W+.*)(?=Regulatory Clearance Status from DCGI)', table.text)
        rr= lk.sub(' ', str(rr))
        ss= re.findall(r'(?sm)(?<=Regulatory Clearance Status from DCGI)[^A-Za-z]*(\w+\W+.*)(?=Health Condition / Problems Studied)', table.text)
        ss= lk.sub(' ', str(ss))
        tt= re.findall(r'(?sm)(?<=Regulatory Clearance Status from DCGI)[^A-Za-z]*(\w+\W+.*)(?=Health Condition / Problems Studied)', table.text)
        tt= lk.sub(' ', str(tt))
        uu= re.findall(r'(?sm)(?<=Health Type)[^A-Za-z]*(\w+\W+.*)(?=Intervention / Comparator Agent)', table.text)
        uu= lk.sub(' ', str(uu))
        vv= re.findall(r'(?sm)(?<=Comparator Agent)[^A-Za-z]*(\w+\W+.*)(?=Comparator Agent)', table.text)
        vv= lk.sub(' ', str(vv))
        ww= re.findall(r'(?sm)(?<=Comparator Agent)[^A-Za-z]*(\w+\W+.*)(?=Inclusion Criteria)', table.text)
        ww= lk.sub(' ', str(ww))
        xx= re.findall(r'(?sm)(?<=Inclusion Criteria)[^A-Za-z]*(\w+\W+.*)(?=ExclusionCriteria)', table.text)
        xx= lk.sub(' ', str(xx))
        yy= re.findall(r'(?sm)(?<=ExclusionCriteria)[^A-Za-z]*(\w+\W+.*)(?=Method of Generating Random Sequence)', table.text)
        yy= lk.sub(' ', str(yy))
        zz= re.findall(r'(?sm)(?<=Method of Generating Random Sequence)[^A-Za-z]*(\w+\W+.*)(?=Method of Concealment)', table.text)
        zz= lk.sub(' ', str(zz))
        ab= re.findall(r'(?sm)(?<=Method of Concealment)[^A-Za-z]*(\w+\W+.*)(?=Blinding/Masking)', table.text)
        ab= lk.sub(' ', str(ab))
        ac= re.findall(r'(?sm)(?<=Blinding/Masking)[^A-Za-z]*(\w+\W+.*)(?=Primary Outcome)', table.text)
        ac= lk.sub(' ', str(ac))
        ad= re.findall(r'(?sm)(?<=Primary Outcome)[^A-Za-z]*(\w+\W+.*)(?=Secondary Outcome)', table.text)
        ad= lk.sub(' ', str(ad))
        ae= re.findall(r'(?sm)(?<=Secondary Outcome)[^A-Za-z]*(\w+\W+.*)(?=Target Sample Size)', table.text)
        ae= lk.sub(' ', str(ae))
        af= re.findall(r'(?sm)(?<=Target Sample Size)[^A-Za-z]*(\w+\W+.*)(?=Phase of Trial)', table.text)
        af= lk.sub(' ', str(af))
        ag= re.findall(r'(?sm)(?<=Phase of Trial)[^A-Za-z]*(\w+\W+.*)(?=Date of First Enrollment)', table.text)
        ag= lk.sub(' ', str(ag))
        ah= re.findall(r'(?sm)(?<=Global)[^A-Za-z]*(\w+\W+.*)(?=Estimated Duration of Trial)', table.text)
        ah= lk.sub(' ', str(ah))
        ai= re.findall(r'(?sm)(?<=Estimated Duration of Trial)[^A-Za-z]*(\w+\W+.*)(?=Recruitment Status)', table.text)
        ai= lk.sub(' ', str(ai))
        aj= re.findall(r'(?sm)(?<=Recruitment Status of Trial)[^A-Za-z]*(\w+\W+.*)(?=Publication Details)', table.text)
        aj= lk.sub(' ', str(aj))
        ak= re.findall(r'(?sm)(?<=Publication Details)[^A-Za-z]*(\w+\W+.*)(?=Brief Summary)', table.text)
        ak= lk.sub(' ', str(ak))
        al= re.findall(r'(?sm)(?<=Brief Summary)[^A-Za-z]*(\w+\W+.*)', table.text)
        al= lk.sub(' ', str(al))
        aw.append('%;'.join([str(aa), str(bb), str(cc), str(dd), str(ee), str(ff), str(gg), str(hh), str(ii), str(jj), str(kk), str(ll), str(mm), str(nn), str(oo), str(pp), str(qq), str(rr), str(ss), str(tt), str(uu), str(vv), str(ww), str(xx), str(yy), str(zz), str(ab), str(ac), str(ad), str(ae), str(af), str(ag), str(ah), str(ai), str(aj), str(ak), str(al)]))
        time.sleep(2)
        
        
    except:
        aw.append('no_value')
        
    finally:
        
        return aw


# In[8]:


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


df2.to_excel('results_29May.xlsx')


# In[ ]:





# In[ ]:




