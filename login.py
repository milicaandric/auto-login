# imports
import csv
from selenium import webdriver
import info
from webdriver_manager.chrome import ChromeDriverManager

# specifies the path to webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email
username = driver.find_element_by_class_name('input__input')

# send_keys() to simulate key strokes
username.send_keys(info.username)

# locate password
password = driver.find_element_by_name('session_password')

# send_keys() to simulate key strokes
password.send_keys(info.password)

# locate submit button
sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

# .click() to mimic button click
sign_in_button.click()
