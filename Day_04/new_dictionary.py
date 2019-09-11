# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:40:35 2019

@author: BSDU
"""

"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""

my_dict = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9,}
my_dict = {key: value ** 2 for key, value in my_dict.items() if value %2==0}
print(my_dict)


my_dict={i: i**2 for i in range(1,11) if i %2==0}
print(my_dict)