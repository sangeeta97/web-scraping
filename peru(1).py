#!/usr/bin/env python
# coding: utf-8

# In[1]:


url = 'https://www.clinicaltrialsregister.eu/ctr-search/search?query=&resultsstatus=trials-with-results&page1'


# In[2]:


import pandas as pd
import numpy as np
import re


# In[3]:


import requests
from bs4 import BeautifulSoup
import re
import time
import random 
import xlrd


# In[5]:


response = requests.get(url)


# In[6]:


page_html = BeautifulSoup(response.text, 'html.parser')


# In[7]:


trial_tables = page_html.find_all('table', {'class': 'result'})


# In[12]:


for trial_table in trial_tables:
        trial_id = trial_table.input.get('title')


# In[14]:


leg_text = page_html.find('div', id = 'synopsisLegislationNote')


# In[44]:


trial_tables = page_html.find_all('table')[4]


# In[17]:


td_value = trial_tables.find_all('td', class_ = 'valueColumn')


# In[18]:


td_value


# In[19]:


td_label = trial_tables.find_all('td', class_ = 'labelColumn') 


# In[58]:


trial_tables.find_all('td')[0].get_text()


# In[45]:


trial_tables.find_all('a')[0].get_text()


# In[65]:


yy= page_html.find_all('table')[4]


# In[66]:


bb= [text for text in yy.stripped_strings]


# In[67]:


bb


# In[ ]:


from requests import get
from requests import ConnectionError
from bs4 import BeautifulSoup
import re
from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import pandas as pd
import random

# +
#pull single page to test and get max page number
url = 'https://www.clinicaltrialsregister.eu/ctr-search/search?query=&resultsstatus=trials-with-results&page1'
response = get(url)
html = response.content

#what does our parsed html look like?
soup = BeautifulSoup(html, "html.parser")
# -

#gets max page number
number_of_pages = soup.find('div', {'class': 'margin-bottom: 6px;'})
max_page_link = str(number_of_pages.find_all('a')[-1])
max_page = re.findall(r'\d+', max_page_link)[0]
print(max_page)

#setting up variables for page URLs
euctr_base_url = 'https://www.clinicaltrialsregister.eu'
euctr_results_search_page = '/ctr-search/search?query=&resultsstatus=trials-with-results&page='

#variables needed for first scrape
pages = [str(i) for i in range(1,int(max_page)+1)]
trial_ids = []
results_urls = []
start_time = time()
requests = 0
print(pages[-1])

# +
#this crawls every trial that comes up with a search result of trials with results on the EUCTR

for page in pages:
    
    #make this request
    tries=3
    for i in range(tries):
        try:
            response = get(euctr_base_url + euctr_results_search_page + page, verify = False)
            break
        except ConnectionError as e:
            if i < tries - 1:
                sleep(2)
                continue
            else:
                raise
    
    #pause to look like a human
    #sleep(random.uniform(0,0.2)) #not needed at the moment for this
    
    #mointor the requests to ensure everything is working
    requests += 1
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)
    
    # Throw a warning for a non-200 status code
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    #Break the looop if we exceed the number of requests which will need to change when i do full scrape
    if requests > int(max_page):
        warn('Number of requests was greater than expected.')  
        break 
    
    #Parse the requests
    page_html = BeautifulSoup(response.text, 'html.parser')
    
    #select all the trial tables
    trial_tables = page_html.find_all('table', {'class': 'result'})
    
    #get the trial id and the trial url for each thing
    for trial_table in trial_tables:
        trial_id = trial_table.input.get('value')
        trial_ids.append(trial_id)
        url = euctr_base_url + trial_table.find_all('a')[-1].get('href')
        results_urls.append(url)

# +
results_trial_id = []
global_end_of_trial_date = []
first_publication_date = []
current_publication_date = []
results_version = []
results_type = []
new1 = []
new2 = []
new3 = []
new4 = []
new5 = []
new6 = []

start_time_2 = time()
requests_2 = 0
trial_number = 0

# +
#this takes the urls from the above scrape, and crawls them for results information

