import time as t
from asyncio import print_call_graph

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
'''# TC_CART_014 - Verify Subtotal Calculation
edge.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
edge.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
prices = edge.find_elements(By.CLASS_NAME, "inventory_item_price")
price1 = float(prices[0].text.replace("$", ""))
price2 = float(prices[1].text.replace("$", ""))
expected_subtotal = price1 + price2
edge.find_element(By.CLASS_NAME, "shopping_cart_link").click()
t.sleep(2)

edge.find_element(By.ID, "checkout").click()
t.sleep(2)
edge.find_element(By.ID, "first-name").send_keys("Naveen")
edge.find_element(By.ID, "last-name").send_keys("Prabu")
edge.find_element(By.ID, "postal-code").send_keys("636304")

edge.find_element(By.ID, "continue").click()
t.sleep(2)

item_total = edge.find_element(By.CLASS_NAME, "summary_subtotal_label").text

print(item_total)
actual_subtotal = float(item_total.replace("Item total: $", ""))

print("Actual Subtotal :", actual_subtotal)
if expected_subtotal == actual_subtotal:
    print("TC_CART_014 Passed")
else:
    print("TC_CART_014 Failed")

#TC_CART_015 verify tax calculation
tax = edge.find_element(By.CLASS_NAME, "summary_tax_label").text

print(tax)
actual_tax = float(tax.replace("Tax: $", ""))

print(actual_tax)

if actual_tax > 0:
    print("TC_CART_015 Passed")
else:
    print("TC_CART_015 Failed")'''

#TC_CART_016 verify grand total
'''subtotal = edge.find_element(
    By.CLASS_NAME,
    "summary_subtotal_label"
).text

subtotal = float(subtotal.replace("Item total: $", ""))

tax = edge.find_element(
    By.CLASS_NAME,
    "summary_tax_label"
).text

tax = float(tax.replace("Tax: $", ""))

grand = edge.find_element(
    By.CLASS_NAME,
    "summary_total_label"
).text

grand = float(grand.replace("Total: $", ""))

expected = subtotal + tax
if expected == grand:
    print("TC_CART_016 Passed")
else:
    print("TC_CART_016 Failed")
'''
#TC_CART_017 verify empyt cart
'''edge.find_element(By.CLASS_NAME, "shopping_cart_link").click()

items = edge.find_elements(By.CLASS_NAME, "cart_item")

if len(items) == 0:
    print("TC_CART_017 Passed")
else:
    print("TC_CART_017 Failed")'''

#TC_CART_019 verify cart after refersh
edge.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

badge = edge.find_element(
    By.CLASS_NAME,
    "shopping_cart_badge"
).text

print("Before Refresh :", badge)

edge.refresh()

badge2 = edge.find_element(
    By.CLASS_NAME,
    "shopping_cart_badge"
).text

print("After Refresh :", badge2)

if badge == badge2:
    print("TC_CART_020 Passed")
else:
    print("TC_CART_020 Failed")