from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


register_xpath="//a[normalize-space()='Register']"
gender_xpath="//input[@id='gender-female']"
Firstname_xpath="//input[@id='FirstName']"
Lastname_xpath="//input[@id='LastName']"
email_xpath="//input[@id='Email']"
pass_xpath="//input[@id='Password']"
confpass_xpath="//input[@id='ConfirmPassword']"
registerbtn_xpath="//button[@id='register-button']"

# log in
logfield_xpath="//a[normalize-space()='Log in']"
emailfield_xpath="//input[@id='Email']"
passfield_xpath="//input[@id='Password']"
logbtn_xpath="//button[normalize-space()='Log in']"

# logo xpath
logo_xpath="/html/body/div[6]/div[1]/div[2]/div[1]/a/img"

# search
searchbox_xpath="//input[@id='small-searchterms']"
searchbutton_xpath="//button[normalize-space()='Search']"

#Sort by
sort_xpath="//select[@id='products-orderby']"
displaysixe_xpath="//select[@id='products-pagesize']"

# product select
prd_select_xpath="//a[normalize-space()='HTC One Mini Blue']"
prd_image1_xpath="//div[@class='picture']//img[@title='Show details for HTC One Mini Blue']"
prd_image2_xpath="//img[@id='main-product-img-19']"
prd_name_xpath="//h1[normalize-space()='HTC One Mini Blue']"
prd_desc_xpath="//div[@class='short-description']"

#image
image_xpath="//img[@id='main-product-img-19']"

# Star and Review
rating_xpath="//div[@class='product-reviews-overview']//div[@class='rating']//div"
review_line_xpath="//a[normalize-space()='4 review(s)']"
SKU_xpath="//div[@class='sku']"

#address tag
address_desc_xpath="//span[normalize-space()='Please select the address you want to ship to']"
arrow_xpath="//i[@class='arrow-down']"
popup_xpath="//div[@id='estimate-shipping-popup-19']"
shipto_xpath="//select[@id='CountryId']"
other_xpath="//select[@id='StateProvinceId']"
zip_xpath="//input[@id='ZipPostalCode']"
shippingmethod_xpath="//div[normalize-space()='Name']"
ground_next_xpath="//div[@class='shipping-options-body']//div[2]//div[1]//label[1]"
applybtn_xpath="//button[normalize-space()='Apply']"
# Price
price_xpath="//span[@id='price-value-19']"
quan_xpath="//*[@id='product_enteredQuantity_19']"
addcart_btn_xpath="//button[@id='add-to-cart-button-19']"


# shpping cart link
shopcart_xpath="//li[@id='topcartlink']"
tick_xpath="//input[@id='termsofservice']"
checkout_xpath="//button[@id='checkout']"

