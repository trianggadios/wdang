import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wdang(object):

    def checkPing (self):
        self.hostname = "google.com"
        self.response = os.system("ping -c 1 " + self.hostname)

        return self.response

    def login (self):
        self.test = True

        while self.test == True:
            self.url = "http://awang.ga/"
            time.sleep(1)

            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            time.sleep(1)

            while self.test == True:
                try:
                    self.error_class = "error-code"

                    self.driver.find_element_by_class_name(self.error_class)
                    time.sleep(1)

                    self.driver.close()
                    time.sleep(1)

                    self.driver = webdriver.Chrome()

                    self.driver.get(self.url)
                    time.sleep(1)
                except:
                    username = "88720042141"
                    password = "11077635201435"
                    button_class = "button-lg"
                    xpath_username = "//input[@type='text' and @id='username_member' and @name='username_member']"
                    xpath_password = "//input[@type='password' and @id='password_member' and @name='password_member']"

                    element = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, "username_member")))
                    time.sleep(1)

                    self.driver.find_element_by_xpath(xpath_username).send_keys(username)
                    time.sleep(1)

                    self.driver.find_element_by_xpath(xpath_password).send_keys(password)
                    time.sleep(1)

                    coba = self.driver.find_elements_by_class_name(button_class)
                    coba[0].click()
                    time.sleep(10)

                    self.test = False

            time.sleep(10)
            self.test = False