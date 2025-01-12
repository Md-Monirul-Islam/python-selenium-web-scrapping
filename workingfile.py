# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://news.google.com/rss/search?q=lockdown')
# soup = BeautifulSoup(r.text, 'html.parser')

# # Print each news item in a readable format
# for item in soup.find_all('item'):
#     title = item.find('title').text
#     link = item.find('link').text
#     pub_date = item.find('pubdate').text
#     print(f"\nTitle: {title}")
#     print(f"Link: {link}")
#     print(f"Published: {pub_date}")

# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# import json

# def scrape_flight_data():
#     # Headers to mimic a browser request
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }

#     try:
#         # Make the initial request
#         response = requests.get('https://flightexpert.com/', headers=headers)
#         response.raise_for_status()  # Raise an exception for bad status codes
        
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Since flight data is likely loaded dynamically, you might need to:
#         # 1. Find and use their API endpoints
#         # 2. Use Selenium for JavaScript rendering
#         # 3. Look for JSON data in the page source
        
#         # Example of extracting flight data (adjust selectors based on actual HTML structure)
#         flights = soup.find_all('div', class_='flight-item')  # Replace with actual class name
        
#         for flight in flights:
#             try:
#                 # Adjust these selectors based on the actual HTML structure
#                 airline = flight.find('div', class_='airline').text.strip()
#                 departure = flight.find('div', class_='departure').text.strip()
#                 arrival = flight.find('div', class_='arrival').text.strip()
#                 price = flight.find('div', class_='price').text.strip()
                
#                 print(f"\nAirline: {airline}")
#                 print(f"Departure: {departure}")
#                 print(f"Arrival: {arrival}")
#                 print(f"Price: {price}")
                
#             except AttributeError as e:
#                 print(f"Error parsing flight data: {e}")
#                 continue
                
#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")

# if __name__ == "__main__":
#     scrape_flight_data()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time
# import random

# def scrape_with_selenium():
#     # Enhanced Chrome options to avoid detection
#     options = webdriver.ChromeOptions()
#     options.add_argument('--start-maximized')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('--disable-infobars')
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
#     # Add random user agent
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
#     ]
#     options.add_argument(f'user-agent={random.choice(user_agents)}')
    
#     driver = webdriver.Chrome(options=options)
#     wait = WebDriverWait(driver, 15)
    
#     try:
#         # Clear cookies and cache before starting
#         driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
#         driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        
#         # Navigate to the website with random delay
#         driver.get('https://www.biman-airlines.com/')
#         time.sleep(random.uniform(2, 4))
        
#         # Add random mouse movements (optional)
#         def random_scroll():
#             driver.execute_script(f"window.scrollTo(0, {random.randint(100, 500)});")
#             time.sleep(random.uniform(0.5, 1.5))
        
#         random_scroll()
        
#         # Input handling with human-like delays
#         def human_type(element, text):
#             for char in text:
#                 element.send_keys(char)
#                 time.sleep(random.uniform(0.1, 0.3))
#             time.sleep(random.uniform(0.5, 1.5))
        
#         # Wait for search form and fill it
#         from_input = wait.until(EC.presence_of_element_located((By.NAME, "from")))
#         human_type(from_input, "NYC")
#         time.sleep(random.uniform(1, 2))
#         from_input.send_keys(Keys.RETURN)
        
#         random_scroll()
        
#         to_input = wait.until(EC.presence_of_element_located((By.NAME, "to")))
#         human_type(to_input, "LAX")
#         time.sleep(random.uniform(1, 2))
#         to_input.send_keys(Keys.RETURN)
        
#         # Random delay before clicking search
#         time.sleep(random.uniform(1, 2))
#         search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
#         search_button.click()
        
#         # Longer wait for results with random scroll
#         time.sleep(random.uniform(3, 5))
#         random_scroll()
        
#         # Rest of your code for extracting flight details...
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
        
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     scrape_with_selenium()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from datetime import datetime, timedelta
# import time
# import random
# import pandas as pd

# def scrape_with_selenium():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--start-maximized')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('--disable-infobars')
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
#     # Add random user agent
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
#     ]
#     options.add_argument(f'user-agent={random.choice(user_agents)}')
    
#     driver = webdriver.Chrome(options=options)
#     wait = WebDriverWait(driver, 15)
    
#     flight_data = []
    
#     try:
#         # Clear cookies and cache
#         driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
#         driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        
#         driver.get('https://flightexpert.com/')
#         time.sleep(random.uniform(2, 4))
        
#         # Human-like typing function
#         def human_type(element, text):
#             for char in text:
#                 element.send_keys(char)
#                 time.sleep(random.uniform(0.1, 0.3))
#             time.sleep(random.uniform(0.5, 1.5))
        
#         # Fill search form
#         from_input = wait.until(EC.presence_of_element_located((By.NAME, "from")))
#         human_type(from_input, "NYC")
#         time.sleep(random.uniform(1, 2))
#         from_input.send_keys(Keys.RETURN)
        
#         to_input = wait.until(EC.presence_of_element_located((By.NAME, "to")))
#         human_type(to_input, "LAX")
#         time.sleep(random.uniform(1, 2))
#         to_input.send_keys(Keys.RETURN)
        
#         # Set departure date (tomorrow's date)
#         tomorrow = datetime.now() + timedelta(days=1)
#         date_str = tomorrow.strftime("%Y-%m-%d")
#         date_input = wait.until(EC.presence_of_element_located((By.NAME, "departure")))
#         driver.execute_script(f"arguments[0].value = '{date_str}'", date_input)
        
