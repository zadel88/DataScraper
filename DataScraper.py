import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Use headless mode to not open a browser window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the page you want to scrape
driver.get("https://eroticasbogota.com/modelos/page/4/")  # Replace with the actual URL

# Wait for the page to load (you can adjust the time or use explicit waits)
wait = WebDriverWait(driver, 10)
product_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/modelo/')]")))

# List to store scraped data for each product
scraped_data = []

# Loop through each product link
for link in product_links:
    try:
        # Get the href attribute (the product link)
        product_url = link.get_attribute("href")
        
        # Open the product page
        driver.get(product_url)
        
        # Initialize a dictionary for the current product
        product_info = {"URL": product_url}  # Add URL to identify the product
        
        # Scrape the header (title)
        try:
            header = driver.find_element(By.XPATH, "//title").text
            product_info["Header"] = header
        except NoSuchElementException:
            product_info["Header"] = "Header not found"
        
        # Scrape the first table (product attributes table)
        try:
            table1 = driver.find_element(By.XPATH, "//table[contains(@class, 'woocommerce-product-attributes')]")
            product_info["Table 1"] = table1.text
        except NoSuchElementException:
            product_info["Table 1"] = "Table 1 not found"
        
        # Scrape the second table using style or another method
        try:
            table2 = driver.find_element(By.XPATH, "//table[contains(@style, 'width: 100.782%;')]")  # Modify as needed
            product_info["Table 2"] = table2.text
        except NoSuchElementException:
            product_info["Table 2"] = "Table 2 not found"
        
        # Append the product information dictionary to the scraped data list
        scraped_data.append(product_info)
        
        # Go back to the main page
        driver.back()
    
    except Exception as e:
        # Catch any errors not related to element search
        print(f"Error with {product_url}: {e}")

# Close the driver
driver.quit()

# Create a DataFrame from the scraped data
df = pd.DataFrame(scraped_data)

# Export the DataFrame to a CSV file
df.to_csv("scraped_products4.csv", index=False)

print("Scraping completed. Data exported to 'scraped_products.csv'")
