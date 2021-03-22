from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser = webdriver.Chrome(파일경로)
driver = webdriver.Chrome('chromedriver.exe')


url = 'http://localhost/MYSERVER/login.html'
driver.get(url)

driver.find_element_by_id('u_name').send_keys('abe')
driver.find_element_by_id('pwd').send_keys('1')
driver.find_element_by_id('mysubmit').click()


#driver.implicitly_wait(3)
time.sleep(1)


url = 'http://localhost/MYSERVER/secret'
driver.get(url) # 현재 상태를 가지고온다.

print(driver.page_source)


    
   
    


