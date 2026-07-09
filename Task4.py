import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge= webdriver.Edge()
edge.maximize_window()
edge.get("https://www.saucedemo.com/")
t.sleep(5)
un=edge.find_element(By.XPATH,value="//input[@id= 'user-name']")
un.send_keys("standard_user")
ps=edge.find_element(By.XPATH,value="//input[@name= 'password']")
ps.send_keys("secret_sauce")
lo=edge.find_element(By.XPATH,value="//input[@id= 'login-button']")
lo.click()
t.sleep(5)
#TC_CART_001 add product to the cart
'''cart=edge.find_element(By.XPATH,value="//button[@id= 'add-to-cart-sauce-labs-backpack']")
cart.click()
t.sleep(5)'''
#TC_CART_002 add 2 product to the cart
'''edge.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
edge.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()'''
#TC_CART_003 add same products multiple times
r=edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
k=edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
t.sleep(5)#it will not work due to the website's rule a product can be added to the cart only once