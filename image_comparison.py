"""
This python script compares the baseline image with the actual image.
After any source code modification, the visual changes are compared easily through this script.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from visual_comparison.utils import ImageComparisonUtil

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the target webpage
driver.get("https://www.saucedemo.com/v1/")
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

# Take a screenshot after login to visualize the changes
actual_image_path = "actual.png"
expected_image_path = "expected.png"
driver.save_screenshot(actual_image_path)

# Close the browser
driver.quit()

# Load the expected image and the actual screenshot
expected_image = ImageComparisonUtil.read_image(expected_image_path)
actual_image = ImageComparisonUtil.read_image(actual_image_path)

# Choose the path to save the comparison result
result_destination = "result_screenshot.png"

# Compare the images and save the result
similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result_destination)
print("Similarity Index:", similarity_index)

# Asserting both images
match_result = ImageComparisonUtil.check_match(expected_image_path, actual_image_path)
assert match_result
