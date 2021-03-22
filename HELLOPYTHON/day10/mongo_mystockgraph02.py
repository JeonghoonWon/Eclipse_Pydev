import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
stock = db.stock
arr = []    
rows = stock.find_one()
print(rows)

for row in rows:
    arr.append(row)
    
print(arr)