# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:19:53 2019

@author: BSDU ADMIN
"""

import pymongo

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

#client = pymongo.MongoClient("mongodb://forsktech:Forsk%40123@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

client = pymongo.MongoClient("mongodb://text1:2gVMABrQQnm4tzD7@test1-shard-00-00-u3nkz.mongodb.net:27017,test1-shard-00-01-u3nkz.mongodb.net:27017,test1-shard-00-02-u3nkz.mongodb.net:27017/test?ssl=true&replicaSet=test1-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.db_school


def add_costmor(name, age, roll_number, branch):
    unique_costmor = mydb.Data2.find_one({"id":age})
    if unique_costmor:
        return "costmor already exists"
    else:
        mydb.Data2.insert_one(
                {
                "Name" : name,
                "Age" : age,
                "Roll_number" : roll_number,
                "Branch" : branch
                })
        return "costmor added successfully"


def fetch_all_costmor():
    user = mydb.Data2.find()
    for i in user:
        print (i)


#Drop a collection in Mongo
#mydb.Data.drop()

#Insert data in collection
add_costmor('abhishek' ,17, '180612S0011',  'ml&ai')
add_costmor('chandu'  ,18, '180612S0018',  'ml&ai')
add_costmor('vishal'  ,18, '180612S0014',  'ml&ai')
add_costmor('lokesh'  ,18, '180612S0017',  'ml&ai')
add_costmor('sapana'  ,20, '180612S0014',  'ml&ai')
add_costmor('lakshya' ,18, '180612S0012',  'ml&ai')
add_costmor('lakshya' ,18, '180612S0012',  'ml&ai')
add_costmor('rahul'   ,18, '180612S0019',  'ml&ai')
add_costmor('ravi'    ,19, '180612S0010',  'ml&ai')
add_costmor('govind'  ,15, '180612S0011',  'ml&ai')
add_costmor('dinesh'  ,18, '180612S0013',  'ml&ai')
add_costmor('lavish'  ,16, '180612S0018',  'ml&ai')
add_costmor('nishu'   ,18, '180612S0010',  'ml&ai')




fetch_all_costmor()


