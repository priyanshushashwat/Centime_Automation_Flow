import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from Centime.utils import config

print("Loading conftest.py")  # Debug print


@pytest.fixture(scope="session")
def setUp():
    print("Initializing driver fixture")  # Debug print

    driver = None
    if config.Driver.lower() == "chrome":
        chrome_options = Options()
        if config.Headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif config.Driver.lower() == "firefox":
        firefox_options = FirefoxOptions()
        if config.Headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    else:
        print("Browser not supported. Suggested values are [Chrome, Firefox]")

    if driver:
        driver.maximize_window()
        driver.get(config.base_url)
        yield driver
        driver.quit()

    print("Driver fixture cleanup complete")  # Debug print
