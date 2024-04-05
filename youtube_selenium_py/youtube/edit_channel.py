from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from youtube_selenium_py.utils import find_element, scroll_to_bottom, set_element_innertext, gen_random_string
import time

def edit_channel(
    driver,
    channel_name: str,
    channel_handle: str,
    channel_description: str,
    profile_picture_path: str,
    banner_picture_path: str, watermark_picture_path: str,
    contact_email_path: str,
    links: list,
):
    try:
        print("1. Navigating to channel page...")
        avatar_button = find_element(driver, By.CSS_SELECTOR, "button[id='avatar-btn']")
        avatar_button.click()
        
        # Get anchor element with text "View your channel"
        view_channel_link = find_element(driver, By.XPATH, "//a[contains(text(), 'View your channel')]")
        view_channel_link.click()

        print("2. Getting channel ID...")
        while True:
            current_url = driver.current_url
            if current_url.find("channel/") != -1:
                channel_id = current_url.split("/")[-1]
                if "?" in channel_id:
                    channel_id = channel_id.split("?")[0]
                break

        print("3. Navigating to basic info tab...")
        driver.get(f"https://studio.youtube.com/channel/{channel_id}/editing/details")

        # If Welcome to Youtube Studio popup opens:
        try:
            continue_button = find_element(driver, By.XPATH, '//ytcp-button[.//div[text()="Continue"]]')
            continue_button.click()
        except:
            print("No welcome popup found.")

        print("4. Filling in channel details...")
        channel_name_input = find_element(driver, By.CSS_SELECTOR, "input[id='brand-name-input']")
        channel_name_input.click()
        channel_name_input.send_keys(Keys.CONTROL + 'a')
        channel_name_input.send_keys(Keys.CONTROL + Keys.BACKSPACE)
        channel_name_input.send_keys(channel_name)

        channel_handle_input = find_element(driver, By.CSS_SELECTOR, "input[id='handle-input']")
        channel_handle_input.click()
        channel_handle_input.send_keys(Keys.CONTROL + 'a')
        channel_handle_input.send_keys(Keys.CONTROL + Keys.BACKSPACE)
        channel_handle_input.send_keys(channel_handle)

        time.sleep(5)
        while True:
            try:
                # Check if the text "This handle isn't available" is somewhere visible on the screen
                if find_element(driver, By.XPATH, '//*[contains(text(), "This handle isn\'t available.")]'):
                    channel_handle  = gen_random_string(9)
                    channel_handle_input = find_element(driver, By.CSS_SELECTOR, "input[id='handle-input']")
                    channel_handle_input.click()
                    channel_handle_input.clear()
                    channel_handle_input.send_keys(channel_handle)
                    time.sleep(3)
                else:
                    break
            except:
                break

        channel_description_input = find_element(driver, By.CSS_SELECTOR, "div[aria-label='Tell viewers about your channel. Your description will appear in the About section of your channel and search results, among other places.']")
        set_element_innertext(driver, channel_description_input, channel_description)

        print("5. Filling in contact channel links...")
        scroll_to_bottom(driver)

        for i, link in enumerate(links):
            print(f"[{i+1}] Adding link...")
            add_link_button = find_element(driver, By.ID, 'add-link-button')
            add_link_button.click()

            print(f"[{i+1}] Adding title: {link['title']}")
            # Find all title inputs
            title_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Enter a title"]')

            # Iterate through all title inputs, to get the emtpy input to send the title 
            for title_input in title_inputs:
                # Check if the input has no value or has not been typed in
                if not title_input.get_attribute('value'):
                    title_input.click()
                    title_input.send_keys(link['title'])

            print(f"[{i+1}] Adding URL: {link['url']}")
            # Find all url inputs
            url_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder="Enter a URL"]')

            for url_input in url_inputs:
                # Check if the input has no value or has not been typed in
                if not url_input.get_attribute('value'):
                    url_input.click()
                    url_input.send_keys(link['url'])

        scroll_to_bottom(driver)

        print("6. Filling in contact email...")
        contact_email_input = find_element(driver, By.CSS_SELECTOR, 'input[placeholder="Email address"]')
        contact_email_input.click()
        contact_email_input.send_keys(contact_email_path)

        print("7. Navigating to branding tab...")
        branding_navigation_button = find_element(driver, By.XPATH, "//ytcp-ve[span[contains(text(), 'Branding')]]")
        branding_navigation_button.click()
        
        print("8. Uploading profile picture, banner, and watermark...")
        # Upload profile picture
        thumbnail_upload_file_input = find_element(driver, By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[2]/ytcp-channel-editing-images-tab/div/section[1]/ytcp-profile-image-upload/div/div[3]/div[2]/div[2]/input")
        thumbnail_upload_file_input.send_keys(profile_picture_path)
        done_button = find_element(driver, By.XPATH, "/html/body/ytcp-profile-image-editor/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]")
        done_button.click()

        # Upload banner
        banner_upload_file_input = find_element(driver, By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[2]/ytcp-channel-editing-images-tab/div/section[2]/ytcp-banner-upload/div/div[3]/div[2]/div[2]/input")
        banner_upload_file_input.send_keys(banner_picture_path)
        done_button = find_element(driver, By.XPATH, "/html/body/ytcp-banner-editor/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]")
        done_button.click()

        # scroll to bottom
        scroll_to_bottom(driver)

        # Upload watermark
        watermark_upload_file_input = find_element(driver, By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[2]/ytcp-channel-editing-images-tab/div/section[3]/ytcp-video-watermark-upload/div/div[3]/div[2]/div[2]/input")
        watermark_upload_file_input.send_keys(watermark_picture_path)
        done_button = find_element(driver, By.XPATH, "/html/body/ytcp-video-watermark-image-editor/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]")
        done_button.click()

        print("9. Publishing channel...")
        time.sleep(3)
        publish_button = find_element(driver, By.XPATH, '//ytcp-button[@id="publish-button"]')
        publish_button.click()
        time.sleep(30)

        print("10. Channel edited successfully.")
        return {
            "status": "success",
            "message": "Channel edited successfully",
            "channel_id": channel_id,
            "channel_name": channel_name,
            "channel_handle": channel_handle,
            "driver": driver,
        }

    except Exception as e:
        print("Error: ", e)
        with open("error.txt", "w") as file:
            file.write(str(e))
        return {
            "status": "error",
            "message": "An error occurred while editing channel.",
            "error": str(e),
            "driver": driver,
        }
