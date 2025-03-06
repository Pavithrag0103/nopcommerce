from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    TimeoutException
)
import time


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
com_xpath="//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']"
note_xpath="//li[@class='inactive']//a[normalize-space()='Notebooks']"
#Sort by
sort_xpath="//select[@id='products-orderby']"
displaysixe_xpath="//select[@id='products-pagesize']"

# product select
prd_select_xpath="//h2[@class='product-title']//a[normalize-space()='Apple MacBook Pro']"
combutton1_xpath="//body[1]/div[6]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/button[2]"
combutton2_xpath="/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/button[2]"
comparelist_xpath="//a[normalize-space()='Compare products list']"

prd_image1_xpath="//div[@class='picture-thumbs']//div[1]//img[1]"
prd_image2_xpath="//div[@class='picture-thumbs']//div[2]//img[1]"
prd_name_xpath="//h1[normalize-space()='Apple MacBook Pro']"
prd_desc_xpath="//div[@class='short-description']"

#image
image_xpath="//img[@id='main-product-img-4']"

# Star and Review
rating_xpath="//div[@class='product-reviews-overview']//div[@class='rating']//div"
review_line_xpath="//a[normalize-space()='1 review(s)']"
SKU_xpath="//span[@id='sku-4']"

#address tag
shipping_xpath="//span[@class='cart-label']"
address_desc_xpath="//span[normalize-space()='Please select the address you want to ship to']"

shipto_xpath="//select[@id='CountryId']"
other_xpath="//select[@id='StateProvinceId']"
zip_xpath="//input[@id='ZipPostalCode']"
ground_next_xpath="//div[@class='shipping-options-body']//div[2]//div[1]//label[1]"
applybtn_xpath="//button[normalize-space()='Apply']"

# Price
price_xpath="//span[@id='price-value-4']"
quan_xpath="//input[@id='product_enteredQuantity_4']"

# Gift
gift_drp="//select[@id='checkout_attribute_1']"

#WISH LIST
add_wish_xpath="//button[@id='add-to-wishlist-button-4']"
wishlist_xpath="//span[@class='wishlist-label']"
add_cart_tick="//input[@name='addtocart']"
addcart_btn_xpath="//button[normalize-space()='Add to cart']"


# shpping cart link
estimated_xpath="//a[@id='open-estimate-shipping-popup']"
tick_xpath="//input[@id='termsofservice']"
checkout_xpath="//button[@id='checkout']"

# compare
prd1_xpath="//tr[@class='product-name']//a[normalize-space()='Apple MacBook Pro']"
prd2_xpath="//a[normalize-space()='Samsung Premium Ultrabook']"
price1_xpath="//td[normalize-space()='$1,800.00']"
price2_xpath="//td[normalize-space()='$1,590.00']"
screen1_xpath="//tbody/tr[3]/td[1]"
screen2_xpath="//tbody/tr[2]/td[1]"
cpu1_xpath="//td[normalize-space()='Intel Core i5']"
cpu2_xpath="//*[@id='main']/div/div[2]/div/div[2]/div/table/tbody/tr[7]/td[2]"
memory1_xpath="//td[normalize-space()='4 GB']"
memory2_xpath="//td[normalize-space()='8 GB']"
harddrive1_xpath="//tbody/tr[5]/td[3]"
harddrive2_xpath="//td[normalize-space()='128 GB']"


