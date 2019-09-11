# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:52:29 2019

@author: BSDU
"""

"""
Code Challenge 7

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.

"""

#import csv
#>>> with open("https://github.com/thecbp/blog_data/blob/master/recipeData.csv") as csvfile:
#...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#...     for row in spamreader:
#...         print ', '.join(row)
#


import csv 
def data():
    file = open("C:/Users/BSDU.DESKTOP-M155C05/Documents/ML_&_AI/Data_handling/Day_04/recipeData.csv",encoding="ISO-8859-1")
    for i in file:
        yield i 

data_row = data()

list2 =[]
while True:
    a = next(data_row)
    list2.append(a)
print(list2[7])



