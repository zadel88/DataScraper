# Web Scraping with Selenium and Pandas

This script performs web scraping using Selenium and Pandas to extract product information from a single page of a website. The extracted data includes product URLs, headers, and information from tables on the product pages. The data is saved to a CSV file.

## Requirements
Before running the script, ensure you have the following installed:

- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `selenium`
  - `webdriver-manager`

Install these libraries using the following command:
```bash
pip install pandas selenium webdriver-manager
```

## How the Script Works

### Setup
1. **WebDriver Configuration**:
   - The script uses Selenium's `webdriver-manager` to handle the ChromeDriver installation automatically.
   - Headless mode is enabled to prevent the browser from opening visually.

2. **Target Website**:
   - Replace the placeholder `URL` with the actual URL of the webpage you want to scrape.

### Scraping Process
1. **Find Product Links**:
   - The script identifies product links on the main page using an XPath query.
   - Update the XPath in the line:
     ```python
     "//a[contains(@href, '/unique path to product/')]
     ```
     to match the structure of the target website.

2. **Extract Data from Each Product Page**:
   - For each product, the script:
     - Retrieves the product URL.
     - Scrapes the header (title).
     - Scrapes information from two tables on the page. Update the XPaths for `table1` and `table2` as per the website structure.
     - Handles cases where elements are not found gracefully by assigning default values.

3. **Save Data**:
   - All scraped data is stored in a Pandas DataFrame and exported to a CSV file named `scraped_products4.csv`.

### Limitations
- The script only loops through the links available on the main page. It does not navigate to additional pages.
- Update the `XPATH` values to align with the structure of the target website.
- The maximum wait time for elements is set to 10 seconds. Adjust as needed for slower websites.

## Usage
1. Replace the placeholder values in the script with details specific to the target website:
   - `URL`: The webpage to scrape.
   - XPaths: Update the XPaths for product links, header, and tables to match the website structure.

2. Run the script:
   ```bash
   python script_name.py
   ```

3. Find the output in the `scraped_products4.csv` file in the working directory.

## Key Functions
- **`WebDriverWait`**:
  - Ensures elements are loaded before accessing them.
  - XPath queries are used to locate specific elements.

- **Error Handling**:
  - `try-except` blocks are used to handle missing elements or unexpected issues during scraping.

## Example Output
The output CSV will look like:

| URL               | Header              | Table 1               | Table 2               |
|-------------------|---------------------|-----------------------|-----------------------|
| product1_url      | Product 1 Header   | Attribute details 1   | Attribute details 2   |
| product2_url      | Product 2 Header   | Attribute details 1   | Attribute details 2   |

## Notes
- The script uses headless mode by default. Remove the `--headless` option in `options.add_argument` to see the browser while scraping.
- To scrape multiple pages, additional logic is required to navigate through pagination.

