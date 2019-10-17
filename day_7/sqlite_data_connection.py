# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:37:04 2019

@author: BSDU ADMIN
"""

import sqlite3

from pandas import DataFrame

conn = sqlite3.connect('costmor.db')


c = conn.cursor()

c.execute('DROP TABLE costmor')

conn.commit()

c.execute ("""CREATE TABLE costmor(
          name  VARCHAR,
          student_age INTEGER,
          student_roll_number INTEGER,
          student_Branch VARCHAR
          
          )"""
          )

conn.commit()


c.execute("INSERT INTO costmor VALUES ('abhishe' ,17, '180612S0011',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('chandU'  ,18, '180612S0018',  'ml&ai' )")
c.execute("INSERT INTO costmor VALUES ('vishal'  ,18, '180612S0014',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('lokesh'  ,18, '180612S0017',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('sapana'  ,20, '180612S0014',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('lakshya' ,18, '180612S0012',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('rahul'   ,18, '180612S0019',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('ravi'    ,19, '180612S0010',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('govind'  ,15, '180612S0011',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('dinesh'  ,18, '180612S0013',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('lavish'  ,16, '180612S0018',  'ml&ai')")
c.execute("INSERT INTO costmor VALUES ('nishu'   ,18, '180612S0010',  'ml&ai')")

conn.commit()


c.execute("SELECT * FROM costmor")


print(c.fetchone())
print(c.fetchmany(5))
print(c.fetchall())


