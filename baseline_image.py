"""
This python script takes a screenshot of the target webpage
and save it as baseline image.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the target webpage
driver.get("https://www.saucedemo.com/v1/")

# To save image in a maximized window state
driver.maximize_window()
driver.implicitly_wait(5)

# Login to the website 
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Click on the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Take a screenshot after login and save it
# Similarly take baseline image for scenarios like registration, dashboard, product details etc.,
expected_image_path = "expected.png"
driver.save_screenshot(expected_image_path)

# Quit the browser
driver.quit()
