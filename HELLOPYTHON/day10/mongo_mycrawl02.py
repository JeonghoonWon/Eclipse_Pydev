import pymongo
import datetime

def insertStock(s_code,s_name,s_price,yyyymmdd_hhmm): 
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    

    doc = {'s_code':s_code,'s_name':s_name,'s_price':s_price,'in_date':yyyymmdd_hhmm}
    stock.insert_one(doc)
    # insert 를 하면 _id 가 자동으로 생긴다.
    
    
if __name__ == '__main__':
    insertStock('1','1','1','1')