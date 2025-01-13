from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.w3schools.com/')

try:
    # Wait for the "Learn HTML" link and click it
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Learn HTML'))
    )
    element.click()

    # Wait for the "Log in" button and click it
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login' and contains(text(), 'Log in')]"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Add some delay to observe the result (optional)
    time.sleep(5)

    # Close the driver
    driver.quit()
