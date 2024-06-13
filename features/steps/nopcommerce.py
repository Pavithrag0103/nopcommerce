from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Launch chrome browser')
def launch(context):
    context.driver = webdriver.Edge()

@when('open nop commerce homepage')
def openhome(context):
    context.driver.get("https://demo.nopcommerce.com/")

@then('verify that the logo is present on the page')
def verify_logo(context):
    logo = context.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[1]/a/img")
    status = logo.is_displayed()
    assert status is True

@then('close browser')
def closebrowser(context):
    context.driver.quit()
