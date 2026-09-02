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
Subjects=chrome.find_element(By.XPATH,'//*[@id="subjects"]')
hobbies=chrome.find_elements(By.XPATH,'//input[@type="checkbox" and @class="form-check-input mt-0"]')
address=chrome.find_element(By.CLASS_NAME,value="form-control")
#values
Name.send_keys("Naveen")
Email.send_keys("naveen@gmail.com")
Gender[0].click()
Mobile.send_keys("8903636777")
t.sleep(2)
print(Name.get_attribute("value"))
Subjects.send_keys("Computer science")
hobbies[0].click()
address.send_keys("jrougofhoghg")
t.sleep(3)
#for i in Gender:
#    print(i.get_attribute("label"),end=" ")
