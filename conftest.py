
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Optional: run headless (no browser window)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
