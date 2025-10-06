from behave import *

@then('I should be logged in and I should see the saucedemo inventory homepage')
def step_impl(context):
		context.inventory_page.verify_login_successful()