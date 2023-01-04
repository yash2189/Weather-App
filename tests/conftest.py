import logging
import pytest
import requests
from selenium import webdriver

logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def init_setup(request):
    logger.info("Setting up Chrome Driver")
    request.cls.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver = request.cls.driver
    driver.implicitly_wait(50)
    yield driver
    driver.quit()
    logger.info("Test Completed")
