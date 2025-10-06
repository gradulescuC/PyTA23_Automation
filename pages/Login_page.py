from selenium.webdriver.common.by import By

from browser import Browser
from pages.selectors.login_selectors import *

class Login_page(Browser):

		def go_to_login_page(self):
				self.driverObject.get("https://www.saucedemo.com/")

		def insert_username(self):
				self.driverObject.find_element(*USERNAME).send_keys("standard_user")

		def insert_password(self):
				self.driverObject.find_element(*PASSWORD).send_keys("secret_sauce")

		def click_login_button(self):
				self.driverObject.find_element(*LOGIN_BUTTON).click()
