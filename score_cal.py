# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:32:45 2019

@author: Administrator
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
#Lets assume there are 3 assignments
Assignment_1 = float(input("enter the first number"))
Assignment_2 = float(input("enter the second number"))
Assignment_3 = float( input("enter the third number"))

#exams, each with max score of 100
Assignment_4 = float(input("enter the fourth number"))
Assignment_5 = float(input("enter the fifth number"))


weighted_score = (((Assignment_1 + Assignment_2 + Assignment_3 ) *0.1) + ((Assignment_4 + Assignment_4 ) * 0.35))

print("Total Assignment score ={}".format(weighted_score))

#each with max score
