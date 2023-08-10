#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip install bs4


# In[4]:


import requests
from bs4 import BeautifulSoup
url='https://www.worldometers.info/co2-emissions/co2-emissions-by-country/'
page=requests.get(url)
page


# In[5]:


page.text


# In[8]:


soup=BeautifulSoup(page.text,'html.parser')
soup


# In[9]:


table=soup.find('table',id="example2")
table


# In[11]:


body=table.find('tbody')
body


# In[12]:


row=body.find_all('tr',style='')
row


# In[14]:


co2_emission=[]
for i in row:
    col=i.find_all('td')
    info=[c.text for c in col]
    co2_emission.append(info)
print(co2_emission)    


# In[15]:


number=[]
for i in co2_emission:
    number.append(i[0])
print(number)   


# In[16]:


country=[]
for i in co2_emission:
    country.append(i[1])
print(country)    


# In[17]:


emission=[]
for i in co2_emission:
    emission.append(i[2])
print(emission)    


# In[19]:


change=[]
for i in co2_emission:
    change.append(i[3])
print(change)    


# In[20]:


population=[]
for i in co2_emission:
    population.append(i[4])
print(population)    


# In[22]:


capita=[]
for i in co2_emission:
    capita.append(i[5])
print(capita)    


# In[23]:


share=[]
for i in co2_emission:
    share.append(i[6])
print(share)    


# In[28]:


data={'Srnumber':number,'Country':country,'CO2Emission(tons,2016)':emission,'1YearChange':change,'Population':population,'PerCapita':capita,'ShareofWorld':share}


# In[29]:


data


# In[30]:


import pandas as pd
table=pd.DataFrame(data)
table
    


# In[ ]:




