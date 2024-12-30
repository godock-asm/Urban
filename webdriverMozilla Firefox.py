from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.saucedemo.com')
driver.maximize_window(),

sleep(20)