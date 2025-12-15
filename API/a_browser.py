from seleniumbase import Driver

class Browser():
    chrome = Driver()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(60)

    def close(self):
        self.chrome.quit()