#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re


# In[2]:


df1= pd.read_excel('results_25july.xlsx')


# In[7]:


df1['sum_all']= df1['all'].str.split(':%')


# In[150]:


dfn= df1[['sum_all']]


# In[151]:


dfn= dfn.stack().apply(pd.Series)


# In[12]:


df1['all'].values[0]


# In[13]:


df2.columns= ['ctri_id', 'study_design', 'public_title', 'scientific_title', 'country', 'sample_size', 'phase', 'trial_type', 'sponsor_1', 'sponsor_2', 'condition', 'intervention', 'primary_outcome']


# In[20]:


df2['ctri']= df2.ctri_id.str.split('\\\\').map(lambda x: x[0]).str.replace("^\W+", '')


# In[33]:


df2['country']= df2.country.str.replace('(?<=[a-z])(?=[A-Z])', ' ').str.replace('\W+', ' ').values


# In[46]:


df2['sample_size']= df2.sample_size.str.split('\=', n=1).map(lambda x: x[-1]).str.split('Sample Size from India').map(lambda x: x[0]).str.replace('\W+', '').values


# In[53]:


df2.sponsor_1.values[1211]


# In[56]:


df2['sponsor_1']= df2.sponsor_1.replace('Address', np.nan, regex= True).astype(str).str.split(',').map(lambda x: x[0])


# In[68]:


df2.ctri_id.values[6]


# In[69]:


df2['sponsor_20']= df2.sponsor_2.str.split('\,\s+\{0:').map(lambda x: x[0]).str.split(',').map(lambda x: x[0]).values


# In[70]:


df2['sponsor_21']= df2.sponsor_2.str.split('\,\s+\{0:').map(lambda x: x[-1]).str.split(',').map(lambda x: x[0]).values


# In[71]:


df2['sponsor_2']= df2['sponsor_20']+ df2['sponsor_21']


# In[87]:


io= re.compile('(?i)(^\W*name|none|nil\W*$)')


# In[179]:


io1= re.compile('(?i)(^\W*name|none|NIL\W*\w+$)')


# In[89]:


df2['sponsor_2']= df2['sponsor_20'].str.replace('0', '').str.replace('\W+', ' ').replace(io, np.nan, regex= True)


# In[92]:


df2['condition']= df2.condition.replace(io, np.nan, regex= True)


# In[190]:


df2['intervention']= dfn[11].str.split('Intervention').map(lambda x: x[-1]).str.replace('(0|1|2)(\:)', '').str.replace('(0|1|2)(\.)', '').str.replace('[^A-Za-z0-9-/:\,]', ' ').replace('^.*xa0Year.*$', np.nan, regex= True).replace('^.*Type\s+Name\s+Details.*$', np.nan, regex= True).str.strip()


# In[149]:


df2['primary_outcome']= df2.primary_outcome.str.replace('([0123])(\.|\:)', '').astype(str).str.replace('[^A-Za-z0-9-/:]', ' ').str.strip().str.replace('\s+', ' ').values


# In[194]:


df2['intervention']= df2.intervention.astype(str).str.split(',', n=1).map(lambda x:x[-1]).str.split(',').map(lambda x: x[0]).str.strip().values


# In[195]:


df2.columns


# In[197]:


df3= df2[['ctri', 'public_title', 'scientific_title', 'sponsor_1',
       'sponsor_2', 'condition', 'intervention', 'primary_outcome']]


# In[198]:


df3.index.size


# In[199]:


import pandas_profiling


# In[201]:


df3.to_excel('last_4663_ctri_25july.xlsx')


# In[202]:


df2.to_excel('last_4663_ctri_allfields_25july.xlsx')


# In[203]:


df4= pd.read_excel('clean_ctri_19123_24july.xlsx')


# In[205]:


df4.drop('ctri_y', axis=1, inplace= True)


# In[209]:


df4.drop('intervention_y', axis=1, inplace= True)


# In[210]:


df4.columns=['ctri', 'sponsor_1', 'sponsor_2', 'primary_outcome', 'condition', 'public_title', 'scientific_title', 'intervention'] 
       


# In[207]:


df3.columns


# In[212]:


df3= df3.reset_index()


# In[216]:


df3.drop(['level_1', 'level_0'], axis= 1, inplace= True)


# In[221]:


ctri_19519= pd.concat([df3, df4]).drop_duplicates(subset= 'ctri')


# In[222]:


ctri_19519.to_excel('ctri_clean_total_19519.xlsx')


# In[ ]:




