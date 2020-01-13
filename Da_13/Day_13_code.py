"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""

#1. Which Male and Female Professor has the highest and the lowest salaries
import pandas as pd
data = pd.read_csv('D:\\LakshyaJain\\DBwithPy\\Salaries.csv')
df = pd.DataFrame(data)

df.groupby('sex')['salary'].max()
df.groupby('sex')['salary'].min()

'OR'

df[df['rank']=='Prof'][df['sex']=='Male']['salary'].max()
df[df['rank']=='Prof'][df['sex']=='Female']['salary'].max()
df[df['rank']=='Prof'][df['sex']=='Male']['salary'].min()
df[df['rank']=='Prof'][df['sex']=='Female']['salary'].min()

#2. Which Professor takes the highest and lowest salaries.
df[df['rank']=='Prof']['salary'].max()
df[df['rank']=='Prof']['salary'].min()


#3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
list1=[1,2,3,4,5]
from statistics import mean

list1.mean()
if(df[df['service']]==df[df['service']]):
    list1.append(df)

df["salary"].fillna( df['salary'].mean(), inplace = True) 
