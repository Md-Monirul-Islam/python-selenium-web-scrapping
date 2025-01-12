from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open the target website
    driver.get('https://news.google.com')  # Replace with the actual target URL

    # Wait for the input field to be present using the 'aria-label' attribute
    search_locator = (By.CSS_SELECTOR, "input[aria-label='Search for topics, locations & sources']")
    search_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_locator)
    )

    # Interact with the input field
    search_element.clear()  # Clear the input field
    search_element.send_keys("technology")  # Enter the search term
    search_element.send_keys(Keys.RETURN)  # Simulate pressing Enter

    # Wait for the search results to load (if applicable)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "NiLAwe"))  # Update this with the actual results class
    )

    print("Search completed successfully.")

    # Keep the browser open for a while to view the results
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the browser
    print("Closing the browser...")
    driver.quit()
