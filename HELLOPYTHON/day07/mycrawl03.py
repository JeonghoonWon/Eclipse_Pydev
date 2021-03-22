'''
Created on 2021. 3. 17.

@author: Josh
'''

import requests
from bs4 import BeautifulSoup
 
response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
html = response.text

#print(html)
 
soup = BeautifulSoup(html, 'html.parser')

#table01 = soup.find('dl',{'class':'.tbody'})

#print(table01)

for info in soup.select('.tbody'):
    
    s_name = info.dt.text
    s_price = info.dd.span.text
    s_code_txt = info.dd['id'] 
    s_code = s_code_txt[len(s_code_txt)-6:len(s_code_txt)]
    
    print(s_name ,end="\t")
    print(s_price, end="\t")
    print(s_code)

   
print("========================================")     


    
    





