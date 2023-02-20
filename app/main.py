import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    options = Options()
    options.add_argument("--high-dpi-support=2")
    #options.add_argument("--force-device-scale-factor=2")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(60)
    driver.set_window_size(1920, 1080)

    logging.info("Entering in google...")
    driver.get("https://google.com")
except Exception as a:
    print(a)