for result_url in results_urls: 
    
    #make this request
    tries=3
    for i in range(tries):
        try:
            requests_2 += 1
            response = get(result_url, verify = False)
            break
        except ConnectionError as e:
            if i < tries - 1:
                sleep(2)
                continue
            else:
                raise     
    
    #pause to look like a human
    #sleep(random.uniform(0,0.5)) #uncomment if needed
    
    #mointor the requests to ensure everything is working
    trial_number += 1
    elapsed_time = time() - start_time_2
    print('Trial Number: {}; Request: {}; Frequency: {} requests/s'.format(trial_number, requests_2, requests_2/elapsed_time))
    clear_output(wait = True)
    
    # Throw a warning for a non-200 status code
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests_2, response.status_code))

    #Break the looop if we exceed the number of requests which will need to change when i do full scrape
    if requests_2 > len(results_urls):
        warn('Number of requests was greater than expected.')  
        break 
    
    #Parse the requests
    page_html = BeautifulSoup(response.text, 'html.parser')
    
    #select all the results tables
    
    trial_tables = page_html.find_all('table')[4]
    
    n1 = trial_tables.find_all('td')[0].get_text()
    new1.append(n1)
    n2 = trial_tables.find_all('td')[1].get_text()
    new2.append(n2)
    n3 = trial_tables.find_all('td')[2].get_text()
    new3.append(n3)
    n4 = trial_tables.find_all('td')[3].get_text()
    new4.append(n4)
    n5 = trial_tables.find_all('td')[4].get_text()
    new5.append(n5)
    n6 = trial_tables.find_all('td')[5].get_text()
    new6.append(n6)
    global_end_date = tds_strip(td_value,3)
    global_end_of_trial_date.append(global_end_date)
    


# In[68]:


import os


# In[69]:


for file in os.listdir():
    if file.endswith('.zip'):
        anzctr_zip = file


# In[70]:


print(anzctr_zip)


# In[72]:


import zipfile
zip_ref = zipfile.ZipFile(anzctr_zip, 'r')
zip_ref.extractall()
zip_ref.close()


# In[75]:


get_ipython().system('pip install xmltodict')


# In[76]:


import xmltodict
import json
anzctr_trials_list = []


# In[77]:


for file in os.listdir():
    if file.endswith('.xml'):
        with open(os.path.join(file), encoding="utf8") as xml:
            doc = xmltodict.parse(xml.read())
            anzctr_trials_list.append(str(json.dumps(doc)))


# In[78]:


df1= pd.DataFrame(anzctr_trials_list)
df1.to_csv('anz.csv')


# In[5]:


import pandas as pd


# In[6]:


df1= pd.read_csv('anz.csv')


# In[7]:


df2= df1[0:3]


# In[8]:


type(df2)


# In[11]:


import json


# In[19]:


js= json.loads(json_string)


# In[24]:


js['ANZCTR_Trial']['trial_identification']['studytitle']


# In[ ]:





# In[ ]:





# In[ ]:





# In[109]:


df1[0].values


# In[ ]:





# In[25]:


import pandas as pd


# In[124]:


k11= pd.read_csv('sangeeta.csv', header= None)


# In[155]:


k11['tt']= k11.astype(str).applymap(lambda x: json.loads(x))


# In[101]:


k1['trial_id']= k1['tt'].map(lambda x: x['main']['trial_id'])


# In[102]:


k1['utrn']= k1['tt'].map(lambda x: x['main']['utrn'])


# In[103]:


k1['reg_name']= k1['tt'].map(lambda x: x['main']['reg_name'])


# In[104]:


k1['date_registration']= k1['tt'].map(lambda x: x['main']['date_registration'])


# In[156]:


k1['primary_sponsor']= k11['tt'].map(lambda x: x['main']).map(lambda x: x.values()).map(lambda x: list(x)).map(lambda x: x[4:5])


# In[107]:


k1['public_title']= k1['tt'].map(lambda x: x['main']['public_title'])


# In[108]:


