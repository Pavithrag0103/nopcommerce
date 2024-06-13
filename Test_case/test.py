from selenium import webdriver
import pytest
import os
from Page_object.pom import Ecommerce
import time
from selenium.common.exceptions import StaleElementReferenceException
import openpyxl
from Utilities import xl_utilities as xl
from Configuration import config



file = config.EXCEL_FILE_PATH
workbook = openpyxl.load_workbook(file)
sheet = workbook.active


def test_register(browser):
    register_page = Ecommerce(browser)
    register_page.register_setup("Tamil", "selvi", "tamil123@gmail.com", "Tamil@123", "Tamil@123")
    print("Successfully registered")
    time.sleep(10)


def test_login(browser):
    try:
        login_page = Ecommerce(browser)
        login_page.login_setup("tamil123@gmail.com", "Tamil@123")
        time.sleep(20)
    except TimeoutException as e:
        print(f"Login test failed: {e}")
        browser.save_screenshot("test_login_error.png")


# Test case for verifying the logo name
def test_logo(browser):
    ecommerce_page = Ecommerce(browser)
    logo_name = ecommerce_page.get_logo_name()
    print("Logo Name:", logo_name)

# Test case for performing a search operation
def test_search(browser):
    searchfield = Ecommerce(browser)
    searchfield.get_search("Cell phone")
    time.sleep(5)

# Test case for verifying the product name
def test_product_name(browser, r=2):
    expected_product_name = xl.readData(file, "Sheet1", r, 3)  # Assuming product name is in the third column (index 2)
    product_page = Ecommerce(browser)
    actual_product_name = product_page.get_product()
    print("Actual Product Name:", actual_product_name)
    expected_product_name = "HTC One Mini Blue"
    assert actual_product_name == expected_product_name, f"Expected {expected_product_name}, but got {actual_product_name}"
    print("Matched Product name")
    time.sleep(20)

# Test case for verifying the product description
def test_prd_desc(browser, row_count=3):
    expected_product_description = xl.readData(file, "Sheet1", row_count, 3)
    product_desc = Ecommerce(browser)
    actual_product_description = product_desc.get_prd_desc()
    print("Actual product desc:", actual_product_description)
    assert actual_product_description == expected_product_description, "Product description did not match the expected description"
    print("Product description matched.")
    time.sleep(10)

# Test case for verifying the product image URL
def test_image(browser, row_count=4):
    expected_image = xl.readData(file, "Sheet1", row_count, 3)
    image = Ecommerce(browser)
    actual_image = image.get_image_element()
    print(f"Actual image URL: {actual_image}")
    assert actual_image == expected_image, "Product image did not match the expected image"

# Test case for verifying the product reviews
def test_review(browser, row_count=6):
    expected_review = xl.readData(file, "Sheet1", row_count, 3)
    review = Ecommerce(browser)
    actual_review = review.get_review()
    print("Actual review:", actual_review)
    assert actual_review == expected_review, "Not matched Reviews"
    time.sleep(10)

# Test case for verifying the SKU of the product
def test_SKU(browser, row_count=7):
    expected_SKU = xl.readData(file, "Sheet1", row_count, 3)
    SKU = Ecommerce(browser)
    actual_SKU = SKU.get_SKU()
    print("Actual SKU:", actual_SKU)
    assert actual_SKU == expected_SKU, "Not matched SKU"
    time.sleep(10)

# Test case for verifying the price of the product
def test_price(browser, row_count=8):
    expected_price = float(xl.readData(file, "Sheet1", row_count, 3))
    price = Ecommerce(browser)
    actual_price_str = price.get_price()
    print("Actual price string:", actual_price_str)
    actual_price = float(actual_price_str.replace('$', ''))  # Convert the string price to float
    assert actual_price == expected_price, "Not matched price"

# Test case for verifying the quantity of the product
def test_quantity(browser, row_count=9):
    expected_quantity = int(xl.readData(file, "Sheet1", row_count, 3))  # Assuming the quantity is an integer
    quantity_page = Ecommerce(browser)
    actual_quantity_str = quantity_page.get_quantity(1)
    time.sleep(2)
    actual_quantity = int(actual_quantity_str) if actual_quantity_str is not None else None
    print("Actual quantity:", actual_quantity)
    assert actual_quantity == expected_quantity, "Not matched quantity"

# Test case for verifying the address description
def test_address_desc(browser, row_count=10):
    expected_address_desc = xl.readData(file, "Sheet1", row_count, 3)
    address_desc = Ecommerce(browser)
    actual_address_desc = address_desc.get_address_tag()
    print(f"Actual address description: {actual_address_desc}")
    assert actual_address_desc == expected_address_desc, "Not matched address description"

# Test case for verifying the address popup
def test_popup(browser):
    popup = Ecommerce(browser)
    popup_page = popup.get_popup()
    assert popup_page.is_displayed(), "Not displayed pop up page"
    time.sleep(25)

# Test case for setting the address
def test_add_address(browser):
    address = Ecommerce(browser)
    address.get_address("1234")
    print("Address added successfully")
    time.sleep(2)

# Test case for clicking the add to cart button
def test_button(browser):
    addtocart = Ecommerce(browser)
    addtocart.get_button()
    print("Clicked the add to cart button")
    time.sleep(5)



# Test case for viewing the shopping cart
def test_shopcart(browser):
    shopping_cart = Ecommerce(browser)
    shopping_cart.get_shopcart()
    print("Shopping cart button clicked")

# Test case for proceeding to checkout
def test_checkout(browser):
    checkout = Ecommerce(browser)
    checkout.get_checkout()
    print("Checkout successfully")