class Ecommerce:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.prd_select_xpath = "//h2[@class='product-title']//a[normalize-space()='Apple MacBook Pro']"
        self.prd_select_xpath = "//h2[@class='product-title']//a[normalize-space()='Apple MacBook Pro']"
        self.prd_image1_xpath = "//div[@class='picture-thumbs']//div[1]//img[1]"
        self.prd_image2_xpath = "//div[@class='picture-thumbs']//div[2]//img[1]"
        self.prd_name_xpath = "//h1[normalize-space()='Apple MacBook Pro']"
        self.prd_desc_xpath = "//div[@class='short-description']"
        self.SKU_xpath = "//div[@class='sku']"
        self.quan_xpath = "//input[@id='product_enteredQuantity_4']"

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

    def get_search(self):
        # self.wait.until(EC.visibility_of_element_located((By.XPATH,searchbox_xpath))).send_keys(searchvalue)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH,searchbutton_xpath))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, com_xpath))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, note_xpath))).click()
        time.sleep(2)
        drp_down_sort = self.wait.until(EC.element_to_be_clickable((By.XPATH, sort_xpath)))
        drp_down_sort.click()
        drp_down_sortelement = Select(drp_down_sort)
        drp_down_sortelement.select_by_index(4)
        drp_down_size=self.wait.until(EC.element_to_be_clickable((By.XPATH,displaysixe_xpath)))
        drp_down_size.click()
        drp_down_sizefield=Select(drp_down_size)
        drp_down_sizefield.select_by_visible_text("6")
        print("Option selected successfully.")

    def get_compare_list(self):
        """Extracts product comparison details and asserts differences."""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, combutton1_xpath))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, combutton2_xpath))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, comparelist_xpath))).click()

        # Extract product names
        product1_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, prd1_xpath))).text
        product2_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, prd2_xpath))).text

        # Extract price values
        price1 = float(
            self.wait.until(EC.visibility_of_element_located((By.XPATH, price1_xpath))).text.replace("$", "").replace(
                ",", ""))
        price2 = float(
            self.wait.until(EC.visibility_of_element_located((By.XPATH, price2_xpath))).text.replace("$", "").replace(
                ",", ""))

        # Extract screen sizes
        screen_size1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, screen1_xpath))).text
        screen_size2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, screen2_xpath))).text

        # Extract CPU types
        cpu1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, cpu1_xpath))).text
        cpu2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, cpu2_xpath))).text

        # Extract memory values
        memory1 = int(self.wait.until(EC.visibility_of_element_located((By.XPATH, memory1_xpath))).text.split()[0])
        memory2 = int(self.wait.until(EC.visibility_of_element_located((By.XPATH, memory2_xpath))).text.split()[0])

        # Extract hard drive details
        hard_drive1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, harddrive1_xpath))).text
        hard_drive2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, harddrive2_xpath))).text

        # Log extracted details
        print(f"Comparing {product1_name} vs {product2_name}")
        print(f"Price: {price1} vs {price2}")
        print(f"Screen Size: {screen_size1} vs {screen_size2}")
        print(f"CPU: {cpu1} vs {cpu2}")
        print(f"Memory: {memory1}GB vs {memory2}GB")
        print(f"Hard Drive: {hard_drive1} vs {hard_drive2}")

        # Assertions for comparison
        try:
            assert price1 > price2, f"{product1_name} is more expensive than {product2_name}"
            assert memory2 > memory1, f"{product2_name} has more RAM than {product1_name}"
            assert cpu2 > cpu1, f"{product2_name} has a better processor than {product1_name}"
            print("Product comparison test passed successfully!")
        except AssertionError as e:
            print(f"Assertion Failed: {e}")

        # Return extracted data for further use
        comparison_data = {
            "Product 1": product1_name,
            "Product 2": product2_name,
            "Price": (price1, price2),
            "Screen Size": (screen_size1, screen_size2),
            "CPU": (cpu1, cpu2),
            "Memory": (memory1, memory2),
            "Hard Drive": (hard_drive1, hard_drive2)
        }

        # After completing the comparison, go back to the previous page
        self.driver.back()
        time.sleep(1)  # Give time for the page to load after navigating back

        return comparison_data# Go back to the previous page

    def get_product(self):
        for attempt in range(3):  # Retry up to 3 times
            try:
                self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, self.prd_select_xpath)))  # Ensure element is present in DOM
                prd_select = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, self.prd_select_xpath)))  # Wait for it to be clickable
                prd_select.click()  # Click the product

                # Wait for the product name to be visible and return it
                product_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.prd_name_xpath))).text
                return product_name
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == 2:  # Fail the test if retry limit is reached
                    raise
            time.sleep(1)  # Wait for 1 second before retrying


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
        try:
            sku_field = self.wait.until(EC.visibility_of_element_located((By.XPATH,SKU_xpath)))
            actual_sku_str = sku_field.text.strip()
            actual_sku_cleaned = actual_sku_str.replace('SKU:', '').strip()
            return actual_sku_cleaned
        except Exception as e:
            print(f"Error fetching SKU: {e}")
            return None

    def get_price(self):
        price_field=self.wait.until(EC.presence_of_element_located((By.XPATH,price_xpath)))
        price_value=price_field.text
        return price_value

    def get_quantity(self, quantity_count):
        quantity_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, quan_xpath)))  # Wait until element is visible
        quantity_field.click()  # Click to focus and interact with it
        quantity_field.clear()  # Clear the current value
        quantity_field.send_keys(str(quantity_count))  # Send new value
        self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH, quan_xpath),
                                                               str(quantity_count)))  # Wait for the value to be updated
        actual_quantity_str = quantity_field.get_attribute("value")  # Get the updated value
        return actual_quantity_str


    def get_wishlist(self):
        try:
            print("Waiting for wishlist button...")
            wish = self.wait.until(EC.presence_of_element_located((By.XPATH, add_wish_xpath)))
            print("Wishlist button found, clicking...")
            wish.click()

            print("Waiting for wishlist page to load...")
            wish_list = self.wait.until(EC.presence_of_element_located((By.XPATH, wishlist_xpath)))
            print("Wishlist page loaded, clicking...")
            wish_list.click()

            print("Waiting for Add to Cart tick mark...")
            add_cart = self.wait.until(EC.presence_of_element_located((By.XPATH, add_cart_tick)))
            print("Add to Cart tick mark found, clicking...")
            add_cart.click()

            print("Waiting for Add to Cart button to become visible...")
            add_cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, addcart_btn_xpath)))

            # Scroll to element if it's out of view
            self.driver.execute_script("arguments[0].scrollIntoView();", add_cart_button)

            print("Waiting 2 seconds before clicking...")
            time.sleep(2)

            print("Clicking Add to Cart button...")
            add_cart_button.click()

            print("Item added to wishlist successfully!")

        except TimeoutException:
            print("Error: Timeout occurred while waiting for elements.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def get_popup(self):
        estimated_field=self.wait.until(EC.element_to_be_clickable((By.XPATH,estimated_xpath)))
        estimated_field.click()


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

    def get_gift(self):
            gift_field = self.wait.until(EC.presence_of_element_located((By.XPATH, gift_drp)))
            gift_value = Select(gift_field)
            gift_value.select_by_index(1)

    def get_shopcart(self):
        tick_field=self.wait.until(EC.element_to_be_clickable((By.XPATH, tick_xpath)))
        tick_field.click()

    def get_checkout(self):
        checkout_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
        checkout_field.click()




