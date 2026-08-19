from selenium import webdriver


def before_all(context):
    print("Starting browser...")
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


def after_all(context):
    print("Closing browser...")
    context.driver.quit()