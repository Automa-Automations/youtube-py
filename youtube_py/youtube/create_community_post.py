from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import find_element, sign_into_youtube_channel, new_driver
from typing import Optional
import re

def create_community_post(
    community_post_title: str,
    community_post_configuration_object: dict,
    email: Optional[str] = None,
    password: Optional[str] = None,
    cookies: Optional[str] = None,
    absolute_chromium_profile_path: Optional[str] = None,
):
    if not cookies and not email and not password and not absolute_chromium_profile_path:
        raise ValueError("You need to provide either cookies, chromium profile path, or email and password")

    print("1. Instantiating driver...")
    driver = new_driver()

    try:
        print("2. Signing into YouTube channel...")
        driver = sign_into_youtube_channel(driver, cookies=cookies, email=email, password=password, absolute_chromium_profile_path=absolute_chromium_profile_path)
        if not driver:
            return {
                "status": "error",
                "message": "Driver invalid"
            }

        print("3. Getting community page link...")
        upload_icon_button = find_element(driver, By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button")
        upload_icon_button.click()
       
        # Find all anchor tags with the specified id
        anchor_tags = driver.find_elements_by_xpath("//a[@id='endpoint']")
        
        # Regular expression pattern to match the href attribute
        pattern = re.compile(r'/channel/[a-zA-Z0-9_-]+/community\?show_create_dialog=1')
        
        # Iterate over each anchor tag
        for anchor_tag in anchor_tags:
            # Get the href attribute value
            href = anchor_tag.get_attribute("href")
            # Check if the href attribute value matches the pattern
            if pattern.match(href):
                print("Going to community page...")
                anchor_tag.click()
                break  # Exit the loop after clicking on the desired element


        channel_id = driver.current_url.split("youtube.com/")[1].split("/")[0]
        driver.quit()


    except Exception as e:
        print('Error:', e)
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": str(e),
        }
