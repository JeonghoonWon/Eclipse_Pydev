from _datetime import datetime

from bokeh.core.property.datetime import Datetime
from bs4 import BeautifulSoup
import pymysql
import requests


response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
text = response.text

# print(text)
 
soup = BeautifulSoup(text, 'html.parser')
 
from datetime import datetime
now = datetime.now()

sql = """insert into stock (s_code, s_name, s_price, in_date) values(%s, %s, %s, %s)"""

conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
curs = conn.cursor()
formatted_date = now.strftime('%Y%m%d.%H%M')

for info in soup.select('.tbody'):
    title = info.dt.text
    str = info.dd["id"]
    num = info.dd["id"][len(str)-6:len(str)]
    price = info.dd.span.text.replace(",","");
    
    print(title, "/", num, "/", price)
    print("-----------------------------------------------")
    
# print(text, end="\t") 끝에 탭을 추가한다. 
    
    curs.execute(sql, (num, title, price, formatted_date))
    
conn.commit() 

conn.close()