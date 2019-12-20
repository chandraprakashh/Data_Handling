# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:13:52 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""

#Convert the column name to single word names
import pandas as pd

file = pd.read_csv('thanksgiving-2015-poll-data.csv')
df = pd.DataFrame(file)
print(file)

#file.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5', 'Row_6', 'Row_7', 'Row_8', 'Row_9', 'Row_10', 'Row_11', 'Row_12', 'Row_13', 'Row_14', 'Row_15', 'Row_16', 'Row_17', 'Row_18', 'Row_19', 'Row_20', 'Row_21', 'Row_22', 'Row_23', 'Row_24', 'Row_25', 'Row_26', 'Row_27', 'Row_28', 'Row_29', 'Row_30', 'Row_31', 'Row_32', 'Row_33', 'Row_35', 'Row_36', 'Row_37', 'Row_38', 'Row_39', 'Row_40', 'Row_41', 'Row_42', 'Row_43', 'Row_44', 'Row_45', 'Row_46', 'Row_47', 'Row_48', 'Row_49', 'Row50', 'Row_51', 'Row_52', 'Row_53', 'Row_54', 'Row_55', 'Row_56', 'Row_57', 'Row_58', 'Row_59', 'Row_60', 'Row_61', 'Row_62', 'Row_63', 'Row_64'] 
                 
#print(file)

c = df.columns.tolist()

list2 = {}

cols = list(df.columns.values)

list3 = []

for i in range(0,65):  
    list3.append('columns'+str(i))
    
list2={}


for i in range(0,len(list3)):
    list2[cols[i]] = list3[i]

df.rename(columns=list2, inplace=True)
print(df)

#=========================================================
#

#Using the apply method to Gender column to convert Male & Female
df['columns62'] = df['columns62'].apply(lambda x:1 if( x =='Male') else 0)
print(df)


#df['columns62'].replace(['male','female'],[0,1],inplace=True)

#==============================================================


#Using the apply method to clean up income
#(Range to a average number, X and up to X, Prefer not to answer to NaN)
import numpy as np
df['columns63']=df['columns63'].astype(str)
df['columns63']=df['columns63'].replace('Prefer not to answer', np.nan)

def fun(num):
    if 'to' in str(num):
        num = num.replace("$","")
        num = num.replace(",", "")
        a,b = num.split(' to ')
        return(float(a) + float(b)/2)
    elif("$200,000 and up"):
        return int(20000)
df['columns63'] = df['columns63'].apply(fun)

#==============================================================================
#compare income between people who tend to eat homemade cranberry sauce for
#Thanksgiving vs people who eat canned cranberry sauce?
    
#
import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv('thanksgiving-2015-poll-data.csv')   
print(d) 

x = round(df[df['columns8']=='Homemade']['columns63']).mean()
y = round(df[df['columns8']=='Canned']['columns63']).mean()

labels = ('Homemade', 'Canned')
sizes = [x,y]

plt.pie(sizes, labels=labels,autopct='%1.2f%%')
plt.show

#===================================================================================    
#find the average income for people who served each type of cranberry sauce
#for Thanksgiving (Canned, Homemade, None, etc).
 


a = df[df['columns8']=='Homemade']['columns63'].mean()
b = df[df['columns8']=='Canned']['columns63'].mean()
c = df[df['columns8']=='None']['columns63'].mean()
d = df[df['columns8']=='other(please specify)']['columns63'].mean()



label = ['Homemade', 'Canned', 'None']
sizes = [a, b, c]
color = ['gold', 'yellowgreen', 'lightcoral']

# Plot
plt.pie(sizes, labels=label, colors=color, autopct='%1.2f%%')


#===================================================================================

#Plotting the results of aggregation
#    
#Do people in Suburban areas eat more Tofurkey than people in Rural areas?

a = len(df[df['columns60']=='Suburban']['columns2'])
b = len(df[df['columns60']=='Rural']['columns2'])

plt.xticks([0,1],['Suburban','Rural'])
plt.bar([0,1],[a,b],color=['blue','pink'])
plt.show()

#=========================================================================================
#Where do people go to Black Friday sales most often?
value = df[df['columns57']=='Yes']['columns64'].value_counts().tolist()
name = df[df['columns57']=='Yes']['columns64'].unique().tolist()

name.pop()

name = tuple(name)
plt.pie(value,labels=name)

#========================================================================================
#Is there a correlation between praying on Thanksgiving and income?
YP = df[df['columns51']=='Yes']['columns63'].mean()
NP = df[df['columns51']=='No']['columns63'].mean()
plt.pie([YP,NP],labels=['y Pray','y Not Pray'],autopct='%1.1f%%',shadow=True, startangle=90)

#================================================================================================
#What income groups are most likely to have homemade cranberry sauce?
Ic = df[df['columns8']=='Homemade']['columns63'].value_counts().tolist()
valueIC = tuple(df[df['columns8']=='Homemade']['columns63'].unique())

plt.pie(Ic,labels=valueIC)
   
#==============================================================================================   
##Verify a pattern:
#        People who have Turducken and Homemade cranberry sauce seem to have 
#        high household incomes.
#        People who eat Canned cranberry sauce tend to have lower incomes, 
#        but those who also have Roast Beef have the lowest incomes
#        
#    Find the number of people who live in each area type (Rural, Suburban, etc)
#    who eat different kinds of main dishes for Thanksgiving:

df[df['columns2']=='Turducken'][['columns8','columns63','columns2']]

# homemade average income
var = df[(df['columns2']=='Turducken') & \
           (df['columns8'] == 'Homemade')
        ].mean()[-1]

# find all the values who has
df[df['columns2']=='Roast beef'][['columns63','columns8','columns2']]

# average income of Canned
var_2 = df[(df['columns8'] == 'Canned') & \
               (df['columns63'] == df['columns63'])
        ].mean()[-1]

# average income of canned roast beef
var_3 = df[(df['columns2'] =='Roast beef') & \
               (df['columns8'] == 'Canned') & \
               (df['columns63'] == df['columns63'])
        ].mean()[-1]


# store the incomes in the list
verify_val = [var,var_2,var_3]
# lets plot the values of the
plt.pie(verify_val,labels=['Homemade','Canned','Roast Beef'])































   
















