#!/usr/bin/python

# Creating 2048 solver that uses Selenium

# Import the proper packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Import time
import time

# Collect input of how many games are wanted
iterations = 0
read = input('Enter a number of how many games you would like to complete: ')
iterations = int(read)
if iterations <= 0:
    print('Error. Please enter a valid number next time.')
    exit()

# Opens browser to 2048 page 
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

retry = False
htmlElement = browser.find_element_by_tag_name('html')

# TODO add grid list to count and keep track of numbers filled in on board
# grid = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]

count = 0
while count < iterations:
    for i in range(0,50):
        htmlElement.send_keys(Keys.RIGHT)
        htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
    try:
        retry = browser.find_element_by_class_name('retry-button')
        retry.click()
        count = count + 1
    except:
        time.sleep(0.1)
