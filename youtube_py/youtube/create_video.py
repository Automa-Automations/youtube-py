from typing import Optional
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from utils import sign_into_youtube_channel, find_element 
import time

def create_video(
    absolute_video_path: str,
    email: Optional[str] = None,
    password: Optional[str] = None,
    cookies: Optional[str] = None,
    absolute_chromium_profile_path: Optional[str] = None,
):

    if not cookies and not email and not password and not absolute_chromium_profile_path:
        raise ValueError("You need to provide either cookies, chromium profile path, or email and password")

    print("1. Starting the browser...")
    options = uc.ChromeOptions()
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    driver = uc.Chrome(options=options)

    try: 
        print("2. Signing into the youtube channel...")
        driver = sign_into_youtube_channel(driver, cookies=cookies, email=email, password=password, absolute_chromium_profile_path=absolute_chromium_profile_path)

        if not driver:
            raise Exception("Could not sign into youtube channel.")
        
        print("3. Navigate to the upload page...")
        time.sleep(3)
        driver.get("https://youtube.com/upload")

        print("4. Uploading the video...")
        upload_video_input = find_element(driver, By.CSS_SELECTOR, "input[type='file']")
        upload_video_input.send_keys(absolute_video_path)

        not_for_kids_radio = find_element(driver, By.CSS_SELECTOR , "tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']", 100)
        not_for_kids_radio.click()

        visibility_tab = find_element(driver, By.CSS_SELECTOR, "button[id='step-badge-3']")
        visibility_tab.click()

        video_private_radio = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-radio-button[id='private-radio-button']")
        video_private_radio.click()
        
        print("5. Checking if the video was uploaded...")
        while True:
            time.sleep(1)
            progress_label = find_element(driver, By.CSS_SELECTOR, "span[class='progress-label style-scope ytcp-video-upload-progress']")
            if not "Uploading" in progress_label.text:
                break
            print("Still uploading...")

        print("6. Saving the video...")
        save_button = find_element(driver, By.CSS_SELECTOR, "ytcp-button[id='done-button']")
        save_button.click()

        try:
            # Close the close button if it exists
            close_button = find_element(driver, By.CSS_SELECTOR, "ytcp-button[id='close-button']")
            close_button.click()
        except:
            print("Close button didn't exist, no need to close it.")

        time.sleep(5)

        print("7. Getting the video and channel id...")
        # Get channel id
        current_url = driver.current_url
        channel_id = current_url.split("channel/")[1].split("/")[0]

        # if Welcome popup is active, click continue button
        try:
            continue_button = find_element(driver, By.CSS_SELECTOR, "ytcp-button[id='dismiss-button']")
            continue_button.click()
        except:
            print("No need to close welcome popup, it doesn't show up at all.")
        
        # Get video id
        video_href = find_element(driver, By.CSS_SELECTOR, "a[id='video-title']").get_attribute("href")

        video_id = ""

        if video_href:
            video_id = video_href.split("video/")[1].split("/")[0]
        print("8. Video uploaded successfully! Quitting driver")
        
        # Quit driver
        driver.quit()

        return {
            "status": "success",
            "channel_id": channel_id,
            "video_id": video_id,
        }

    except Exception as e:
        print('Error:', e)
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": str(e),
        }
