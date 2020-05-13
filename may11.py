#!/usr/bin/env python
# coding: utf-8

# In[1]:


from xml.etree.ElementTree import parse


# In[6]:


document= parse('myxml.xml')


# In[7]:


print(document)


# In[8]:


root= document.getroot()


# In[9]:


root


# In[11]:


tag= root.tag
att= root.attrib


# In[12]:


print(tag)
print(att)


# In[13]:


for child in root:
    print(child.tag, child.attrib)


# In[16]:


for child in root:
    #print(child.tag, child.attrib)
    for subchild in child:
        #print(subchild.tag, subchild.attrib, subchild.text)
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.attrib, subsubchild.text)


# In[17]:


for item in document.iterfind('trial'):
    for x in item .iterfind('trial_identification'):
        print(x.findtext('trial_id'))


# In[18]:


import os
import pandas as pd
import xmltodict
import json


# In[20]:


for file in os.listdir():
    if file.endswith('.xml'):
        with open(os.path.join(file), encoding= 'ISO-8859-1') as xml:
            doc= xmltodict.parse(xml.read())


# In[ ]:





# In[24]:


trials_trials= []
for trial in doc['trials']['trial']:
    trials_trials.append(json.dumps(trial))


# In[26]:


df= pd.DataFrame()


# In[82]:


df[0]= trials_trials


# In[83]:


df.head(2)


# In[84]:


df[0]


# In[85]:


xx= json.loads(df[0][0])


# In[ ]:





# In[36]:


xx.keys()


# In[30]:


json.loads(df[0][0]).keys()


# In[80]:


ff= pd.DataFrame(columns= range(1, 17))


# In[86]:


ff.columns= list(json.loads(df[0][0]).keys())


# In[87]:


df[0]= df[0].map(lambda x: json.loads(x))


# In[88]:


for col in ff.columns:
    ff[col]= df[0].map(lambda x: x.get(col))


# In[89]:


ll= ['trial_identification', 'sponsors_and_support', 'health_conditions', 'interventions', 'recruitment', 'study', 'outcomes', 'contacts', 'secondary_ids', 'references']


# In[90]:


ff_new= ff[ll]


# In[91]:


for x in ll:
    pp= ff_new[x][0].keys()
    for i in pp:
        ff[i]= ff[x].map(lambda x: x.get(i))


# In[92]:


ff.drop(ll, axis= 1, inplace= True)


# In[93]:


ff.columns


# In[94]:


dd= []
for x in ff.columns:
    if 'dict' in str(type(ff[x][0])):
        dd.append(x)
    
        
    


# In[99]:


for x in dd:
    try:
        ff[x]= ff[x].map(lambda x: x.values())
            
    except:
        pass


# In[101]:


ff[dd]


# In[ ]:


ff.applymap()


# In[102]:


ff.applymap(lambda x: str(x)).replace(to_replace= '@', value= '', regex= True).replace(to_replace= "{'@value': ", value= '', regex= True)


# In[ ]:





# In[ ]:




