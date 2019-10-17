# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:09:04 2019

@author: BSDU ADMIN
"""

import json

json_string = """
{
	"faculti_name": {
		"first_name": "mnoj",
		"last_name": "gurjar",
		"school_of": "computing_skills",
		"age": 24,
		"address": "bhilwara"
	}
}
"""
print(json_string)
with open("fac.json", "w") as write_file:
    json.dump(json_string, write_file)
   
with open("fac.json", "r") as read_file:
    jsondata=json.load(read_file)
    print(jsondata)