# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:04:59 2019

@author: Administrator
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
#import math
import  math

#user number. 
number= int(input("enter the number"))

#Factorial of 3 = 3 * 2 * 1= 6 
factorial_number = math.factorial(number)

#factorial of a number. 
print("factorial number is ={}".format(factorial_number))