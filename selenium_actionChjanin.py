from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    driver.implicitly_wait(5)

    # Wait for the cookie element to be present
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'bigcookie'))
    )
    cookie_count = driver.find_element(By.ID, 'cookies')

    items = [driver.find_element(By.ID, 'productPrice0') + str(i) for i in range(1, -1, -1)]

    action = ActionChains(driver)
    action.click(cookie)

    for i in range(5000):
        action.perform()
        count = int(cookie_count.text.split(' ')[0])
        # print(count)
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()