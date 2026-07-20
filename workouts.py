from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
a=webdriver.Edge()
a.maximize_window()
a.get("https://techbeamers.com/selenium-practice-test-page/")
t.sleep(5)
un=a.find_element(By.XPATH,"//*[@id='username']")
un.send_keys("naveen")
t.sleep(3)
print(un.get_attribute("class"))#gets the attribute name
print(un.get_attribute("ID"))#gets the attribute name
print(un.get_attribute("maxlength"))#gets the attribute name
print(un.get_attribute("placeholder"))#gets the attribute name
print(un.get_attribute("type"))#gets the attribute name
una=a.find_element(By.XPATH,"//*[@id='username']").value_of_css_property("background-color")#gets the css property
print(una)
une=a.find_element(By.XPATH,"//*[@id='username']").is_enabled()#checks if it is enabled
print(une)
unk=a.find_element(By.XPATH,"//*[@id='username']").is_displayed()#checks if it is displayed
print(unk)
uns=a.find_element(By.XPATH,"//*[@id='username']").is_selected()#checks if it is seleected
print(uns)
unl=a.find_element(By.XPATH,"//*[@id='username']").location#gives its location as x&y coordinates=>{'x': 245, 'y': 1180}
print(unl)