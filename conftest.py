from selenium import webdriver
import pytest

URL="https://demo.nopcommerce.com/"
@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()  # Close the browser