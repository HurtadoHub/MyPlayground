import time


from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This is a Git Test. Version Control Update 1. #

def test_end2end(browser_instance):
    driver = browser_instance

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_experimental_option("credentials_enable_service", False)
    # chrome_options.add_argument("headless") # headless browser means the service runs without showing the actions, headmode is the default of the browser.
    # chrome_options.add_argument("--ignore-certificate-errors") # This allows you to ignore certificate errors


    # Setting driver and service
    # chrome_srvc = Service("/Users/CHURTADO/Documents/Browser_Drivers/Chrome/chromedriver")
    # driver = webdriver.Chrome(service=chrome_srvc)
    # driver = webdriver.Chrome(service=chrome_srvc, options=chrome_options)


    # Adding waits
    # driver.implicitly_wait(2)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://rahulshettyacademy.com//loginpagePractise/")
        driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
        driver.find_element(By.ID, "password").send_keys("learning")
        driver.find_element(By.ID, "terms").click()
        terms_checkbox = driver.find_element(By.ID, "terms")
        assert terms_checkbox.is_selected() == True
        driver.find_element(By.ID, "signInBtn").click()

###### Code Reminder for working with alerts.. #######
        # wait.until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # alert_message = alert.text
        # print(f"Alert message: {alert_message}")
        # alert.accept()

        # driver.get("https://rahulshettyacademy.com/angularpractice/") # Navigate to page.
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'shop')]"))).click() # Click on "Shop" when its available for click.
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='card h-100']"))) # Explicit wait on table rows to fully load.
        phone_list = driver.find_elements(By.XPATH, "//div[@class='card h-100']") # Created object list for elements in the row.
        print("Available Phones:")
        list_of_phones = []
        for phone in phone_list:
            phone_name = phone.find_element(By.XPATH, ".//h4").text  # Created object list of all available phone names.
            list_of_phones.append(phone_name)  # appending names to list_of_phones
        print(list(list_of_phones))  # Printing all the available phone by header text from a list.
        for phone in phone_list:
            phone_name = phone.find_element(By.XPATH, ".//h4").text
            if phone_name == 'Blackberry': # Applied if condition
                phone.find_element(By.XPATH, ".//div/button").click() # Click Add for element with "Blackberry" in header title.
                print(f"Added {phone_name} to cart.")
                break
        checkout_button = driver.find_element(By.CSS_SELECTOR, "a.nav-link.btn.btn-primary") # New Object. Checkout Button.
        details = checkout_button.text # New Object. Button text details.
        checkout_details = details.replace("(current)", "").strip() # Removing unwanted string text. ridding of leading spaces.
        print(checkout_details) # Printing Checkout text.
        assert "Checkout ( 1 )" in checkout_details, f"Something is wrong. Try Again." # Validation of element text based off conditions.
        checkout_button.click() # Going to Checkout
        wait.until(EC.visibility_of_element_located((By.XPATH, "//td[@class='text-right']//strong"))) # Grabbing desired element once its visible.
        total_price = driver.find_element(By.XPATH, "//td[@class='text-right']//strong").text # New Object. Applying text.
        print("Total Price:", total_price) # Printing total price text.
        final_checkout = driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']") # New Object. Checkout Button.
        final_checkout.click() # Proceeding to Checkout. Click
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='country']"))) # Waiting for input element to be interactable.
        input_field = driver.find_element(By.XPATH, "//input[@id='country']") # New Object. Input field.
        input_field.send_keys("Un") # Typing "Un" for suggestive dropdown to load.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='suggestions']//a"))) # Explicit wait for attributes that hold text to fully load.

        # Running for loop. Iterating off the list of elements and selecting desired element.
        suggestions = driver.find_elements(By.XPATH, "//div[@class='suggestions']//a") # New Object. Suggested items.
        for country in suggestions:
            if country.text == "United States of America": # Only click if iteration lands on "United States of America".
                country.click()
                break
        print(f"Selected, {input_field.get_attribute("value")}") # Printing New displayed input value.

        driver.find_element(By.XPATH, "//label[@for='checkbox2']").click() # Clicking on checkbox for Terms and Conditions
        check_box = driver.find_element(By.XPATH, "//input[@id='checkbox2']") # New Object.  Checkbox
        print(f"Is checkbox selected? {check_box.is_selected()}")
        driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click() # Completing Purchase
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
        success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success_message # asserting partial text # Important. == asserts EXACT text. "in", asserts PARTIAL text.

    except Exception as e:
        print(e)

    except StaleElementReferenceException as e:
        print(e)

    except TimeoutException:
        print("timed out waiting for alert")

    finally:
        print("Test Passed")
        driver.quit()


