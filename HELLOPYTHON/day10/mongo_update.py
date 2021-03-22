import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
sample = db.sample

cnt = sample.update_many({'col01':'2'},{"$set":{'col02':'7','col03':'7'}})
print(cnt)



