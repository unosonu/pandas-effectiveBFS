
# coding: utf-8

# In[4]:

import csv as csv
import numpy as np
csv_file_object  = csv.reader(open('C:\\Users\\atul_anand01\\Desktop\\train.csv', 'rb'))

header = csv_file_object.next()

data = []
for row in csv_file_object:
    data.append(row)
    #print row
#print data[0]
data = np.array(data)
header

#print data[0::,4]  ## To print all the values from a column
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))

print number_passengers
print number_survived
proportion_survivors = number_survived/number_passengers
print proportion_survivors

women_only_stats = data[0::,4] == 'female'
#print women_only_stats

men_only_stats = data[0::,4] != 'female'
#print men_only_stats

women_onboard = data[women_only_stats,1].astype(np.float)     
men_onboard = data[men_only_stats,1].astype(np.float)

proportion_women_survived =                        np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived =                        np.sum(men_onboard) / np.size(men_onboard) 

# and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived


# In[20]:

test_file = open('C:\\Users\\atul_anand01\\Desktop\\test.csv', 'rb')
#test_file = 'C:\\Users\\atul_anand01\\Desktop\\test.csv'
test_file_object = csv.reader(test_file)
header = test_file_object.next()
sum =0
for row in test_file_object:
    sum += 1
    
print sum


# In[24]:

test_file = open('C:\\Users\\atul_anand01\\Desktop\\test.csv', 'rb')
test_file_object = csv.reader(test_file)

prediction_file = open("C:\\Users\\atul_anand01\\Desktop\\genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)
prediction_file_object.writerow(["passengerId","survived"])
for row in test_file_object:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])
test_file.close()
prediction_file.close()


# In[25]:

#Addition of a ceiling
fare_ceiling = 40

data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling -1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

number_of_classes = 3

number_of_classes = len(np.unique(data[0::,2]))

survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))

for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets): #Looping through each price bin 
        
        women_only_stats = data[
                            (data[0::,4] == "female")
                            &(data[0::,2].astype(np.float) == i+1)
                            &(data[0::,9].astype(np.float) >= j*fare_bracket_size)
                            &(data[0::,9].astype(np.float) < (j+1)*fare_bracket_size),1]
        
        men_only_stats = data[
                              (data[0::,4] != "female")
                            &(data[0::,2].astype(np.float) == i+1)
                            &(data[0::,9].astype(np.float) >= j*fare_bracket_size)
                            &(data[0::,9].astype(np.float) < (j+1)*fare_bracket_size),1]
        
        
survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float)) 
survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))
        

