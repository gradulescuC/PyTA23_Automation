from selenium.webdriver.common.by import By

from browser import Browser
from pages.selectors.login_selectors import *

class Login_page(Browser):

		def go_to_login_page(self):
				self.driverObject.get("https://www.saucedemo.com/")

		def click_login_button(self):
				self.driverObject.find_element(*LOGIN_BUTTON).click()