k1['scientific_title']= k1['tt'].map(lambda x: x['main']['scientific_title'])


# In[109]:


k1['date_enrolment']= k1['tt'].map(lambda x: x['main']['date_enrolment'])


# In[110]:


k1['type_enrolment']= k1['tt'].map(lambda x: x['main']['type_enrolment'])


# In[111]:


k1['target_size']= k1['tt'].map(lambda x: x['main']['target_size'])


# In[112]:


k1['recruitment_status']= k1['tt'].map(lambda x: x['main']['recruitment_status'])


# In[113]:


k1['study_type']= k1['tt'].map(lambda x: x['main']['study_type'])


# In[114]:


k1['study_design']= k1['tt'].map(lambda x: x['main']['study_design'])


# In[115]:


k1['phase']= k1['tt'].map(lambda x: x['main']['phase'])


# In[116]:


k1['countries']= k1['tt'].map(lambda x: x['countries']['country2'])


# In[117]:


k1['inclusion_criteria']= k1['tt'].map(lambda x: x['criteria']['inclusion_criteria'])


# In[118]:


k1['exclusion_criteria']= k1['tt'].map(lambda x: x['criteria']['exclusion_criteria'])


# In[119]:


k1['health_condition_keyword']= k1['tt'].map(lambda x: x['health_condition_keyword']['hc_keyword'])


# In[120]:


k1['sec_id']= k1['tt'].map(lambda x: x['secondary_ids']['secondary_id']).map(lambda x: [i['sec_id'] for i in x])


# In[121]:


k1= k1.iloc[:, 2:]


# In[157]:


k1.shape


# In[159]:


k1.to_excel('sk_peru_17sept2019.xls')


# In[135]:


ml= k11.astype(str).applymap(lambda x: json.loads(x))[0][0]


# In[140]:


type(ml['main'])


# In[141]:


lm= ml['main']


# In[145]:


lm= lm.values()


# In[147]:


lm= list(lm)


# In[152]:


lm[4:5]


# In[139]:


ml[0:1]


# In[137]:


ml['main']['primary_sponsor']


# In[ ]:





# In[ ]:





# In[59]:


jk= k1.applymap(lambda x: x['secondary_ids']['secondary_id'])[0][0]


# In[ ]:


for i in jk:
    


# In[60]:


[i['sec_id'] for i in jk]


# In[39]:


k1[0][0]


# In[67]:


k1.applymap(lambda x: x['intervention_keyword'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


leg_text = page_html.find('div', id = 'synopsisLegislationNote')
    trial_tables = page_html.find_all('table')[4]
    td_value = trial_tables.find_all('td', class_ = 'valueColumn')
    td_label = trial_tables.find_all('td', class_ = 'labelColumn') 
    trial_id = trial_tables.find_all('a')[0].get_text()
    results_trial_id.append(trial_id)
    global_end_date = tds_strip(td_value,3)
    global_end_of_trial_date.append(global_end_date)
    
    if td_label[-1].div.get_text().strip() == 'Summary report(s)' and leg_text:
        first_pub = tds_strip(td_value,11)
        first_publication_date.append(first_pub)
        current_pub = tds_strip(td_value,10)
        current_publication_date.append(current_pub)
        version = td_value[9].get_text().strip()
        results_version.append(version)
        results_type.append("Document")
    
    elif td_label[-1].div.get_text().strip() == 'Summary report(s)' and not leg_text:
        first_pub = tds_strip(td_value,7)
        first_publication_date.append(first_pub)
        current_pub = tds_strip(td_value,6)
        current_publication_date.append(current_pub)
        version = td_value[5].get_text().strip()
        results_version.append(version)
        results_type.append("Mixed")
        
    else:
        first_pub = tds_strip(td_value,7)
        first_publication_date.append(first_pub)
        current_pub = tds_strip(td_value,6)
        current_publication_date.append(current_pub)
        version = td_value[5].get_text().strip()
        results_version.append(version)
        results_type.append("Tabular")
# -

if len(trial_ids) == len(results_trial_id):

