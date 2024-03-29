import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
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

    # 2. TODO: Make Youtube channel, don't fill in anything yet, keep the default username and handle.

    # Make youtube channel.
    avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar_btn']")
    avatar_button.click()

    create_channel_link= find_element(driver, By.XPATH, "//a[contains(text(), 'Create a channel')]")
    create_channel_link.click()

    create_channel_button = find_element(driver, By.XPATH, "//button[contains(., 'Create channel')]")
    create_channel_button.click()

    # 3. TODO: Navigate to profile, get profile ID, and go to youtube studio, to edit page

    # Get channel id
    while True:
        current_url = driver.current_url
        if current_url.find("channel/") != -1:
            channel_id = current_url.split("/")[-1]
            break

    # Go to youtube studio basic info tab
    driver.get(f"https://studio.youtube.com/channel/{channel_id}/editing/details")

    # 4. TODO: Edit channel name, description, handle, links, and contact email

    channel_name_input = find_element(driver, By.CSS_SELECTOR, "input[id='brand-name-input']")
    channel_name_input.click()
    channel_name_input.send_keys(Keys.CONTROL + 'a')
    channel_name_input.send_keys(Keys.CONTROL + Keys.BACKSPACE)
    channel_name_input.send_keys(channel_name)

    channel_handle_input = find_element(driver, By.CSS_SELECTOR, "input[id='handle-input']")
    channel_handle_input.click()
    channel_handle_input.send_keys(Keys.CONTROL + 'a')
    channel_handle_input.send_keys(Keys.CONTROL + Keys.BACKSPACE)
    channel_handle_input.send_keys(channel_name)

    channel_description_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Tell viewers about your channel. Your description will appear in the About section of your channel and search results, among other places.']")
    driver.execute_script("arguments[0].innerText = arguments[1];", channel_description_input, channel_description)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for link in links:
        add_link_button = find_element(driver, By.ID, 'add-link-button')
        add_link_button.click()

        # Find all title inputs
        title_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Enter a title"]')

        # Iterate through all title inputs, to get the emtpy input to send the title 
        for title_input in title_inputs:
            # Check if the input has no value or has not been typed in
            if not title_input.get_attribute('value'):
                title_input.click()
                title_input.send_keys(link.title)

        # Find all url inputs 
        url_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Enter a URL"]')

        for url_input in url_inputs:
            # Check if the input has no value or has not been typed in
            if not url_input.get_attribute('value'):
                url_input.click()
                url_input.send_keys(link.url)

    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    contact_email_input = find_element(driver, By.CSS_SELECTOR, 'input[placeholder="Email address"]')
    contact_email_input.click()
    contact_email_input.send_keys(contact_email_path)

    # 5. TODO: Upload thumbnail, banner, watermark
    # 6. TODO: Save Youtube Channel.
    # 7. TODO: Return channel ID, success message, and cookies.

