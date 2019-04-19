#!/usr/bin/python
# encoding: utf-8

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title
print(driver.title)
