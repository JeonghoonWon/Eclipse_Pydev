import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
sample = db.sample

doc = [
    {'col01':'1','col02':'2','col03':'3'},
    {'col01':'2','col02':'3','col03':'4'},
    {'col01':'3','col02':'4','col03':'5'}

    ]
cnt = sample.insert_many(doc)
# insert 를 하면 _id 가 자동으로 생긴다.
print("cnt",cnt)
