from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open the target website
    driver.get('https://news.google.com')

    # Debugging: Print page title to verify successful navigation
    print(f"Page title: {driver.title}")

    # Wait for the search input field
    search_locator = (By.CSS_SELECTOR, "input[aria-label='Search for topics, locations & sources']")
    search_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_locator)
    )
    print("Search bar located.")

    # Interact with the search input field
    search_element.clear()
    search_element.send_keys("technology")
    search_element.send_keys(Keys.RETURN)
    print("Search query submitted.")

    # Wait for the search results to load
    results_locator = (By.CLASS_NAME, "NiLAwe")
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(results_locator)
    )
    print("Search results loaded.")

    # Fetch and print articles
    articles = driver.find_elements(By.CLASS_NAME, "NiLAwe")
    if not articles:
        print("No articles found.")
    else:
        print(f"Found {len(articles)} articles.")
        for index, article in enumerate(articles[:5]):  # Limit to 5 results for brevity
            title_element = article.find_element(By.TAG_NAME, "h3")
            print(f"{index + 1}. {title_element.text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the browser
    print("Closing the browser...")
    driver.quit()
