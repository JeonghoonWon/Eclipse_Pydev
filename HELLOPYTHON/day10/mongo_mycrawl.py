
from bokeh.core.property.datetime import Datetime
from bs4 import BeautifulSoup
import pymysql
import requests
import time

from datetime import datetime

import sys

import pymongo

 

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
stock = db.stock

#doc = {'col01':'1','col02':'2','col03':'3'}



# insert 를 하면 _id 가 자동으로 생긴다.

#sql = """insert into stock (s_code, s_name, s_price, in_date) values(%s, %s, %s, %s)"""

#conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
#curs = conn.cursor()

for i in range(10):
    print("i",i)
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    
    now = datetime.now() 
    formatted_date = now.strftime('%Y%m%d.%H%M%S')
        
    print(formatted_date)
    for info in soup.select('.tbody'):
        s_name = info.dt.text # s_name
        s_code_text = info.dd["id"] 
        s_code = info.dd["id"][len(s_code_text)-6:len(s_code_text)] #s_code
        s_price = info.dd.span.text.replace(",","") #s_price
        #curs.execute(sql, (num, title, price, formatted_date))
        #print(title, "/", num, "/", price)
        #print("-----------------------------------------------")
        stock.insert_one({"s_name":s_name,"s_code":s_code,"s_price":s_price,"in_date":formatted_date})
    # print(text, end="\t") 끝에 탭을 추가한다. 
#   conn.commit()
    time.sleep(60)

#conn.close()
connection.close()
    
        
    

