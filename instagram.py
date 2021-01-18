from instagramUserInfo import email, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Instagram:
    def __init__(self,email,password):
        self.browser = webdriver.Firefox()
        self.email = email
        self.password = password

    def signIn(self): 
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        emailInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.email)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

instgrm = Instagram(email, password)
instgrm.signIn()