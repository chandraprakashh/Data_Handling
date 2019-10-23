# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:59:48 2019

@author: BSDU ADMIN
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "https://bidplus.gem.gov.in/bidlists"



browser = webdriver.Chrome("c:/chromedriver.exe")


browser.get(url)


for i in range(1,11):
    bid_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    bid_result.click()


























