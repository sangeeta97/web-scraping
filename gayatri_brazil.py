#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd

import xmltodict
import json
tctr_trials = []

for file in os.listdir():
    if file.endswith('.xml'):
        with open(os.path.join(file), encoding = "ISO-8859-1") as xml:
            doc = xmltodict.parse(xml.read())
            trials_trials=[]
            for trial in doc['trials']['trial']:
                 tctr_trials.append(json.dumps(trial))


# In[5]:


from datetime import date
import csv

def tctr_csv():
    with open('tctr1.csv','w', newline = '') as tctr_csv:
        writer=csv.writer(tctr_csv)
        for val in tctr_trials:
            writer.writerow([val])

tctr_csv()


# In[9]:


df= pd.read_csv('tctr1.csv', header= None)


# In[69]:


list(df[0][0].values())[0]


# In[40]:


ff= pd.DataFrame(columns= range(1, 17))


# In[41]:


ff.columns= list((json.loads(df[0][0])).keys())


# In[44]:


ff.columns


# In[49]:


df[0].map(lambda x: type(x))


# In[58]:


for col in ff.columns:
    ff[col]= df[0].map(lambda x: x.get(col))


# In[48]:


df[0]= df[0].map(lambda x: json.loads(x))


# In[72]:


pp= ff['trial_identification'][0].keys()


# In[74]:


for i in list(pp):
    ff[i]= ff['trial_identification'].map(lambda x: x.get(i))


# In[60]:


ff['trial_identification'].map(lambda x: x.keys())


# In[77]:


ff.drop(range(0, 9), axis= 1, inplace= True)


# In[78]:


ff.columns


# In[87]:


pp= ff['contacts'][0].keys()
for i in list(pp):
    ff[i]= ff['contacts'].map(lambda x: x.get(i))


# In[89]:


pp= ff['secondary_ids'][0].keys()
for i in list(pp):
    ff[i]= ff['secondary_ids'].map(lambda x: x.get(i))


# In[91]:


pf= ff.drop(['trial_identification', 'sponsors_and_support', 'health_conditions',
       'interventions', 'recruitment', 'study', 'outcomes', 'contacts',
       'secondary_ids'], axis=1)


# In[93]:


ff.columns


# In[92]:


pf.columns


# In[98]:


pf= pf.applymap(lambda x: str(x)).replace(to_replace= '@', value= '', regex= True).replace(to_replace= "{'value':", value= '', regex= True).replace(to_replace= "{", value= '', regex= True).replace(to_replace= "}", value= '', regex= True)


# In[99]:


pf.to_excel('sk_brazil_terminated_29April2020.xlsx')


# In[ ]:




