from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
chrome= webdriver.Chrome()
chrome.maximize_window()
#getting into a website
chrome.get("https://www.saucedemo.com/")
#t.sleep(2)
#login into that website
un=chrome.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")
ps=chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")
btn=chrome.find_element(By.ID,"login-button").click()
t.sleep(2)
print("Executed!!!")
#adding an element into cart
chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
t.sleep(5)
print("added 1 element")