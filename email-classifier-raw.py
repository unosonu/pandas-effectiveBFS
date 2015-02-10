
# coding: utf-8

# In[2]:

from pandas.io import sql
import pyodbc

#connection object here
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.68.24.3;DATABASE=IMAP_Yellow_DB;UID=spineuser;PWD=spineuser')
query = 'SELECT ID,Subject,txtContent,htmlContent FROM dbo.SpineEmailDetails'
query2 = 'SELECT * FROM dbo.MailTemplateMaster'
query3 = 'Select * from dbo.MailTemplates'

results2 = sql.read_frame(query2, con=conn)
results3 = sql.read_frame(query3, con=conn)
#print results.head()
print results[13:17]


# In[5]:

results3


#### result3

# In[4]:

result3


# In[5]:

import csv as csv 
import pandas as pd
import numpy as np

df = results
type(df)
#df.info()

data_file_v1 = open("C:\\Users\\atul_anand01\\Desktop\\data_file_v1.csv", "wb")

##df.to_csv(data_file_v1, sep=',', encoding='UTF-8')
##df.to_csv(data_file_v1, delim_whitespace=True, encoding='UTF-8')
##df.to_csv(data_file_v1, sep=r'\s+', encoding='UTF-8')

#df.to_csv(data_file_v1, sep=',', encoding='UTF-8')

header=['ID','Subject','txtContent','htmlContent']
df.to_csv(data_file_v1,cols=header,encoding='UTF-8')

data_file_v1.close()

'''
data_file = open("C:\\Users\\atul_anand01\\Desktop\\data_file.csv", "wb")
data_file_object = csv.writer(data_file)
data_file_object.writerow([])
data_file.close()
'''


# In[1]:

get_ipython().system(u'cat C:\\\\Users\\\\atul_anand01\\\\Desktop\\\\data_file_v1.csv')

import pandas as pd

data = pd.read_csv('C:\\Users\\atul_anand01\\Desktop\\data_file_v1.csv')
#data


# In[117]:

#data.fillna('NA')
#data.fillna(0.0)
#data


# In[122]:

from bs4 import BeautifulSoup as BS, Comment
import re

import math
import numpy as np

#data
#data[0:3]  #not required now
#data['htmlContent'][0]
#dtype(data.htmlContent[0])

#data.htmlContent[0]  # not required now
'''
html = data.htmlContent[0]
soup = BeautifulSoup(html)

#soup.get_text()
#1
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
for comment in comments:
    comment.extract()
    
for style_tag in soup.findAll('style'):
    style_tag.extract()

soup_data=soup.stripped_strings
for string in soup_data:
    print string
'''    
    
#The above in the form of a function
def text_from_html(num):
    html = data.htmlContent[num]
    msg_string = ''
    #if pd.isnull(data.htmlContent[count]) == False:
    #if data.htmlContent[num] is not None :    
    #if data.htmlContent[num] is not 'nan':
    #if type(data.htmlContent[num]) != 'float':
    #if math.isnan(data.htmlContent[num]) == False:
    #if (data['htmlContent'][count]).pd.notnull():
    #if data.htmlContent[count].dtype != 'float':
    #if data.htmlContent[count] != np.nan:
    #if pd.isnull(data['htmlContent'][count]) == False:
    if pd.isnull(data['htmlContent'][num]) == False:
        soup = BS(html)
        comments = soup.findAll(text=lambda text:isinstance(text,Comment))
        for comment in comments:
            comment.extract()
        for style_tag in soup.findAll('style'):
            style_tag.extract()
        soup_data = soup.stripped_strings
        #return soup_data # works fine with returning the soup_data but need to return a string
        for string in soup_data:
            msg_string = msg_string + ' ' + string
    
    else:   
        msg_string = data.txtContent[num]
    return msg_string
 
print type(data['htmlContent'][12])    
print data['htmlContent'][12]
some = text_from_html(1)
#print type(some)
print some

print type(data['htmlContent'][12])

'''        
#to be used when the return type is generator
some = text_from_html(1)
for string in some:
    print string
print type(some)
'''

#for string in some:
#    print string



#print soup.body.style.get_text()
    
'''    
for child in soup.body.style.children:
    if isinstance(child,Comment):
        print child
'''

#for string in soup.strings():
#    print (repr(string))

#print type(comment)
#print soup.prettify()   
#print soup.get_text()



#[comment.extract() for comment in comments]


#soup.comment.replace_with('')
#3

'''
for string in soup.stripped_strings:
    print string
   '''



# In[123]:

#identify the length of the number of rows in the data frame
len(data)
#create a new column in the dataframe
data['message'] = 'blank data'
for count in range(len(data)):
    #condition to check for null values in txtContent as well as white spaces.
    if pd.isnull(data['htmlContent'][count]) == False:
        data['message'][count] = data['htmlContent'][count]
    else:
        data['message'][count] = data['txtContent'][count]
        #print type(data['txtContent'][count])
        


# In[38]:

'''
## the explicit(non function version of code one cell above)
from bs4 import BeautifulSoup as BS, Comment
import re

data['messageText'] = None
for count in range(len(data)):
    
    print count
    html = data.htmlContent[count]
    if pd.isnull(data.htmlContent[count]) == False:
        #
        soup = BS(html)
        comments = soup.findAll(text=lambda text:isinstance(text,Comment))
        for comment in comments:
            comment.extract()
        for style_tag in soup.findAll('style'):
            style_tag.extract()
        soup_data = soup.stripped_strings
        msg_string = ''
        for string in soup_data:
            msg_string = msg_string + ' ' + string
    
        data['messageText'][count] = msg_string
    else:
        data['messageText'][count] = data['txtContent'][count]
'''


# In[125]:

data['messageText'] = None
for count in range(len(data)):
    returned_string = text_from_html(count)
    data['messageText'][count] = returned_string


# In[135]:

type(data['messageText'])
data['messageText_lower']=data['messageText'].str.lower()


# In[139]:

#data['messageText_lower']=data['messageText'].str.lower()
#data

header = ["ID", "Subject", "messageText_lower"]
data.to_csv('C:\\Users\\atul_anand01\\Desktop\\data_file_v2.csv', cols = header, encoding='UTF-8')


# In[84]:

print type(data['htmlContent'][0])

'''
data.head(10)
#data['Subject','txtContent'].head(10)
df = data['htmlContent'].notnull()
#df.head(50)
data.head(50)
#data[50::100]

'''


# In[ ]:


"""
## to write from the database to a csv for better import
import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.68.24.3;DATABASE=IMAP_Yellow_DB;UID=spineuser;PWD=spineuser')
##Can provide port as well with "Port=" as another argument
cursor = conn.cursor()

#

'''same as below'''
### -- cursor.execute("SELECT ID,Subject, txtContent, htmlContent FROM dbo.SpineEmailDetails")
#row = cursor.fetchone()
#print row

'''risky to execute, hangs the browser tab'''
## --rows = cursor.fetchall()  ## if you use fetchone as well above then then using fetchall brings the results after the first row

'''
for each_row in rows:
    print each_row
'''

# now get every every row from rows to put in a csv file.

conn.close()
               
"""


    
    
'''
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match(('<!--.*-->').encode('UTF-8'), str(element)):
        return False
    return True
texts = soup.findAll(text = True)
visible_texts = filter(visible, texts)
'''


# In[81]:

data

