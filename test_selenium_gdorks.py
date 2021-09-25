
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navigator = webdriver.Chrome()

navigator.get("http://www.google.com")
navigator.find_element_by_name("q").send_keys(" \"QAladies\" ")

navigator.find_element_by_name("q").send_keys(Keys.RETURN)
