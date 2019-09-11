# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:46:43 2019

@author: BSDU
"""


"""
Code Challenge 1
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""


def number_generator():
    yield(7)
    yield(13)
    yield(17)
    yield(231)
    yield(12)
    yield(8)
    yield(3)
    
v = list()
    

num = number_generator()
for i in range(1,8):
    n = next(num)
    v.append(n)
    print(sum(v) / len(v))
           







