import time as t
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
a=webdriver.Edge()
a.maximize_window()
'''a.get("https://demoqa.com/menu")
t.sleep(2)
menu=a.find_element(By.XPATH,"//*[@id='nav']/li[2]/a")
actions=ActionChains(a)'''
#move to element
'''actions.move_to_element(menu).perform()
t.sleep(3)'''
#click()
'''actions.move_to_element(menu)\
    .click()\
    .perform()
t.sleep(3)'''
#right click
'''a.get("https://demoqa.com/buttons")
t.sleep(2)'''
'''button=a.find_element(By.XPATH,"//*[@id='rightClickBtn']")
act=ActionChains(a)
act.context_click(button).perform()
t.sleep(3)'''
#double click
'''button=a.find_element(By.XPATH,"//*[@id='doubleClickBtn']")
act=ActionChains(a)
act.double_click(button).perform()'''
#hold and release
'''a.get("https://jqueryui.com/droppable/")
t.sleep(2)
button=a.find_element(By.ID,value="draggable")
act=ActionChains(a)
act.click_and_hold(button)\
    .release(button)\
    .perform()
t.sleep(3)'''#not performing
#drag and drop
a.get("https://jqueryui.com/droppable/")
t.sleep(2)
'''a.switch_to.frame(0)#switching to iframe
act=ActionChains(a)
source=a.find_element(By.XPATH,"//*[@id='draggable']")
dest=a.find_element(By.XPATH,"//*[@id='droppable']")
act.drag_and_drop(source,dest).perform()
t.sleep(3)
a.switch_to.default_content()#returing to normal frame'''