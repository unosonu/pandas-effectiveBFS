
# coding: utf-8

# In[2]:

import pandas as pd

daf = pd.read_csv('C:\\Users\\atul_anand01\\Desktop\\data_file_v2.csv')


# In[8]:

#daf
dtype(daf['messageText_lower'])
type(daf['messageText_lower'])
daf.info()
daf.describe()


# In[12]:

daf['messageText_lower']

