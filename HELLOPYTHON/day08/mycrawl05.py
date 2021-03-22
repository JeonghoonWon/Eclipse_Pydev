'''
Created on 2021. 3. 17.

@author: Josh
'''

import requests
from bs4 import BeautifulSoup
 
response = requests.get('http://localhost/MYSERVER/secret')
 
html = response.text

#print(html)
 
soup = BeautifulSoup(html, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)


