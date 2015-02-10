
# coding: utf-8

# In[19]:

import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse

file_obj = open('C:\Users\\atul_anand01\\Desktop\\parse-correct.html','U')
soup = BeautifulSoup(file_obj)
print soup


# In[24]:

# write contents in a file
return_file = open('C:\Users\\atul_anand01\\Desktop\\return_file.html','w+')
return_file.write(soup.prettify())
return_file.close()


# In[52]:

import sys
sys.path.append('C:\Users\atul_anand01\Desktop\test-exe')


# In[67]:

##from Users.atul_anand01.Desktop.test_exe import setup
get_ipython().magic(u"load r'C:\\Users\\\\atul_anand01\\\\Desktop\\\\test-exe\\\\setup.py'")
import setup


# In[ ]:

C:\Users\\atul_anand01\\Desktop\\test-exe\\setup.py


# In[ ]:

C:\Users\\atul_anand01\\Desktop\\test-exe\\html-correct.py


# In[ ]:

C:\Users\\atul_anand01\\Desktop\\test-exe\\html-correct.py


# In[30]:

from distutils.core import setup
import py2exe

setup(console=['C:\\Users\\atul_anand01\\Desktop\\test-exe\\html-correct.py'])