class Ecommerce:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def register_setup(self, first_name, last_name, email,password,curpassword):
        register_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, register_xpath)))
        register_link.click()

        # Fill in registration form
        gender_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, gender_xpath)))
        gender_radio.click()

        first_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, Firstname_xpath)))
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, Lastname_xpath)))
        last_name_field.send_keys(last_name)

        email_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, email_xpath)))
        email_field.send_keys(email)

        password_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,pass_xpath)))
        password_field.send_keys(password)

        curr_pass_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,confpass_xpath)))
        curr_pass_field.send_keys(curpassword)

        registerbtn_filed=self.wait.until(EC.element_to_be_clickable((By.XPATH,registerbtn_xpath)))
        registerbtn_filed.click()

    def login_setup(self,email,password):
        loginfiled=self.wait.until(EC.visibility_of_element_located((By.XPATH,logfield_xpath)))
        loginfiled.click()
        emailfield=self.wait.until(EC.visibility_of_element_located((By.XPATH,emailfield_xpath)))
        emailfield.send_keys(email)
        passwordfield=self.wait.until(EC.visibility_of_element_located((By.XPATH,passfield_xpath)))
        passwordfield.send_keys(password)
        logbtnfield=self.wait.until(EC.element_to_be_clickable((By.XPATH,logbtn_xpath)))
        logbtnfield.click()

    def get_logo_name(self):
        # Replace 'parent_xpath' with the XPath of the parent element containing the logo name
        parent_element = self.wait.until(EC.visibility_of_element_located((By.XPATH,logo_xpath)))
        logo_name = parent_element.text
        return logo_name

    def get_search(self,searchvalue):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,searchbox_xpath))).send_keys(searchvalue)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,searchbutton_xpath))).click()
        drp_down_sort = self.wait.until(EC.element_to_be_clickable((By.XPATH, sort_xpath)))
        drp_down_sort.click()
        drp_down_sortelement = Select(drp_down_sort)
        drp_down_sortelement.select_by_index(3)
        drp_down_size=self.wait.until(EC.element_to_be_clickable((By.XPATH,displaysixe_xpath)))
        drp_down_size.click()
        drp_down_sizefield=Select(drp_down_size)
        drp_down_sizefield.select_by_visible_text("18")
        print("Option selected successfully.")

    def get_product(self):
        for attempt in range(3):
            try:
                prd_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, prd_select_xpath)))
                prd_select.click()
                product_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, prd_name_xpath))).text
                return product_name
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                time.sleep(1)

    def get_image_element(self):
        image_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,image_xpath)))
        image_value=image_field.get_attribute("src")
        return image_value


    def get_prd_desc(self):
        prd_desc_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,prd_desc_xpath)))
        return prd_desc_field.text

    def get_rating(self):
        rating_field = self.wait.until(EC.presence_of_element_located((By.XPATH, rating_xpath)))
        rating_value = rating_field.text
        return rating_value
    def get_review(self):
        review_field=self.wait.until(EC.presence_of_element_located((By.XPATH,review_line_xpath)))
        review_value=review_field.text
        return review_value

    def get_SKU(self):
        SKU_field=self.wait.until(EC.presence_of_element_located((By.XPATH,SKU_xpath)))
        SKU_value=SKU_field.text
        return SKU_value

    def get_price(self):
        price_field=self.wait.until(EC.presence_of_element_located((By.XPATH,price_xpath)))
        price_value=price_field.text
        return price_value

    def get_quantity(self, quantity_count):
        quantity_field = self.wait.until(EC.presence_of_element_located((By.XPATH, quan_xpath)))
        quantity_field.click()  # Clicking the element to focus and interact with it
        quantity_field.clear()
        quantity_field.send_keys(str(quantity_count))
        actual_quantity_str = quantity_field.get_attribute("value")
        return actual_quantity_str

    def get_address_tag(self):
        address_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,address_desc_xpath)))
        address_value=address_field.text
        return address_value

    def get_popup(self):
        address_field=self.wait.until(EC.element_to_be_clickable((By.XPATH,arrow_xpath)))
        address_field.click()
        popup_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,popup_xpath)))
        return popup_field

    def get_address(self,zip_code):
        shipto=self.wait.until(EC.visibility_of_element_located((By.XPATH, shipto_xpath)))
        shipto.click()
        shipto_select=Select(shipto)
        shipto_select.select_by_visible_text("India")
        other=self.wait.until(EC.visibility_of_element_located((By.XPATH, other_xpath)))
        other.click()
        other_select=Select(other)
        other_select.select_by_index(0)
        zip=self.wait.until(EC.visibility_of_element_located((By.XPATH, zip_xpath)))
        zip.send_keys(zip_code)
        ground_field=self.wait.until(EC.element_to_be_clickable((By.XPATH,ground_next_xpath)))
        ground_field.click()
        apply_field=self.wait.until(EC.element_to_be_clickable((By.XPATH,applybtn_xpath)))
        apply_field.click()

    def get_button(self):
        button_field=self.wait.until(EC.visibility_of_element_located((By.XPATH,addcart_btn_xpath)))
        button_field.click()

    def get_shopcart(self):
        success_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, shopcart_xpath)))
        success_field.click()
        tick_field=self.wait.until(EC.element_to_be_clickable((By.XPATH, tick_xpath)))
        tick_field.click()

    def get_checkout(self):
        checkout_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
        checkout_field.click()




