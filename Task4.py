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
"""cart=edge.find_element(By.XPATH,value="//button[@id= 'add-to-cart-sauce-labs-backpack']")
cart.click()
t.sleep(5)"""
#TC_CART_002 add 2 product to the cart
'''edge.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
edge.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()'''
#TC_CART_003 add same products multiple times
'''r=edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
k=edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
t.sleep(5)'''#it will not work due to the website's rule a product can be added to the cart only once
#TC_CART_004 remove product
"""edge.find_element(By.ID,"remove-sauce-labs-backpack").click()
basket=edge.find_elements(By.CLASS_NAME,"shopping_cart_badge")
if len(basket)==0:
    print("empty")
else:
    print(len(basket))"""
#TC_CART_005 remove product from the cart
'''edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
edge.find_element(By.CLASS_NAME,"shopping_cart_link").click()
edge.find_element(By.ID,"remove-sauce-labs-backpack").click()
bas=edge.find_elements(By.CLASS_NAME,"shopping_cart_badge")
t.sleep(5)
if len(bas)==0:
    print("cart is empty")
else:
    print(f"cart has {len(bas)} items")'''
#TC_CART_013 verify item price
'''edge.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
price=edge.find_element(By.CLASS_NAME,"inventory_item_price").text
print(price)
edge.find_element(By.CLASS_NAME,"shopping_cart_link").click()
inside_price=edge.find_element(By.CLASS_NAME,"inventory_item_price").text
print(inside_price)
if price==inside_price:
    print("TC_CART_013 passed")
else:
    print("TC_CART_013 failed")'''