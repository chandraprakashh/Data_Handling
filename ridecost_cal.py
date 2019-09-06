# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:19:42 2019

@author: Administrator
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""    
#Assume you travel 80 km to and fro in a day
Travel = 80

#Cost of Diesel per litre is 80 INR 
Diesel = 80

#Your vehicle Fuel Average is 18 km/litre.

Fuel_Average = 18 

total_driving = (Diesel/Fuel_Average)*Travel

print("per day office ={}".format(total_driving))