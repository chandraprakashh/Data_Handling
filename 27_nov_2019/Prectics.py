# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:28:01 2019

@author: BSDU ADMIN
"""

import pandas as pd

import numpy as np

data = np.array([12,22,44,89])


print(type(data))
print(data)



s = pd.Series(data)
print (type(s))
print(s)



#####################################indexing ################################################
data = np.array([12,22,44,55])
print(type(data))

s = pd.Series(data,index=[10,11,12,13])
type(s)
print (s)

################################## sliesing #################################################

s = pd.Series(data,index=[10,11,12,13])

print(s[10])
print(s[:2])
print(s[:-3])
###########################


c = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(type(c))
print(c)


print(c['c'])
print(c['e'])
print(c[['a','c','e']])


#########################################'''A Data frame is a two-dimensional data structure''' #######
import pandas as pd

data = [1,4,7,9]
frame = pd.DataFrame(data)
print(type(frame))
print(frame)

#######################################use for data frame ##############################

frame = [['chandra prakash',19],['abhisekh gupta',17],['dinesh perjapat',18]]

the = pd.DataFrame(frame, columns=['name','age'])
type(the)
print (the)


data = {'name':['chandu','amit','rahul','maynk'],'age':[19,18,18,18]}
data3 = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
type (data3)
print(data3)

print(data3['age']['rank3'])

####################################################################################

c = {'one':pd.Series([1,2,3],index=[1,2,3]),
     'two':pd.Series([3,4,5,6],index=[1,2,3,4])}

r = pd.DataFrame(c)

print (r)


########################## add coulmns ################################################

c['three'] = pd.Series([12,21,12,34],index=[1,2,3,4])
r = pd.DataFrame(c)
print(r)


c['fourth'] = pd.Series([2,3,4,5],index=[1,2,3,4])
r = pd.DataFrame(c)
print(r)


################################ new row coulam ko jodna ++++ ###########################################
c['sixth']= c['two']+c['fourth']
r = pd.DataFrame(c)
print(r)


############################### colums ko delet krna #######################################
del c['three']
print(r)

c['one'] = pd.DataFrame[1,2,3,4],index=[1,2,3,4]
r = pd.DataFrame(c)
print(r)

r.pop('two')
print(r)


del r['sixth']
print(r)

r.pop('one')
print(r)

################################# loc and iloc uses ########################################
print (type(r.loc[3]))
print (r.loc[3])


print (type(r.iloc[3]))
print(r.iloc[3])
print (r)

####################################### csv file ####################################

import pandas as pd

i = pd.read_csv("Salaries.csv")
print(i)



i.info()

i.ndim  

i.size

i.shape

i.head()

i.tail(5)
i.columns 
i.dtypes
i.values


print(type(i.describe()))


############################# code challanage ##################################
#1. Which Male and Female Professor has the highest and the lowest salaries

import pandas as pd

i = pd.read_csv("Salaries.csv")
print(i)
i ['sex'].unique().tolist()
i[i['sex']=='Male'][i['rank']=='Prof'] ['salary'].max()
i[i['sex']=='Female'][i['rank']=='Prof'] ['salary'].max()

i[i['sex']=='Male'][i['rank']=='Prof'] ['salary'].min()
i[i['sex']=='Female'][i['rank']=='Prof'] ['salary'].min()



#2. Which Professor takes the highest and lowest salaries.
i [i['rank']=='Prof']['salary'].max()
i [i['rank']=='Prof']['salary'].min()


#6. How many are Prof, AssocProf and AsstProf. 
   #Show both in numbers adn Graphically using a Pie Chart
   
import matplotlib.pyplot as plt
import pandas as pd

this = i['rank'].value_counts()
labels = ['Prof', 'Asso', 'Asst']
explode = [0.1,0,0]


plt.pie(this, explode=explode, autopct='%1.2f%%', labels=labels)

plt.show()



















































































######################################################




























