from selenium import webdriver
def before(context):
    context.driver=webdriver.edge()
    context.driver.maximize_window()
def after(context):
    context.driver.quit()