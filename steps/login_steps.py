from behave import *

@given("I am on the saucedemo homepage")
def step_impl(context):
		context.login_page.go_to_login_page()

@when('I insert username')
def step_impl(context):
		context.login_page.insert_username()

@when('I insert password')
def step_impl(context):
		context.login_page.insert_password()

@when('I click the login button')
def step_impl(context):
		context.login_page.click_login_button()