from selenium import webdriver
from src import solveRecaptcha
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

driver = webdriver.Chrome()
site_url = os.getenv('SITE_URL')
driver.get(site_url)
solveRecaptcha(driver)
