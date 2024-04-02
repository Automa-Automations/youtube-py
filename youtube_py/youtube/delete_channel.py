from selenium.webdriver.common.by import By
from utils import find_element
import time

def delete_channel(
    driver,
    email: str,
):
    try:
        time.sleep(5)
        driver.get("https://www.youtube.com/account_advanced")

        # Get the anchor element with the text "Delete channel"
        delete_channel_link = find_element(driver, By.XPATH, "//a[text()='Delete channel']")
        delete_channel_link.click()

        permanently_delete_button = find_element(driver, By.CSS_SELECTOR, "button[id='sectioni8']")
        permanently_delete_button.click()

        checkbox_1 = find_element(driver, By.XPATH, "/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[5]/div[2]/div/div[1]/div/div[1]/div/input")
        checkbox_1.click()

        checkbox_2 = find_element(driver, By.XPATH, "/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[5]/div[2]/div/div[2]/div/div[1]/div/input")
        checkbox_2.click()

        delete_button = find_element(driver, By.XPATH, "/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[5]/div[2]/div/div[3]/div/div/button")
        delete_button.click()

        email_address_input = find_element(driver, By.XPATH, "/html/body/div[13]/div[2]/div/div[1]/div/div[1]/div/div/label/input")
        email_address_input.send_keys(email)

        delete_content_button = find_element(driver, By.XPATH, "/html/body/div[13]/div[2]/div/div[2]/div[2]/button")
        delete_content_button.click()

        time.sleep(10)

        return {
            "status": "success",
            "driver": driver,
            "message": "Channel deletion successful"
        }

    except Exception as e:

        with open("error.txt", "w") as f:
            f.write(str(e))

        print("Error occurred with deleting channel.")

        return {
            "status": "error",
            "message": "An error occurred while deleting channel",
            "driver": driver,
            "error": str(e)
       }
