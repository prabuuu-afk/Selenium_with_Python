import time as t
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
a=webdriver.Edge()
a.maximize_window()
a.get("https://demoqa.com/menu")
t.sleep(2)
menu=a.find_element(By.XPATH,"//*[@id='nav']/li[2]/a")
actions=ActionChains(a)
actions.move_to_element(menu)\
.click()\
.perform()
t.sleep(3)