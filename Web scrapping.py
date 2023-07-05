#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url="https://www.w3schools.com/python/default.asp"


# In[8]:


page=requests.get(url)


# In[ ]:





# In[12]:


soup=BeautifulSoup(page.text,'html')


# In[13]:


print(soup)


# In[14]:


print(soup.prettify())


# In[15]:


soup.find('div')


# In[17]:


soup.find_all('div')


# In[20]:


soup.find_all('div',class_='')


# In[23]:


soup.find('div',id="leftmenuinnerinner")


# In[27]:


soup.find('p').text.strip()

