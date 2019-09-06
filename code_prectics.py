# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:39:34 2019

@author: Administrator
"""

#s1 =["ram","ravi","rahul","gopal"]
#s2 ="chandraprakash"
#
#for item in s1:
#    print(item)
#   
#for item in s2:
#    print(item)
#    
#index = 0
#for item in s1:
#    print(index, item)
#    index += 1


"""
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]      
Since you're super hungry and super excited about lunch,
enumerate over the array and append an "!" ("exclamation mark") 
to each menu item. 
"""
    
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"] 
obj1 = enumerate(lunch_menu)  
print (list(enumerate(lunch_menu)))


# Hands On 2  
"""
nums = [1, 2, 3, 4]
Enumerate over the array and return a new array of the
squares of those numbers.
"""
nums = [1, 2, 3, 4]
for index,ele in enumerate(nums,1):     
    print (index," ", ele**2) 
    
    
# Hands On 3  
"""
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
iterate over the array and return any even numbers. 
iterate over the array and return only the first array element that is odd

"""
        
  
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]

index = 0

for i in odds_and_evens:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
        
# Hands On 4  
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
We all know that cats and dogs don't get along. 
Iterate over the array and delete the elements that represent dogs.
"""

cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
while "dog" in (cats_and_dogs):
     cats_and_dogs.remove("dog")
print(cats_and_dogs)

        
# Hands On 5  
"""
famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]
check and see if the array includes the string "Maru"
"""

famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]
for i in famous_cats:
    if i=="Maru":
        print("true")


# Hands On 6
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]
terate over the array to determine if any of the words contained there are loud (upcased).
"""
for i in famous_cats:
    if i=="":
        print("")


















        
        

      
    





























    
    