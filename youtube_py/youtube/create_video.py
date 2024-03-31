from typing import Optional
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from utils import sign_into_youtube_channel, find_element, set_element_innertext
import time

def create_video(

    absolute_video_path: str,
    video_title: str,
    video_description: str,
    video_thumbnail_absolute_path: str,
    video_schedule_date: Optional[str] = None,
    video_schedule_time: Optional[str] = None,
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
        
        # Input title and description of video
        title_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Add a title that describes your video (type @ to mention a channel)']")
        set_element_innertext(driver, title_input, video_title)

        description_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Tell viewers about your video (type @ to mention a channel)']")
        set_element_innertext(driver, description_input, video_description)

        # Upload thumbnail if video thumbnail is specified
        if video_thumbnail_absolute_path:
            thumbnail_input = find_element(driver, By.CSS_SELECTOR, "input['type=file']")
            thumbnail_input.send_keys(video_thumbnail_absolute_path)

        not_for_kids_radio = find_element(driver, By.CSS_SELECTOR , "tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']", 100)
        not_for_kids_radio.click()

        visibility_tab = find_element(driver, By.CSS_SELECTOR, "button[id='step-badge-3']")
        visibility_tab.click()

        video_public_radio = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='PUBLIC']")
        video_public_radio.click()

        # Schedule video if schedule time is specified
        if video_schedule_date and video_schedule_time:
            schedule_dropdown_button = find_element(driver, By.CSS_SELECTOR, "ytcp-icon-button[id='second-container-expand-button']")
            schedule_dropdown_button.click()
       
            date_toggle_menu = find_element(driver, By.CSS_SELECTOR, "ytcp-text-dropdown-trigger[id='datepicker-trigger']")
            date_toggle_menu.click()

            date_input = find_element(driver, By.XPATH, "/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
            date_input.clear()
            date_input.click()
            date_input.send_keys(video_schedule_date)

            time_toggle_menu = find_element(driver, By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/div[2]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
            time_toggle_menu.click()

            time_menu = find_element(driver, By.XPATH, "/html/body/ytcp-time-of-day-picker/tp-yt-paper-dialog/tp-yt-paper-listbox")
            # Look through all the children of the time menu (tp-yt-paper-item), and select the one with the same text as the time input.
            for child in time_menu.find_elements(By.CSS_SELECTOR, "tp-yt-paper-item"):
                if child.text == video_schedule_time:
                    child.click()
                    break

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
