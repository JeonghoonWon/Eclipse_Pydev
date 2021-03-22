import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
sample = db.sample

row = sample.find_one()
print(row)
print("=================================================")
rows = sample.find()
for r in rows:
    print(r)
print("=================================================")
for x in sample.find():
    print(x)

print("=================================================")

rows = sample.find({'col01':'1'})
for r in rows:
    print(r)