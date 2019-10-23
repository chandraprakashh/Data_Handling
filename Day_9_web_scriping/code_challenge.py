# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:12:57 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup   
import requests

cricket = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print (cricket)

soup = BeautifulSoup(cricket,"lxml")
#print (soup)

print (soup.prettify())

print (soup)
print (soup.div.table)

right_table=soup.find('table', class_="table")


print (right_table)


A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
        
from collections import OrderedDict

col_name = ["Pose","Team ","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
print (df)



########################################################################################


from bs4 import BeautifulSoup   
import requests

cricket = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i").text
print (cricket)

soup = BeautifulSoup(cricket,"lxml")
#print (soup)

print (soup.prettify())

print (soup)
print (soup.div.table)

right_table=soup.find('table', class_="table")


print (right_table)


A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
        
from collections import OrderedDict

col_name = ["Pose","Team ","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
print (df)

##############################################################################################

from bs4 import BeautifulSoup   
import requests

cricket = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/test").text
print (cricket)

soup = BeautifulSoup(cricket,"lxml")
#print (soup)

print (soup.prettify())

print (soup)
print (soup.div.table)

right_table=soup.find('table', class_="table")


print (right_table)


A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
        
from collections import OrderedDict

col_name = ["Pose","Team ","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
print (df)

