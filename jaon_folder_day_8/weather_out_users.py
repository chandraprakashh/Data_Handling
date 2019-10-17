# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:56:24 2019

@author: BSDU ADMIN
"""



import requests


url1 = "http://api.openweathermap.org/data/2.5/weather/?q="
url2 = input("enter the city name::-")
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)

response = requests.get(url)

response.content

print (type(response.content))
data = response.json()


t = data["main"]["temp"]

c = t-273.15
print(round(c,2))

import time
dir(time)

sun.ctime = data["sys"]["sunset"]


sun.ctime = data["sys"]["sunset"]









