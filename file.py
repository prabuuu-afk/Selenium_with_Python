#worked in By.Name
'''import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

a = webdriver.Edge()
a.maximize_window()

a.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
t.sleep(30)
un = a.find_element(By.NAME, "username")
un.send_keys("Admin")
pa = a.find_element(By.NAME, "password")
pa.send_keys("admin123")
login = a.find_element(By.XPATH, "//button[@type='submit']")
login.click()
t.sleep(5)

a.quit()'''

#Worked in XPath
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge=webdriver.Edge()
edge.maximize_window()
edge.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
t.sleep(15)
un=edge.find_element(By.XPATH,"//input[@name='username']")
un.send_keys("Admin")
pa=edge.find_element(By.XPATH,value="//input[@name='password']")
pa.send_keys("admin123")
lgn=edge.find_element(By.XPATH,value="//button[@type='submit']")
lgn.send_keys(Keys.ENTER)
t.sleep(15)