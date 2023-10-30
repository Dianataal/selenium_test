from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Step 1: Go to Google homepage
driver.get("https://www.google.ee/")
assert "Google" in driver.title  

# Step 2: Enter the keyword "samoyed" in the search bar
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("samoyed")
search_box.send_keys(Keys.RETURN)

# Step 3: Wait for search results to load (adjust the sleep duration if needed)
time.sleep(2)  

# Step 4: Click on the "Images" tab
images_tab = driver.find_element(By.XPATH, "//a[text()='Pildid']")
images_tab.click()

# Step 5: Wait for images to load (adjust the sleep duration if needed)
time.sleep(2)

# Step 6: Click on the first image related to "samoyed"
first_image = driver.find_element(By.CSS_SELECTOR, "div[data-ri='0'] a")
first_image.click()

# Wait for a few seconds to see the opened image (adjust the sleep duration)
time.sleep(5)

# Close the browser window
driver.quit()
