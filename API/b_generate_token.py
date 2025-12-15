import time

import requests as requests
from selenium.webdriver.common.by import By
from .a_browser import Browser
from .c_extract_otp import get_latest_otp_with_wait, get_gmail_service


class Generate_token(Browser):
    CLIENT_ID = "bbfd54ee1ef84bb99a9d438948ae8ff4"
    CLIENT_SECRET = "6aca16c7b09a440aaa8068227eb65f4c"
    RESPONSE_TYPE= "code"
    ENCODED_REDIRECT_URI = "https%3A%2F%2Fitfactory.ro%2Fcallback"
    REDIRECT_URI = "https://itfactory.ro/callback"
    SCOPE = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private"
    HOST = "https://accounts.spotify.com"
    USERNAME = (By.ID,"username")
    CONTINUE = (By.XPATH,'//button[@data-testid="login-button"]')
    OTP = (By.XPATH,'//input[@inputmode="numeric"]')
    PASSSWORD = (By.ID,"login-password")
    LOG_IN_BUTTON =(By.ID,"login-button")
    AGREE_BUTTON = (By.CLASS_NAME,"jWBSO")
    GRANT_TYPE = "authorization_code"

    def create_authorize_endpoint(self):
        endpoint = self.HOST + "/authorize?client_id=" + self.CLIENT_ID+"&response_type="+self.RESPONSE_TYPE+"&redirect_uri="+self.ENCODED_REDIRECT_URI+"&scope="+self.SCOPE
        return endpoint

    def load_endpoint(self):
        self.chrome.get(self.create_authorize_endpoint())

    def login_to_spotify(self):
        service = get_gmail_service()
        last_msg_id = None

        # trimite cererea de login Spotify (apasă pe “Send code”)
        self.chrome.find_element(*self.USERNAME).send_keys("meet@itfactory.ro")
        self.chrome.find_element(*self.CONTINUE).click()

        # acum așteaptă OTP-ul
        otp, last_msg_id = get_latest_otp_with_wait(service, last_msg_id=last_msg_id)
        self.chrome.find_element(*self.OTP).send_keys(otp)
        try:
            self.chrome.find_element(*self.PASSSWORD).send_keys("meetitfactorytest")
            self.chrome.find_element(*self.LOG_IN_BUTTON).click()
        except:
            pass

    def authorize_login(self):
        self.chrome.find_element(*self.AGREE_BUTTON).click()

    def get_code(self):
        url = self.chrome.current_url
        code = url[url.index("=")+1:]
        return code

    def get_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
                "redirect_uri": self.REDIRECT_URI,
                "client_id": self.CLIENT_ID,
                "client_secret":self.CLIENT_SECRET,
                "code":self.get_code(),
                "grant_type":self.GRANT_TYPE
                }
        response = requests.post(self.HOST + "/api/token", data=data, headers=header)
        return response.json()["access_token"]

    def authorization(self):
        self.create_authorize_endpoint()
        self.load_endpoint()
        try:
            self.login_to_spotify()
            self.authorize_login()
        except:
            self.get_code()
        return f"Bearer {self.get_token()}"