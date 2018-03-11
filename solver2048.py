#!/usr/bin/python

# Creating 2048 solver that uses Selenium

# Import the proper packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Import time
import time

# Opens browser to 2048 page 
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

retry = False
htmlElement = browser.find_element_by_tag_name('html')

grid = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]

while True:
    # TODO add test for retry button and click if it appears
    try:
        retry = browser.find_element_by_class_name('retry-button')
        retry.click()
    except:
        time.sleep(0.1)
    for i in range(0,50):
        htmlElement.send_keys(Keys.RIGHT)
        htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
