# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:33:49 2019

@author: BSDU ADMIN
"""

import json 

json_string = """
{
	"student_name": {
		"first_name": "rahul",
		"last_name": "jeengar"
	},
    "datils": {
	"school": "ml&ai",
	"age": 19,
	"reg.no.": "180162s008",
	"phone": [9680603502, 8233317920],
	"job": null,
	"collage_student": true,
	"hobbies_singing": false
    },
    	"address":{
		"t": "bhagrota",
		"p": "bhilwara"
	}
}
"""
print (json_string)
my_data = json.loads(json_string)
print (type(my_data))
print(my_data)
print(my_data["student_name"])
print(my_data["datils"])
print(my_data["address"])
print(my_data["address"]["t"])

