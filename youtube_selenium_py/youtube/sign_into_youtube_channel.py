from typing import Optional
import undetected_chromedriver as uc
from youtube_selenium_py.utils import find_element
import time
from selenium.webdriver.common.by import By

def sign_into_youtube_channel(
    driver,
    email: Optional[str] = None,
    password: Optional[str] = None, 
    cookies: Optional[list] = None,
    absolute_chromium_profile_path: Optional[str] = None
) -> Optional[dict]:
    if not email and not password and not cookies and not absolute_chromium_profile_path:
        raise Exception("You must provide either an email and password, chromium driver path, or cookies.")

    if not email and password and not cookies and not absolute_chromium_profile_path:
        raise Exception("You must provide an email and password.")

    driver.get("https://youtube.com")
    
    if cookies:
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            return {
                "status": "success",
                "driver": driver,
                "message": "Successfully loaded cookies.",
            }
        except Exception as e:
            print("Error adding cookies to driver. Are you sure the cookies are valid?")
            print(str(e))
            return {
                "status": "error",
                "driver": driver,
                "message": "Error loading cookies.",
            }

    
    elif absolute_chromium_profile_path:
        try:
            driver = uc.Chrome(absolute_chromium_profile_path)
            driver.get("https://youtube.com")
            return {
                "status": "success",
                "driver": driver,
                "message": "Successfully loaded Chrome profile.",
            }
        except Exception as e:
            print("Error loading chrome profile. Are you sure the path is correct?")
            print(str(e))
            return {
                "status": "error",
                "driver": driver,
                "message": "Error loading Chrome profile.",
            }

    elif email and password:
        try:
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

            print("Implicitly sleeping for 20 seconds, if your account has two step authentication, or asking for verification code...")
            time.sleep(20)
            
            return {
                "status": "success",
                "driver": driver,
                "message": "Successfully signed into youtube channel.",
            }
        except Exception as e:
            print("Error signing into youtube channel. Are you sure the email and password are correct?")
            print(str(e))
            return {
                "status": "error",
                "driver": driver,
                "message": "Error signing into youtube channel.",
                "error": str(e),
            }
    else:
        print("This should never be reached.")
        return {
            "status": "error",
            "driver": driver,
            "message": "Error signing into youtube channel.",
        }
