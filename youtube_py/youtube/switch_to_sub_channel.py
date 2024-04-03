import time
from selenium.webdriver.common.by import By
from utils import find_element, find_elements

def switch_to_sub_channel(
    driver,
    channel_name: str,
):
    try:
        time.sleep(5)
        if driver.current_url != "https://youtube.com":
            driver.get("https://youtube.com")

        print("1. Switching to sub channel...")
        avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar-btn']")
        avatar_button.click()

        switch_account_button = find_element(driver, By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[2]")
        switch_account_button.click()
        
        time.sleep(3)

        channels_items = find_elements(driver, By.CSS_SELECTOR, "ytd-account-item-renderer[thumbnail-size='48']")
        does_sub_channel_exist = False
        for channel_item in channels_items:
            if channel_name in channel_item.text:
                channel_item.click()
                does_sub_channel_exist = True
                break

        time.sleep(3)
        if not does_sub_channel_exist:
            return {
            "status": "error",
            "message": "Sub channel does not exist.",
            "driver": driver
            }
        return {
            "status": "success",
            "message": "Switched to sub channel successfully.",
            "driver": driver
        } 

    except Exception as e:
        return {
            "status": "error",
            "message": "An error occurred while switching to sub channel.",
            "error": str(e),
            "driver": driver
        }
