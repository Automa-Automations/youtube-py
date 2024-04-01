from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import find_element, sign_into_youtube_channel, new_driver
from typing import Optional
import re

def create_community_post(
    community_post_title: str,
    community_post_configuration_object: dict,
    schedule: Optional[dict] = None,
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
        print(f"Channel ID: {channel_id}")
        
        print("4. Creating community post...")
        
        # Input community post title
        print(f"4.1. Inputting community post title: {community_post_title}...")
        community_post_title_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Share a behind-the-scenes photo']")
        community_post_title_input.click()
        community_post_title_input.send_keys(community_post_title)

        if community_post_configuration_object['type'] == "image":
            image_type_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add an image']")
            image_type_button.click()
            images = community_post_configuration_object['images_absolute_path']

            if isinstance(images, list) and len(images) > 5 or len(images) == 0:
                raise ValueError("You can only upload up to 5 images or GIFs, and at least one image or GIF is required.")

            if isinstance(images, str):
                images = [images]
            
            print(f"4.2. Uploading images: {images}...")
            for image in images:
                image_input = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")[1]
                image_input.send_keys(image)

        elif community_post_configuration_object['type'] == "image_poll":
            image_poll_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add an image poll']")
            image_poll_button.click()

            options = community_post_configuration_object['options']
            total_options = len(options)
            
            # A default poll already has 2 created options
            total_new_options_to_create = total_options - 2

            if total_new_options_to_create == -1:
                print("4.1. Creating poll with one option...")
                # This means that the user just want one option
                delete_option_button = find_element(driver, By.CSS_SELECTOR, "yt-icon-button[class='remove-button style-scope ytd-backstage-image-poll-editor-renderer']")
                delete_option_button.click()

            elif total_new_options_to_create < 0:
                print(f"4.1. Creating poll with {total_options} options...")
                for i in range(total_new_options_to_create):
                    add_option_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add option']")
                    add_option_button.click()
            
            add_image_buttons = driver.find_elements(By.CSS_SELECTOR, "yt-icon-button[class='add-image-icon-button style-scope ytd-backstage-image-poll-editor-renderer]")
            options_inputs = driver.find_elements(By.CSS_SELECTOR, "textarea[maxlength='36']")

            for i, option in enumerate(options):
                print(f"4.2. Creating option [{i + 1}] ...")
                add_image_button = add_image_buttons[i]
                option_input = options_inputs[i]

                add_image_button.click()

                # Now, you can locate the file input element and send the path of the image file
                # TODO: If there is an error here, just send it to the other input, as there are 2 inputs in the dev tools.
                file_input = find_element(driver, By.CSS_SELECTOR, "input[type='file]")
                file_input.send_keys(option["image_absolute_path"])  
                
                print(f"4.3. Inputting option [{i + 1}] text: {option['text']}...")
                option_input.click()
                option_input.send_keys(option["text"])

        elif community_post_configuration_object['type'] == "text_poll":

            text_poll_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add a text poll']")
            text_poll_button.click()

            options = community_post_configuration_object['options']
            total_options = len(options)
            
            # A default poll already has 2 created options
            total_new_options_to_create = total_options - 2

            if total_new_options_to_create == -1:
                print("4.1. Creating poll with one option...")
                # This means that the user just want one option
                delete_option_button = find_element(driver, By.CSS_SELECTOR, "yt-icon-button[class='remove-button style-scope ytd-poll-attachment']")
                delete_option_button.click()

            elif total_new_options_to_create < 0:
                print(f"4.1. Creating poll with {total_options} options...")
                for i in range(total_new_options_to_create):
                    add_another_option_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add another option']")
                    add_another_option_button.click()
                    
            option_inputs = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Add option']")

            for i, option in enumerate(options):
                print(f"4.2. Creating option [{i + 1}] ...")
                option_input = option_inputs[i]
                
                print(f"4.3. Inputting option [{i + 1}] text: {option}...")
                option_input.click()
                option_input.send_keys(option)

        elif community_post_configuration_object['type'] == "quiz":
            quiz_poll_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add a quiz']")
            quiz_poll_button.click()
            
            # Options represent answers, just using it for consistency of names.
            options = community_post_configuration_object['options']
            total_options = len(options)
            
            # A default poll already has 2 created options
            total_new_options_to_create = total_options - 2

            if total_new_options_to_create == -1:
                print("4.1. Creating poll with one option...")
                # This means that the user just want one option
                delete_option_button = find_element(driver, By.CSS_SELECTOR, "yt-icon-button[class='remove-button style-scope ytd-backstage-quiz-editor-renderer']")
                delete_option_button.click()

            elif total_new_options_to_create < 0:
                print(f"4.1. Creating poll with {total_options} options...")
                for i in range(total_new_options_to_create):
                    add_option_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Add answer']")
                    add_option_button.click()
            
                    
            option_inputs = driver.find_elements(By.CSS_SELECTOR, "textarea[maxlength='80']")
            correct_answer_checkboxes = driver.find_elements(By.CSS_SELECTOR, "yt-icon-button[aria-label='Mark as correct answer']")
            for i, option in enumerate(options):
                print(f"4.2. Creating option [{i + 1}] ...")
                option_input = option_inputs[i]
                correct_answer_checkbox = correct_answer_checkboxes[i]

                print(f"4.3. Inputting option [{i + 1}] text: {option['text']}...")
                option_input.click()
                option_input.send_keys(option)

                if "reason_answer" in option:
                    print(f"4.4. Marking option [{i + 1}] as correct answer...")
                    correct_answer_checkbox.click()

                    real_answer_input = find_element(driver, By.CSS_SELECTOR, "Explain why this is correct (optional)")
                    real_answer_input.click()
                    real_answer_input.send_keys(option["reason_answer"])


        elif community_post_configuration_object['type'] != "text":
            raise ValueError("Invalid community post configuration object")

        if schedule:
            print(f"5. Scheduling post for {schedule['date']} at {schedule['time']} in {schedule['GMT_timezone']} timezone...")

            # Arrow down button next to post button.
            print("5.1. Clicking on post additional options button...")
            post_additional_options_button = find_element(driver, By.CSS_SELECTOR, "button=[class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--segmented-end']")
            post_additional_options_button.click()

            print("5.2. Clicking on schedule post menu opener button...")
            schedule_post_menu_opener_button = find_element(driver, By.CSS_SELECTOR, "ytd-menu-service-item-renderer")
            schedule_post_menu_opener_button.click()
            
            print("5.3. Clicking on date picker button...")
            date_picker = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-button[id='date-picker']")
            date_picker.click()

            print("5.4. Inputting date...")
            date_input = find_element(driver, By.CSS_SELECTOR, "input[id='textbox']") 
            date_input.click()
            date_input.send_keys(Keys.CONTROL + "a")
            date_input.send_keys(Keys.DELETE)
            date_input.send_keys(schedule["date"])
            date_input.send_keys(Keys.ENTER)

            print("5.5. Clicking on time picker button...")
            time_picker = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-button[id='time-picker']")
            time_picker.click()

            print("5.6. Selecting time...")
            time_listbox = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-listbox[id='time-listbox']")
            # Get all the tp-yt-paper-item in the time_listbox.
            all_times = time_listbox.find_elements(By.CSS_SELECTOR, "tp-yt-paper-item")
            
            for time in all_times:
                if time.text.strip() == schedule["time"].replace(" ", " "):
                    time.click()
                    break

            print("5.7. Selecting timezone...")
            timezone_picker = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-button[id='timezone-picker']")
            timezone_picker.click()

            timezone_listbox = find_element(driver, By.CSS_SELECTOR, "tp-yt-paper-listbox[id='timezone-listbox']")
            all_timezones_items = timezone_listbox.find_elements(By.CSS_SELECTOR, "tp-yt-paper-item")

            for timezone_list_item in all_timezones_items:
                timezone_GMT_format = timezone_list_item.text.strip().split("(")[1].split(")")[0]

                if timezone_GMT_format == schedule["GMT_timezone"]:
                    timezone_list_item.click()
                    break

            print("5.8. Clicking on schedule button...")
            schedule_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Schedule']")
            schedule_button.click()

            try:
                print("5.9. Clicking on Got it button...")
                got_it_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Got it']")
                got_it_button.click()

                schedule_button = find_element(driver, By.CSS_SELECTOR, "button[aria-label='Schedule']")
                schedule_button.click()
            except:
                print("Not needed to click on Got it button.")

        else:
            print("5. Posting community post...")
            post_button = find_element(driver, By.CSS_SELECTOR, "ytd-button-renderer[id='submit-button']")
            post_button.click()
        driver.quit()


    except Exception as e:
        print('Error:', e)
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": str(e),
        }
