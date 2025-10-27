from behave import *
# from pages.selectors import login_selectors
from pages.selectors.login_selectors import *
from test_data import *

@given("I am on the saucedemo homepage")
def step_impl(context):
		context.login_page.go_to_login_page()

@when('I insert username')
def step_impl(context):
		context.base_page.insert_input(standard_username, USERNAME)
		# in general nu este recomandat sa hardcodam valori, adica nu sa scriem valori efective in cod
		# in schimb acestea este recomandat sa fie scrise in fisiere separate
		# care pot fi usor modificare

@when('I insert username "{username_value}"')
def step_impl(context,username_value):
		context.base_page.insert_input(username_value,USERNAME)

@when('I insert password')
def step_impl(context):
		context.base_page.insert_input(password_value, PASSWORD_SELECTOR)

@when('I insert password "{password}"')
def step_impl(context,password):
		context.base_page.insert_input(password,PASSWORD_SELECTOR)

@when('I click the login button')
def step_impl(context):
		context.login_page.click_login_button()

@then('I should receive an unsuccessful login message: "{err}"')
def step_impl(context, err):
		context.base_page.verify_error_message(err,LOGIN_ERROR_MESSAGE)