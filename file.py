import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

a = webdriver.Edge()
a.maximize_window()

a.get("https://www.youtube.com/")

sb = a.find_element(By.ID, "search")
sb.send_keys("rick roll")
sb.send_keys(Keys.ENTER)

t.sleep(500)

a.quit()