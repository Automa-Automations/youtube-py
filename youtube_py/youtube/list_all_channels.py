from selenium.webdriver.common.by import By
from utils import find_element, find_elements 
import time

def list_all_channels(
    driver
):
    try:
        time.sleep(3)
        print("1. Navigating to youtube.com...")
        if driver.current_url != "https://www.youtube.com/":
            driver.get("https://www.youtube.com/")
        avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar-btn']")
        avatar_button.click()

        switch_account_button = find_element(driver, By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[2]")
        switch_account_button.click()

        channels_items = find_elements(driver, By.CSS_SELECTOR, "ytd-account-item-renderer[thumbnail-size='48']")

        channels_list = []
        print("2. Listing all channels...")
        for i, channel_item in enumerate(channels_items):
            channel_name, channel_handle = channel_item.find_elements(By.CSS_SELECTOR, "yt-formatted-string")[:2]
            print(f"[{i+1}] Channel Name:", channel_name.text)
            print(f"[{i+1}] Channel Handle:", channel_handle.text)
            channels_list.append({
                "channel_name": channel_name.text,
                "channel_handle": channel_handle.text
            })

        print("3. Channels listed successfully.")
        return {
            "channels_list": channels_list,
            "status": "success",
            "message": "Channels listed successfully",
            "driver": driver,
        }

    except Exception as e:
        print(e)
        with open("error.txt", "w") as f:
            f.write(str(e))
        return {
            "status": "error",
            "message": str(e),
            "driver": driver
        } 
