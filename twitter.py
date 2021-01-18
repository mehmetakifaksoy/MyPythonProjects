from twitterUserInfo import username ,  password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter : 
    def __init__(self, username, password):
        self.browserProfile = webdriver.FirefoxOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Firefox('firefoxdrive.exe',chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)


        usernameInput = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")



        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
        btnSubmit.click()

        time.sleep(2)


twitter = Twitter(username,password)
#login işlemi
twitter.signIn()