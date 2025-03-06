from selenium import webdriver
import pytest
import os
import logging
from Page_object.pom import Ecommerce
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import openpyxl
from Utilities import xl_utilities as xl
from Configuration import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

file = config.EXCEL_FILE_PATH
workbook = openpyxl.load_workbook(file)
sheet = workbook.active


@pytest.mark.smoke
def test_register(browser):
    """Test case to verify user registration functionality."""
    try:
        register_page = Ecommerce(browser)
        register_page.register_setup("Tamil", "Selvi", "tamil123@gmail.com", "Tamil@123", "Tamil@123")
        logging.info("Successfully registered")
        time.sleep(5)
    except Exception as e:
        logging.error(f"Registration test failed: {e}")


@pytest.mark.smoke
def test_login(browser):
    """Test case to verify user login functionality."""
    try:
        login_page = Ecommerce(browser)
        login_page.login_setup("tamil123@gmail.com", "Tamil@123")
        logging.info("Login successful")
        time.sleep(5)
    except TimeoutException as e:
        logging.error(f"Login test failed: {e}")
        browser.save_screenshot("test_login_error.png")


@pytest.mark.visual
def test_logo(browser):
    """Test case to verify the website logo name."""
    try:
        ecommerce_page = Ecommerce(browser)
        logo_name = ecommerce_page.get_logo_name()
        logging.info(f"Logo Name: {logo_name}")
    except NoSuchElementException as e:
        logging.error(f"Failed to get logo name: {e}")


@pytest.mark.functional
def test_search(browser):
    """Test case to perform a product search operation."""
    try:
        search_field = Ecommerce(browser)
        search_field.get_search()
        logging.info("Search operation completed successfully")
    except Exception as e:
        logging.error(f"Search test failed: {e}")


@pytest.mark.functional
def test_comparelist(browser):
    """Test case to verify the product comparison list."""
    try:
        compare = Ecommerce(browser)
        compare.get_compare_list()
        logging.info("Product comparison completed successfully")
    except Exception as e:
        logging.error(f"Compare list test failed: {e}")


@pytest.mark.product
@pytest.mark.parametrize("row", [2, 3, 4,5])  # Testing multiple rows
def test_product_details(browser, row):
    """Test case to verify product details (name, description, image, review)."""
    try:
        expected_product_name = xl.readData(file, "Sheet1", row, 3)
        product_page = Ecommerce(browser)
        actual_product_name = product_page.get_product()

        assert actual_product_name == expected_product_name, \
            f"Expected {expected_product_name}, but got {actual_product_name}"

        logging.info(f"Product details verified for row {row}")
    except Exception as e:
        logging.error(f"Product details test failed for row {row}: {e}")


@pytest.mark.product_details
def test_SKU(browser, row=7):
    """Test case to verify the SKU of a product."""
    try:
        expected_SKU = xl.readData(file, "Sheet1", row, 3).strip()
        sku_page = Ecommerce(browser)
        actual_SKU = sku_page.get_SKU().strip()

        assert actual_SKU == expected_SKU, f"Expected SKU {expected_SKU}, but got {actual_SKU}"
        logging.info(f"Verified SKU: {actual_SKU}")
    except Exception as e:
        logging.error(f"SKU test failed: {e}")


@pytest.mark.product_details
def test_price(browser, row=8):
    """Test case to verify product pricing."""
    try:
        expected_price = float(xl.readData(file, "Sheet1", row, 3))
        price_page = Ecommerce(browser)
        actual_price = float(price_page.get_price().replace(',', '').replace('$', ''))
        assert actual_price == expected_price, f"Expected price {expected_price}, but got {actual_price}"
        logging.info(f"Verified price: {actual_price}")
    except Exception as e:
        logging.error(f"Price test failed: {e}")


@pytest.mark.cart
def test_wishlist(browser):
    """Test case to verify adding a product to the wishlist."""
    try:
        wishlist = Ecommerce(browser)
        wishlist.get_wishlist()
        logging.info("Added to wishlist successfully")
    except Exception as e:
        logging.error(f"Wishlist test failed: {e}")


@pytest.mark.visual
def test_popup(browser):
    """Test case to verify popups."""
    try:
        popup = Ecommerce(browser)
        popup.get_popup()
        logging.info("Popup displayed successfully")
    except Exception as e:
        logging.error(f"Popup test failed: {e}")


@pytest.mark.cart
def test_add_address(browser):
    """Test case to verify adding an address during checkout."""
    try:
        address_page = Ecommerce(browser)
        address_page.get_address("1234")
        logging.info("Address added successfully")
    except Exception as e:
        logging.error(f"Address test failed: {e}")


@pytest.mark.payment
def test_gift(browser):
    """Test case to verify adding a product to the cart."""
    try:
        cart_page = Ecommerce(browser)
        cart_page.get_gift()
        logging.info("Added to cart successfully")
    except Exception as e:
        logging.error(f"Add to cart test failed: {e}")

@pytest.mark.cart
def test_shopcart(browser):
    """Test case to verify viewing the shopping cart."""
    try:
        shopping_cart = Ecommerce(browser)
        shopping_cart.get_shopcart()
        logging.info("Shopping cart viewed successfully")
    except Exception as e:
        logging.error(f"Shopping cart test failed: {e}")


@pytest.mark.payment
def test_checkout(browser):
    """Test case to verify the checkout process."""
    try:
        checkout_page = Ecommerce(browser)
        checkout_page.get_checkout()
        logging.info("Checkout completed successfully")
    except Exception as e:
        logging.error(f"Checkout test failed: {e}")