#         time.sleep(random.uniform(1, 2))
#         search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
#         search_button.click()
        
#         # Wait for results and extract data
#         time.sleep(random.uniform(5, 7))  # Longer wait for results to load
        
#         # Scroll slowly through results
#         def scroll_slowly():
#             height = driver.execute_script("return document.body.scrollHeight")
#             for i in range(0, height, 100):
#                 driver.execute_script(f"window.scrollTo(0, {i});")
#                 time.sleep(random.uniform(0.1, 0.3))
        
#         scroll_slowly()
        
#         # Extract flight information
#         flights = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".flight-card, .flight-item, .flight-result")))  # Adjust selector based on actual website
        
#         for flight in flights:
#             try:
#                 flight_info = {
#                     'airline': flight.find_element(By.CSS_SELECTOR, ".airline-name, .carrier-name").text,
#                     'departure_time': flight.find_element(By.CSS_SELECTOR, ".departure-time").text,
#                     'arrival_time': flight.find_element(By.CSS_SELECTOR, ".arrival-time").text,
#                     'duration': flight.find_element(By.CSS_SELECTOR, ".duration").text,
#                     'price': flight.find_element(By.CSS_SELECTOR, ".price, .amount").text,
#                     'stops': flight.find_element(By.CSS_SELECTOR, ".stops, .layover").text
#                 }
#                 flight_data.append(flight_info)
                
#                 # Print flight details
#                 print("\nFlight Details:")
#                 for key, value in flight_info.items():
#                     print(f"{key.replace('_', ' ').title()}: {value}")
                
#             except Exception as e:
#                 print(f"Error extracting flight details: {e}")
#                 continue
        
#         # Save to CSV if data was collected
#         if flight_data:
#             df = pd.DataFrame(flight_data)
#             df.to_csv('flight_prices.csv', index=False)
#             print("\nData saved to flight_prices.csv")
            
#     except Exception as e:
#         print(f"An error occurred: {e}")
        
#     finally:
#         driver.quit()
        
#     return flight_data

# if __name__ == "__main__":
#     flight_data = scrape_with_selenium()
    
#     if flight_data:
#         print("\nSummary of flights found:")
#         print(f"Total flights found: {len(flight_data)}")
        
#         # Calculate average price if possible
#         try:
#             prices = [float(flight['price'].replace('$', '').replace(',', '')) for flight in flight_data]
#             avg_price = sum(prices) / len(prices)
#             print(f"Average price: ${avg_price:.2f}")
#         except:
#             print("Could not calculate average price")
#     else:
#         print("No flight data was collected")




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_flight_expert():
    try:
        # Setup Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        # Add these options to help prevent detection
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Add random user agent
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
        options.add_argument(f'user-agent={random.choice(user_agents)}')
        
        # Initialize WebDriver with Service
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        wait = WebDriverWait(driver, 20)
        
        prices = []
        
        try:
            print("Navigating to FlightExpert...")
            driver.get('https://flightexpert.com/flight/search?t')
            time.sleep(random.uniform(3, 5))
            
            print("Filling origin...")
            # Fill origin
            from_input = wait.until(EC.presence_of_element_located((By.ID, "from-search")))
            from_input.clear()
            from_input.send_keys("DAC")  # Dhaka
            time.sleep(random.uniform(1, 2))
            
            print("Filling destination...")
            # Fill destination
            to_input = wait.until(EC.presence_of_element_located((By.ID, "to-search")))
            to_input.clear()
            to_input.send_keys("DXB")  # Dubai
            time.sleep(random.uniform(1, 2))
            
            print("Setting departure date...")
            # Set departure date (tomorrow)
            tomorrow = datetime.now() + timedelta(days=1)
            date_str = tomorrow.strftime("%d-%m-%Y")
            date_input = wait.until(EC.presence_of_element_located((By.ID, "departureDate")))
            date_input.click()
            time.sleep(1)
            driver.execute_script(f"arguments[0].value = '{date_str}'", date_input)
            
            print("Clicking search button...")
            # Click search button
            search_button = wait.until(EC.element_to_be_clickable((By.ID, "searchFlightsButton")))
            search_button.click()
            
            print("Waiting for results...")
            time.sleep(15)  # Adjust wait time based on website's response
            
            print("Extracting prices...")
            # Extract prices from result cards
            price_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".flight-fare .fare-amount")))
            
            for element in price_elements:
                try:
                    price_text = element.text.strip()
                    if price_text:
                        # Clean and parse the price text
                        price = float(price_text.replace(',', '').replace('৳', '').strip())
                        prices.append(price)
                except Exception as e:
                    print(f"Error parsing price: {e}")
                    continue
            
            if prices:
                print("\nPrice Summary:")
                print(f"Lowest Price: ৳ {min(prices):,.2f}")
                print(f"Highest Price: ৳ {max(prices):,.2f}")
                print(f"Number of flights found: {len(prices)}")
            else:
                print("No prices found")
                
        except Exception as e:
            print(f"Error during scraping: {str(e)}")
            
        finally:
            print("Closing browser...")
            driver.quit()
            
    except Exception as e:
        print(f"Error setting up WebDriver: {str(e)}")
        
    return prices

if __name__ == "__main__":
    print("Starting FlightExpert scraper...")
    prices = scrape_flight_expert()
