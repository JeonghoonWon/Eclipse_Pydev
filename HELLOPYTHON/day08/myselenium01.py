from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser = webdriver.Chrome(파일경로)
driver = webdriver.Chrome('chromedriver.exe')


url = 'http://localhost/MYSERVER/login'
driver.get(url)

time.sleep(1)

url = 'http://localhost/MYSERVER/secret'
driver.get(url) # 현재 상태를 가지고온다.

print(driver.page_source)