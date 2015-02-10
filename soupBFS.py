
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:

s = pd.Series([1,3,5,np.nan,6,8])
s


# In[8]:

dates = pd.date_range('20130101', periods = 6)
dates

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df


# In[9]:

df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","text","train"]),
                    'F':'foo'})
df2


# In[11]:

df2.dtypes


# In[12]:

df.head()


# In[16]:

df.tail()
df.index


# In[24]:

df.columns
df.values
df.describe()
df.T
df.sort(columns='B')
df.A
df['A']
df[0:3]
df['20130102':'20130104']
df.loc[dates[0]]
df.loc[:,['A','B']]
#label sliding with both endpoints included
#selection by position
df.iloc[3]


# In[27]:

df.mean()
df.


# In[21]:

import urllib2
from bs4 import BeautifulSoup

page_object = urllib2.urlopen(r'file:\\C:\Users\atul_anand01\Desktop\test-html-imdb.html')
soup = BeautifulSoup(page_object)
links = soup.find_all('a')
for link in links:
    print  link.get('href') , '-=-=-=-=-=-=', link.get_text()
    
    #link.get_text()


# In[22]:

import urllib2
from bs4 import BeautifulSoup

#page_object = urllib2.urlopen(r'http://www.imdb.com/title/tt1547234/')
page_object = urllib2.urlopen(r'http://sparshv2/Pages/Home.aspx')
soup = BeautifulSoup(page_object)
links = soup.findall('a')
print links

