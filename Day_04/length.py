# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:34:28 2019

@author: BSDU
"""

"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""
name = ['chandra', 'prakash', 'jeengar', 'raila']

# Write a code using simple for loop
word_dict=dict()

for word in name:
    word_dict[word] = len(word)    

print(word_dict)
