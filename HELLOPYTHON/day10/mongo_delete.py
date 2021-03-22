import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
sample = db.sample


cnt = db.sample.delete_many({'col01':'2'})
print(cnt)

