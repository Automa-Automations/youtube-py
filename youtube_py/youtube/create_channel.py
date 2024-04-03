from selenium.webdriver.common.by import By
from utils import find_element
import time

def create_channel(
    driver,
):

    try:
        print("1. Creating channel...")
        youtube_url = "https://youtube.com"
        time.sleep(5)
        if driver.current_url != youtube_url:
            driver.get("https://youtube.com")

        avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar-btn']")
        avatar_button.click()

        create_channel_link= find_element(driver, By.XPATH, "//a[contains(text(), 'Create a channel')]")
        create_channel_link.click()

        create_channel_button = find_element(driver, By.XPATH, "//button[contains(., 'Create channel')]")
        create_channel_button.click()

        print("2. Getting channel ID...")
        while True:
            current_url = driver.current_url
            if current_url.find("channel/") != -1:
                channel_id = current_url.split("/")[-1]
                if "?" in channel_id:
                    channel_id = channel_id.split("?")[0]
                break

        # Data to be returned
        data = {
            "status": "success",
            "channel_id": channel_id, 
            "message": "Channel created successfully", 
            "cookies": driver.get_cookies(),
            "driver": driver
        }

        print("10. Channel created successfully.")
        print("Return Data: ", data)
        return data

    except Exception as e:
        print("Error: ", e)
        with open("error.txt", "w") as file:
            file.write(str(e))
        return {
            "status": "error",
            "message": "An error occurred while creating channel.",
            "error": str(e),
            "driver": driver,
        }
