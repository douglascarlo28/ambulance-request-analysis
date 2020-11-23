#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests;


# In[9]:


import pandas as pd;


# In[ ]:


# Requisitando dados da API

url = 'http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id=5aaf98cb-0a6a-46e7-8cbd-3fedd6d4fa4d&limit=1000'  
r = requests.get(url)


# In[37]:


result = r.json()
result


# In[53]:


### Convertendo JSON to Dataframe

dataframe = pd.read_json(r.content)
dataframe
pd.json_normalize(dataframe['result']['records'])

