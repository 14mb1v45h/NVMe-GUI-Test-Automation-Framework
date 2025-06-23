import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.nvme_page import NVMePage
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver():
    logger.info("Starting Chrome WebDriver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    logger.info("Quitting WebDriver")
    driver.quit()

@pytest.fixture(scope="function")
def nvme_page(driver):
    page = NVMePage(driver)
    page.navigate()
    yield page