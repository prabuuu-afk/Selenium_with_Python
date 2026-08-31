import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome=webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
t.sleep(2)
print("Link opened!!!")
Name=chrome.find_element(By.ID,"name")
Email=chrome.find_element(By.ID,"email")
Gender = chrome.find_elements(By.XPATH, '//input[@type="radio"]')
#print(Gender[0])
Mobile=chrome.find_element(By.NAME,"mobile")
#Mobile.send_keys("8903636777")
#print(Mobile.get_attribute("placeholder"))
Name.send_keys("Naveen")
Email.send_keys("naveen@gmail.com")
Gender[0].click()
Mobile.send_keys("8903636777")
t.sleep(2)