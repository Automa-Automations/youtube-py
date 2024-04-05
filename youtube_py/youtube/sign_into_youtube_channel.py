from typing import Optional
import undetected_chromedriver as uc
from utils import find_element
import time
from selenium.webdriver.common.by import By

def sign_into_youtube_channel(
    driver,
    email: Optional[str] = None,
    password: Optional[str] = None, 
    cookies: Optional[list] = None,
    absolute_chromium_profile_path: Optional[str] = None
):
    if not email and not password and not cookies and not absolute_chromium_profile_path:
        raise Exception("You must provide either an email and password, chromium driver path, or cookies.")

    driver.get("https://youtube.com")
    
    try:
        if cookies:
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            return driver
        
        elif absolute_chromium_profile_path:
            driver = uc.Chrome(absolute_chromium_profile_path)
            driver.get("https://youtube.com")
            return driver

        elif email and password:
            # Sign up button
            sign_in_with_google_link = find_element(driver, By.CSS_SELECTOR, "a[href*='https://accounts.google.com/ServiceLogin']")
            link = sign_in_with_google_link.get_attribute("href")

            if link is None: 
                raise Exception("Could not find sign in with google link.")

            driver.get(link)
       
            email_input = find_element(driver, By.CSS_SELECTOR, "input[type='email']")
            email_input.click()
            email_input.send_keys(email)

            next_button = find_element(driver, By.XPATH, "//button[contains(span/text(), 'Next')]")
            next_button.click()

            time.sleep(3)

            password_input = find_element(driver, By.CSS_SELECTOR, "input[type='password']")
            password_input.click()
            password_input.send_keys(password)

            see_password_checkbox = find_element(driver, By.CSS_SELECTOR, "input[type='checkbox']")
            see_password_checkbox.click()

            next_button = find_element(driver, By.XPATH, "//button[contains(span/text(), 'Next')]")
            next_button.click()

            return driver
        else:
            raise Exception("You must provide either an email and password, chromium driver path, or cookies.")

    except Exception as e:
        print("Error signing into youtube channel: ", e)

        with open("error.txt", "w") as f:
            f.write(str(e))

        return driver
