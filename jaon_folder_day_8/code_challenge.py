# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:54:16 2019

@author: BSDU ADMIN
"""


"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests
user = int(input("enter your dolar::"))
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=6273930dbd8ec6e7f2fa"

response = requests.get(url)

response.content


data = response.json()["USD_INR"]*user
print(round(data ,2))

################################## simpal code######################
user = int(input("enter the number"))
c = user*71.388504
print(c)