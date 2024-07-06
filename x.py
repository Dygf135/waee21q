from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Initialize the Chrome driver
test_driver = webdriver.Chrome(options=options)

try:
    # Initialize the RecaptchaSolver
    solver = RecaptchaSolver(driver=test_driver)

    # Open the webpage with reCAPTCHA
    test_driver.get('https://www.google.com/recaptcha/api2/demo')

    # Find the reCAPTCHA iframe
    recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

    # Click the reCAPTCHA checkbox
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)

    # Take a screenshot after solving reCAPTCHA
    test_driver.save_screenshot('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")
    
finally:
    # Clean up
    test_driver.quit()
