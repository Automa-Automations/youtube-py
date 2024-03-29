import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from utils import find_element
from dotenv import load_dotenv

def create_channel(
    channel_name: str,
    channel_handle: str,
    channel_description: str,
    email: str,
    password: str,
    profile_picture_path: str,
    banner_picture_path: str,
    watermark_picture_path: str,
    contact_email_path: str,
    links: list,
):
    # Global variables for function
    youtube_url = "https://youtube.com"

    # 1. TODO: Navigate to youtube and sign in to google.
    # Instantiate driver
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    # Navigate to Youtube
    driver.get(youtube_url)

    # Get sign in with google url:
    sign_in_with_google_link = find_element(driver, By.CSS_SELECTOR, "a[href*='https://accounts.google.com/ServiceLogin']")
    link = sign_in_with_google_link.get_attribute("href")

    if link is None:
        raise Exception("Could not find sign in with google link.")
    driver.get(link)
    
    # Google sign in with email and password
    email_input = find_element(driver, By.CSS_SELECTOR, "input[type='email']")
    email_input.click()
    email_input.send_keys(email)

    next_button = find_element(driver, By.XPATH, "//button[contains(span/text(), 'Next')]")
    next_button.click()

    password_input = find_element(driver, By.CSS_SELECTOR, "input[type='password']")
    password_input.click()
    password_input.send_keys(password)

    next_button = find_element(driver, By.XPATH, "//button[contains(span/text(), 'Next')]")
    next_button.click()
    # Wait for page to load
    # 2. TODO: Make Youtube channel, don't fill in anything yet, keep the default username and handle.
    # Go to profile page to get channel id.
    avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar_btn']")
    avatar_button.click()

    view_channel_link = find_element(driver, By.XPATH, "//a[contains('View your channel')]")
    next_button.click()
    # 3. TODO: Navigate to profile, get profile ID, and go to youtube studio, to edit page
    # 4. TODO: Edit channel name, description, and handle
    # 5. TODO: Upload thumbnail, banner, watermark, and contact email
    # 6. TODO: Save Youtube Channel.
    # 7. TODO: Return channel ID, success message, and cookies.

