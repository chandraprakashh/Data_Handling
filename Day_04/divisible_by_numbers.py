# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:39:54 2019

@author: BSDU
"""

"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by

"""

my_dict= max([i for i in range(1,1000) if i%3==0 if range(i,10)])
print(my_dict)