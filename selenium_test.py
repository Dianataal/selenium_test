from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Sulgeb pop-upi
def click_decline_all(driver):
    try:
        decline_button = driver.find_element(By.ID, "W0wltc")
        decline_button.click()
    except NoSuchElementException:
        print("Didn't find the button")
        pass

# Otsime samoyedi
def search(search_box):
    driver.implicitly_wait(2)
    search_box.send_keys("samoyed")
    print("wrote")


def enter(search_box):
    search_box.send_keys(Keys.RETURN)
    print("tried to enter")

# kas sõna on otsingus
def check_word_in_results(driver, word):
    try:
        result = driver.find_element(By.XPATH, f"//*[contains(text(), '{word}')]")
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome()
driver.get('https://www.google.com')
click_decline_all(driver)
search_box = driver.find_element(By.ID, "APjFqb")
search(search_box)
driver.implicitly_wait(5)
enter(search_box)
driver.implicitly_wait(5)

if check_word_in_results(driver, "samoyed"):
    print("That's one nice boy.")
else:
    print("No dogs allowed.")

driver.implicitly_wait(5)

driver.quit()