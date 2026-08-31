'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
chrome= webdriver.Chrome()
chrome.maximize_window()
#getting into a website
chrome.get("https://www.saucedemo.com/")
t.sleep(2)
#login into that website
un=chrome.find_element(By.XPATH,'//*[@id="user-name"]').send_keys("standard_user")
ps=chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys("secret_sauce")
btn=chrome.find_element(By.ID,"login-button").click()
t.sleep(2)
print("Executed!!!")
'''
'''#adding an element into cart
chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
t.sleep(5)
print("added 2 elements")
#getting into cart
chrome.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
samp=chrome.find_elements(By.XPATH,'//*[@id="shopping_cart_container"]/a')
t.sleep(5)
print("in the cart",end=" ")
print(len(samp))
#web element methods
txt=chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
print(txt.text)
print(txt.get_attribute("class"))#btn btn_primary btn_small btn_inventory
print(txt.get_attribute("id"))
print(txt.is_displayed())
#chrome.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
print(txt.value_of_css_property("background-color"))'''
import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome=webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
t.sleep(2)
radio=chrome.find_element(By.XPATH,'//*[@id="gender"]')
radio.click()
print(radio.is_selected())#True
print(radio.location)#{'x': 772, 'y': 307}
#browser navigation methods
chrome.back()
chrome.forward()
chrome.refresh()
t.sleep(2)
from selenium.webdriver.support.ui import Select
dropdownlist=Select(chrome.find_element(By.XPATH,'//*[@id="state"]'))
dropdownlist.select_by_value("NCR")
chrome.save_screenshot("D:\Selinium_with_python\screenshot.jpg")#takes screen shots and stores in the location we given and the name we have given
t.sleep(3)