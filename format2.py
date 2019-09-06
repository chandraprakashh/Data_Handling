# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:29:09 2019

@author: Administrator
"""


"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""
# Input:
import math

user = "Welcome to pink city jaipur"

c  = user.replace(" " , "*")

print (c)