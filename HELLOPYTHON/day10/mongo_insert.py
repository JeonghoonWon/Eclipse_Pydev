import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
sample = db.sample

doc = {'col01':'1','col02':'2','col03':'3'}


sample.insert_one(doc)
# insert 를 하면 _id 가 자동으로 생긴다.