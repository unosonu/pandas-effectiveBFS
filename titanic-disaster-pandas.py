
# coding: utf-8

# In[9]:

import csv as csv
import numpy as np
csv_file_object = csv.reader(open('C:\\Users\\atul_anand01\\Desktop\\train.csv','rb'))
header = csv_file_object.next()
data = []

for row in csv_file_object:
    data.append(row)
    
data = np.array(data)
#print data
#print header

#first 15 rows of the age column
print data[0:15,5]

type(data[0::,5]) #to see what kind of data type is the age column


# In[8]:

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\atul_anand01\\Desktop\\train.csv', header=0)
#df
df.head(3)
type(df)
df.dtypes
df.info()
df.info
df.describe()
df['Age'][0:10] #first 10 rows of the age column
df.Age[0:10] #alternate way
type(df['Age'])
df['Age'].mean()
df[['Sex','Pclass','Age']]
df[df['Age']>60]
df[df['Age']>60][['Sex','Pclass','Age','Survived']]
df[df['Age'].isnull()][['Sex','Pclass','Age']]

for i in range(1,4):
    print i, len(df[ (df['Sex']=='male') & (df['Pclass']==i) ])  ## use of where clause with multiple conditions


# In[18]:

import pylab as p
df['Age'].hist()
p.show()
df['Age'].dropna().hist(bins=16, range=(0,80), alpha=.5)
p.show()


# In[39]:

df['Gender']= 4 #Adding a column
df.head(2)
df['Gender'] = df['Sex'].map(lambda x: x[0].upper())
df.head(3)
df['Gender'] = df['Sex'].map({'female':0, 'male':1}).astype(int)

median_ages = np.zeros((2,3))
median_ages

#populating the array
for i in range(0,2):
    for j in range(0,3):
        median_ages[i,j]  = df[(df['Gender'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()
        
median_ages


# In[45]:




df['AgeFill'] = df['Age']  #Make a copy of age column
df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)

#filling in missing values 
for i in range(0,2):
    for j in range(0,3):
        df.loc[(df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1), 'AgeFill'] = median_ages[i,j]
df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)

df[df['Age'].isnull()][['Gender','Pclass','Age','AgeFill']].head(10)

df['AgeIsNull'] = pd.isnull(df.Age).astype(int)
df['AgeIsNull']


# In[54]:

df['FamilySize'] = df['SibSp'] + df['Parch']
df['Age*Pclass'] = df['Age'] * df['Pclass'] # Product can be a factor in survival as together. Can be useful
df['Age*Pclass'].hist()
df['FamilySize'].hist()
p.show()

#To check for which columns are strings
df.dtypes
df.dtypes[df.dtypes.map(lambda x: x=='object')]

# Drop the columns which we are not going to use
df = df.drop(['Name','Sex','Ticket','Cabin','Embarked'],axis =1 )
df = df.drop(['Age'],axis =1 ) # since age has missing values

# alternate way to delete columns which have missing values
df = df.dropna()


# In[55]:

#Now convert the data to a numpy array
train_data = df.values
train_data


# In[1]:

from sklearn.ensemble import RandomForestClassifier
#create random forest object
forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(train_data[0::,1::],train_data[0::,0::])
output = forest.predict(test_data)

