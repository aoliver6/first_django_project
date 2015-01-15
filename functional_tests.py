from selenium import webdriver
#Starts Selenium webdriver and pops up a Firefox window
browser = webdriver.Firefox()
#Sends a GET request to the web address specified
browser.get('http://localhost:8000')
#checks to see if 'Django' is in the page title
assert 'Django' in browser.title
