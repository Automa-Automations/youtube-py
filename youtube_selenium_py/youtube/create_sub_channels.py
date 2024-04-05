from typing import List
import time
from selenium.webdriver.common.by import By
from youtube_selenium_py.utils import find_element

def create_sub_channels(
    driver,
    sub_channels_names: List[str],
):
    try:
        time.sleep(5)
        for i, sub_channel_name in enumerate(sub_channels_names):
            print(f"[{i + 1}] Creating sub channel: {sub_channel_name}")
            print("1. Navigating to account settings...")
            driver.get("https://youtube.com/account")

            # Get the anchor element with the text inside "Create a new channel"
            try:
                create_channel_link = find_element(driver, By.XPATH, "//a[contains(text(), 'Create a new channel')]")
                create_channel_link.click()
            except:
                add_or_manage_channels_link = find_element(driver, By.XPATH, "//a[contains(text(), 'Add or manage your channel(s)')]")
                add_or_manage_channels_link.click()

                create_channel_link = find_element(driver, By.CSS_SELECTOR, "a[aria-label='Create a channel']")
                create_channel_link.click()
            
            print("2. Entering channel name...")
            channel_name_input = find_element(driver, By.CSS_SELECTOR, "input[id='PlusPageName']")
            channel_name_input.click()
            channel_name_input.send_keys(sub_channel_name)
        
            print("3. Clicking on checkbox...")
            checkbox_input = find_element(driver, By.CSS_SELECTOR, "input[type='checkbox']")
            checkbox_input.click()

            print("4. Creating channel by pressing submit button...")
            submit_input_button = find_element(driver, By.CSS_SELECTOR, "input[id='submitbutton']")
            submit_input_button.click()

            print("5. Waiting for the channel to be created...")
            time.sleep(10)
            
            print(f"Sub channel with name '{sub_channel_name}' created successfully.")

        return {
            "status": "success",
            "message": "Sub channels created successfully.",
            "driver": driver
        }
    except Exception as e:
        print(f"Error: {e}")
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": "An error occurred while creating sub channels.",
            "driver": driver
        }

