

    
    






from bokeh.core.property.datetime import Datetime
from bs4 import BeautifulSoup
import pymysql
import requests
import time

from datetime import datetime


sql = """insert into stock (s_code, s_name, s_price, in_date) values(%s, %s, %s, %s)"""

conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
curs = conn.cursor()

for i in range(10):
    print("i",i)
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    
    now = datetime.now() 
    formatted_date = now.strftime('%Y%m%d.%H%M%S')
        
    print(formatted_date)
    for info in soup.select('.tbody'):
        title = info.dt.text
        str = info.dd["id"]
        num = info.dd["id"][len(str)-6:len(str)]
        price = info.dd.span.text.replace(",","");
        curs.execute(sql, (num, title, price, formatted_date))
        #print(title, "/", num, "/", price)
        #print("-----------------------------------------------")
        
    # print(text, end="\t") 끝에 탭을 추가한다. 
    conn.commit()
    time.sleep(60)

conn.close()
    
        
    

