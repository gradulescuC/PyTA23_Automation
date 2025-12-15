from browser import Browser


class Inventory_page(Browser):

		def verify_login_successful(self):
				expected_url = "https://www.saucedemo.com/inventory.html"
				actual_url = self.driverObject.get_current_url()
				assert expected_url == actual_url, f"Expected URL {expected_url} is different from actual URL {actual_url}"