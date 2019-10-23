# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:57:08 2019

@author: BSDU ADMIN
"""

from bs4 import BeautifulSoup   
import requests



from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"


browser = webdriver.Chrome("c:/chromedriver.exe")


browser.get(url)

sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)



get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')

get_school_result.click()


sleep(20)
 
html_page = browser.page_source

soup = BS(html_page,"lxml")



sleep(10)





right_table=soup.find('table',id='Table4')


print (right_table)


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]



for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 13:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        G.append(cells[6].text.strip())
        H.append(cells[7].text.strip())
        I.append(cells[8].text.strip())
        J.append(cells[9].text.strip())
        K.append(cells[10].text.strip())
        L.append(cells[11].text.strip())
        M.append(cells[12].text.strip())
        
        
        
from collections import OrderedDict

col_name = ["Reh.no","Name","I Lang-I","I Lang-II","Eng","hindi","Social Science","Phy","Chem","Bio","Maths","IT","Result"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G,H,I,J,K,L,M]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
print (df)

