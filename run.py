from selenium import webdriver
from selenium.webdriver.common.by import By
from Insta_bot import InstaFollower

CHROME_DRIVER_PATH = '/Users/flight/Downloads/chromedriver'

SIMILAR_ACCOUNT = '<>'
USERNAME = '<>'
PASSWORD = '<>'
insta_url = 'https://www.instagram.com/accounts/login/'
sample_account_url = f'https://www.instagram.com/{SIMILAR_ACCOUNT}/'

bot = InstaFollower()
bot.login(insta_url)
bot.find_followers(sample_account_url)
bot.follow()


