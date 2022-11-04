from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path='D:\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
username=['standard_user','locked_out_user']
password=['secret_sauce','demo_sauce']
for i in range(len(username)):
    driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys(username[i])
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password[i])
    driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
    if driver.current_url == 'https://www.saucedemo.com/inventory.html':
        print("Test case passed")
        driver.get('https://www.saucedemo.com/')
    else:
        print("Test case failed")    
    time.sleep(5)
driver.close()