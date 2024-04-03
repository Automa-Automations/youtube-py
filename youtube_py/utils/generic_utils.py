from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import random

# Short function to find element, using webdriver wait
def find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def find_elements(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )

# Simple function to scroll to bottom of screen.
def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def set_element_innertext(driver, element, text):
    driver.execute_script("arguments[0].innerText = arguments[1];", element, text)

def new_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    driver = uc.Chrome(options=options)
    return driver

def gen_random_string(length=8):
    random_string = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(length))
    return random_string
