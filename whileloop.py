# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:39:43 2019

@author: Administrator
"""

"""Hands On 1
# Print all the numbers from 1 to 10 using condition in while loop

"""

"""
Hands On 3
#  Print all the even numbers from 1 to 10 using condition in while loop

"""
"""
Hands On 5
#  Print all the odd numbers from 1 to 10 using condition in while loop

"""
# Print all the numbers from 1 to 10 using condition in while loop
user = 1
while user <= 9:
    print(user)
    user += 1
else:
    print("1 to 10 number :-", user)
 
    
#even number
number =1
while number <= 10:
    if number % 2 == 0:
        print("even number:-","{0}".format(number))
    number = number + 1
    
    
#odd number
number =1
while number <= 10:
    if number % 2 != 0: 
        print("odd number:-","{0}".format(number))
    number = number + 1
    