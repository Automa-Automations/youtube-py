from typing import Optional
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import find_element
import time

def create_video(
    driver,
    absolute_video_path: str,
    video_title: str,
    video_description: str,
    video_thumbnail_absolute_path: Optional[str] = None,
    video_schedule_date: Optional[str] = None,
    video_schedule_time: Optional[str] = None,
):
    try: 
        print("1. Navigate to the upload page...")
        time.sleep(3)
        driver.get("https://youtube.com/upload")

        print("2. Uploading the video...")
        upload_video_input = find_element(driver, By.CSS_SELECTOR, "input[type='file']")
        upload_video_input.send_keys(absolute_video_path)
        
        print(f"3.1. Adding video title '{video_title}'...")
        # Input title and description of video
        title_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Add a title that describes your video (type @ to mention a channel)']")
        # set_element_innertext(driver, title_input, video_title)
        title_input.click()
        title_input.send_keys(Keys.CONTROL + "a")
        title_input.send_keys(Keys.DELETE)
        title_input.send_keys(video_title)
        
        print(f"3.2. Adding video description '{video_description}'...")
        description_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Tell viewers about your video (type @ to mention a channel)']")
        description_input.click()
        description_input.send_keys(Keys.CONTROL + "a")
        description_input.send_keys(Keys.DELETE)
        description_input.send_keys(video_description)

        # Upload thumbnail if video thumbnail is specified
        if video_thumbnail_absolute_path:
            print("Uploading video thumbnail...")
            thumbnail_input = find_element(driver, By.CSS_SELECTOR, "input[type='file']")
            thumbnail_input.send_keys(video_thumbnail_absolute_path)
            time.sleep(10)
        
        print("3.3. Setting video visibility to 'Not Made for Kids'...")
        not_for_kids_radio = find_element(driver, By.CSS_SELECTOR , "tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']", 100)
        not_for_kids_radio.click()

        print(f"3.4. Setting video visibility to 'Public'...")
        visibility_tab = find_element(driver, By.CSS_SELECTOR, "button[id='step-badge-3']")
        visibility_tab.click()

        video_public_radio = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='PUBLIC']")
        video_public_radio.click()

        # Schedule video if schedule time is specified
        if video_schedule_date and video_schedule_time:
            print(f"3.5. Scheduling video for {video_schedule_date} at {video_schedule_time}...")
            schedule_dropdown_button = find_element(driver, By.CSS_SELECTOR, "ytcp-icon-button[id='second-container-expand-button']")
            schedule_dropdown_button.click()
       
            date_toggle_menu = find_element(driver, By.CSS_SELECTOR, "ytcp-text-dropdown-trigger[id='datepicker-trigger']")
            date_toggle_menu.click()

            date_input = find_element(driver, By.XPATH, "/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
            date_input.clear()
            date_input.click()
            date_input.send_keys(video_schedule_date)
            date_input.send_keys(Keys.ENTER)

            time_toggle_menu = find_element(driver, By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/div[2]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")
            time_toggle_menu.click()

            time_menu = find_element(driver, By.XPATH, "/html/body/ytcp-time-of-day-picker/tp-yt-paper-dialog/tp-yt-paper-listbox")
            # Look through all the children of the time menu (tp-yt-paper-item), and select the one with the same text as the time input.
            for child in time_menu.find_elements(By.CSS_SELECTOR, "tp-yt-paper-item"):
                if child.text == video_schedule_time.replace(" ", " "):
                    child.click()
                    break

        print("4. Checking if the video was uploaded...")
        while True:
            time.sleep(1)
            progress_label = find_element(driver, By.CSS_SELECTOR, "span[class='progress-label style-scope ytcp-video-upload-progress']")
            if not "Uploading" in progress_label.text:
                break
            print("Still uploading...")

        print("5. Saving the video...")
        save_button = find_element(driver, By.CSS_SELECTOR, "ytcp-button[id='done-button']")
        save_button.click()

        try:
            # Close the close button if it exists
            close_button = find_element(driver, By.CSS_SELECTOR, "ytcp-button[id='close-button']")
            close_button.click()
        except:
            print("Close button didn't exist, no need to close it.")

        time.sleep(5)

        print("6. Getting the video and channel id...")
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

        print("7. Video uploaded successfully!")

        return_dict = {
            "status": "success",
            "channel_id": channel_id,
            "video_id": video_id,
            "message": "Video uploaded successfully",
            "driver": driver,
        }

        return return_dict

    except Exception as e:
        print('Error:', e)
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": "An error occurred while uploading video.",
            "error": str(e),
            "driver": driver,
        }
