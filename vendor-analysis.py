
# coding: utf-8

# In[2]:

#Get the details of the vendor
from pandas.io import sql
import pyodbc

#connection object here
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.68.24.3;DATABASE=IMAP_Yellow_DB;UID=spineuser;PWD=spineuser')
query = 'SELECT * FROM dbo.IMAP_CaseTransactionTable'
results = sql.read_frame(query, con=conn)

#print results.head()
#print results[13:17]


# In[5]:

#Saving results in a csv file and then fetching the data from it.
import csv as csv 
import pandas as pd
import numpy as np

df = results
type(df)
#df.info()

vendor_details_v1 = open("C:\\Users\\atul_anand01\\Desktop\\vendor-details-v1.csv", "wb")

##df.to_csv(data_file_v1, sep=',', encoding='UTF-8')
##df.to_csv(data_file_v1, delim_whitespace=True, encoding='UTF-8')
##df.to_csv(data_file_v1, sep=r'\s+', encoding='UTF-8')

#df.to_csv(data_file_v1, sep=',', encoding='UTF-8')

header=['GrossAmount','NetAmount','VendorID','VendorName','TotalAmtCCC']
df.to_csv(vendor_details_v1,cols=header,encoding='UTF-8')

vendor_details_v1.close()


# In[8]:

#Script to read data from the csv.
import pandas as pd

vendor_data = pd.read_csv('C:\\Users\\atul_anand01\\Desktop\\vendor-details-v1.csv')


# In[9]:

vendor_data

