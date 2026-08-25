from behave import given, when, then
import time as t


@given("the user opens the login page")
def open_login(context):
    context.driver.get("https://the-internet.herokuapp.com/login")


@when("the user enters valid username and password")
def enter_valid_credentials(context):
    context.driver.find_element("id", "username").send_keys("tomsmith")
    context.driver.find_element(
        "id", "password"
    ).send_keys("SuperSecretPassword!")


@when("the user enters invalid username and password")
def enter_invalid_credentials(context):
    context.driver.find_element("id", "username").send_keys("wronguser")
    context.driver.find_element(
        "id", "password"
    ).send_keys("wrongpassword")

@when("the user enters valid username and invalid password")
def enter_val_un_inval_pass(context):
    context.driver.find_element("id","username").send_keys("tomsmith")
    context.driver.find_element("id","password").send_keys("wrongpass")

@when("the user enters invalid username and valid password")
def enter_inval_un_val_pass(context):
    context.driver.find_element("id","username").send_keys("smithtom")
    context.driver.find_element("id", "password").send_keys("SuperSecretPassword!")

@when("the user clicks the Login button")
def click_login(context):
    context.driver.find_element(
        "css selector", "button[type='submit']"
    ).click()
    t.sleep(3)


@then("the user should be successfully logged in")
def verify_successful_login(context):
    message = context.driver.find_element("id", "flash").text

    assert "You logged into a secure area!" in message


@then("an error message should be displayed")
def verify_error_message(context):
    message = context.driver.find_element("id", "flash").text

    print("ACTUAL ERROR MESSAGE:", message)

    assert message