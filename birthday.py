from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver (update the path to where you saved ChromeDriver)
driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")  # On Windows, use .exe; on Mac/Linux, no extension

# Open Google
driver.get("https://www.google.com")

# Find the search bar, type a query, and submit
search_box = driver.find_element("name", "q")  # Google search bar has name="q"
search_box.send_keys("What is Selenium?")
search_box.send_keys(Keys.RETURN)

# Wait a moment for results to load
time.sleep(2)

# Take a screenshot
driver.save_screenshot("google_search_selenium.png")

# Close the browser
driver.quit()

print("Screenshot saved as 'google_search_selenium.png'!")