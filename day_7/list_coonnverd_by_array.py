# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:26:32 2019

@author: BSDU ADMIN
"""
import numpy as np
user = int(input("enter the number:"))
list1 = []
for i in range (1,6):
    user = int(input("enter the number:"))
    list1.append(i)
    np.array(list1)
    
    
live = ["81","32","7","32","81","81","7","9","32","9"]

this = {}

for i in live:
    this[i]= this.get(i,0)+1
print(str(this))



number = [1,2,3,4,5,6]
tuple(number)



x = '81'
y = '91'
z = eval(x) + eval(y)
print (z)


 
