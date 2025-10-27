from selenium.webdriver.common.by import By

USERNAME=(By.ID,"user-name")
PASSWORD_SELECTOR=(By.ID, "password")
LOGIN_BUTTON=(By.ID,"login-button")
LOGIN_ERROR_MESSAGE=(By.CSS_SELECTOR,"h3[data-test=\"error\"]")