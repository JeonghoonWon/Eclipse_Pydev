'''
Created on 2021. 3. 17.

@author: Josh
'''
  
#ID : QHxqLn_sL5OOF5F23uTj
#Secret : 3LxXpMtORE

import os
import sys
import urllib.request
from bs4 import BeautifulSoup
client_id = "QHxqLn_sL5OOF5F23uTj"
client_secret = "3LxXpMtORE"
encText = urllib.parse.quote("기아차")
url = "https://openapi.naver.com/v1/search/blog.xml?display=100&sort=date&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    soup = BeautifulSoup(response_body, 'xml')
    print(soup)
    print(soup.decode('utf-8'))
    for info in soup.select('item'):
        title = info.title.text.replace('<b>', '').replace("</b>", "")
        link = info.link.text
        desc = info.description.text.replace('<b>', '').replace("</b>", "")
        blogName = info.bloggername.text
        blog = info.bloggerlink.text
        postdate = info.postdate.text
        
        print(title, "\n", link, "\n",  desc, "\n" , blogName, "\n", blog , "\n", postdate, "\n")
else:
    print("Error Code:" + rescode)


