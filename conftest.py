# Pytest read from this directory. conftest can be treated as a global directory/ placeholder for your project test packages.
# Every pytest.py file you make reads from this file if created and applied.


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


###### Notes ######

# In this instance, you can utilize command line options to "choose" your browser instance
# In the example below, chrome and firefox are setup.
# to send commands, you must add the "request" argument within the method.
    # Example:
    # def myMethod(request):
# After, create the object of choice to assign the request script to
# Set, "browser" as the object
# Apply to it, "request.config.getoption("browser")"
    # This script reads from the terminal.


###### IMPORTANT SETUP ######
# You must register command tools if wanting to properly work within your test.
# To do so, grap the correct script from https://docs.pytest.org/en/stable/example/simple.html
# Customize script below to fit your own setup.

# Template:
# def pytest_adoption(parser): parser.adoption("--cmdopt", action="store", default="type1", help="my option: type1 or type2")

def pytest_addoption(parser): parser.addoption("--browser", action="store", default="chrome", help="This is a browser selection")

###### Applied and Run ######
# Once this is applied,
# Within cmd/terminal, run command,
    #  cd /Users/CHURTADO/PycharmProjects/PythonProject/Main_Pytest_Runs  - This takes you to the project folder path
# Then run,
    # pytest test_End_to_End_Framework.py --browser firefox
    # OR
    # pytest test_End_to_End_Framework.py --browser chrome


@pytest.fixture(scope="function")
def browser_instance(request):
    browser = request.config.getoption("browser") # Read Notes Above.
    if browser == "chrome": # firefox
        chrome_options = ChromeOptions() # Creating an object for chrome option assignment.
        chrome_options.add_argument("--start-maximized") # Maximizes window option
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False} # This pref tuple is absolutely necessary to apply. not the arguments itself, but the setup.
        # Above, Disabling password warnings and password manager.
        chrome_options.add_experimental_option("prefs", prefs) # Applying "prefs" to the experimental_option method.
        driver = webdriver.Chrome(options=chrome_options) # Pulling the Service automatically from Selenium and Pulling the custom chrome_options above.
        driver.implicitly_wait(3) # Adding an Implicit wait of 3 seconds.
    elif browser == "firefox":
        firefox_options = FirefoxOptions() # Creating an object for firefox option assignment.
        firefox_options.add_argument("--start-maximized") # Maximizes window option
        firefox_options.set_preference("signon.rememberSignons", False) # Removing Password Manager options
        firefox_options.set_preference("signon.autofillForms", False) # Removing Password Manager options
        firefox_options.set_preference("signon.generation.enabled", False) # Removing Password Manager options
        driver = webdriver.Firefox(options=firefox_options) # Pulling the Service automatically from Selenium and Pulling the custom firefox_options above.
        driver.implicitly_wait(3)
    yield driver # This yields the entire fixture then returns back to the driver...entire driver runs, then comes back here to close.
    # Before test function execution
    driver.quit() # After test function execution
