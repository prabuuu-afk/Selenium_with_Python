import selenium
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
a=webdriver.Edge()
a.maximize_window()
a.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
a.find_element(By.ID).send_keys('')#use to give input values
t.sleep(5)
a.find_element(By.XPATH)
t.sleep(10)
a.find_element(By.CLASS_NAME).send_keys(''+Keys.ENTER)
t.sleep(5)