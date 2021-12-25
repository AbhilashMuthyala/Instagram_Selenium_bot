from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = '<>/chromedriver'

SIMILAR_ACCOUNT = '<>'
USERNAME = '<>'
PASSWORD = '<>'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self,url):
        self.driver.get(url)

        sleep(3)
        email_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(USERNAME)

        sleep(1)
        passowrd_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        passowrd_input.send_keys(PASSWORD)

        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_button.click()

        sleep(5)

    def find_followers(self,url):
        self.driver.get(url)
        sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(3)

        scroll_down_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        scroll = 0
        while scroll < 1:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down_popup)
            sleep(1)
            scroll +=1
        sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector('li button')
        for ele in follow_buttons:
            ele.click()
            sleep(1)

