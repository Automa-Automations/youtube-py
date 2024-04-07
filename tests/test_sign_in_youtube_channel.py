import unittest
import json
import os
from youtube_selenium_py.classes import Youtube
import time
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")
absolute_chromium_profile_path = os.getenv("ABSOLUTE_CHROMIUM_PROFILE_PATH")

# Get cookies from "cookies.json" file

# Read JSON data from file
with open('cookies.json', 'r') as file:
    cookies = json.load(file)

class TestSignInYoutubeChannel(unittest.TestCase):

    def sign_in_email_password_success(self):
        if not test_email or not test_password:
            self.skipTest("Test email and password not provided")

        youtube = Youtube(email=test_email, password=test_password)
        sign_in_result = youtube.sign_in_result

        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)
        
        time.sleep(5)
        youtube.close()

    def sign_in_email_password_fail(self):
        if not test_email or not test_password:
            self.skipTest("Test email and password not provided")

        youtube = Youtube(email=test_email, password="hello")

        sign_in_result = youtube.sign_in_result
        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)

        time.sleep(5)
        youtube.close()

    def sign_in_cookies_success(self):
        if not cookies:
            self.skipTest("Cookies not provided")

        youtube = Youtube(cookies=cookies)

        sign_in_result = youtube.sign_in_result
        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)

        time.sleep(5)
        youtube.close()
    def sign_in_cookies_fail(self):
        if not cookies:
            self.skipTest("Cookies not provided")

        youtube = Youtube(cookies=[{"dumy": "Hello"}])

        sign_in_result = youtube.sign_in_result
        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)

        time.sleep(5)
        youtube.close()
    def sign_in_chromium_path_success(self):
        if not absolute_chromium_profile_path:
            self.skipTest("Chromium path not provided")

        youtube = Youtube(absolute_chromium_profile_path=absolute_chromium_profile_path)
       
        sign_in_result = youtube.sign_in_result
        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)

        time.sleep(5)
        youtube.close()

    def sign_in_chromium_path_fail(self):
        if not absolute_chromium_profile_path:
            self.skipTest("Chromium path not provided")

        youtube = Youtube(absolute_chromium_profile_path="./bob")
       
        sign_in_result = youtube.sign_in_result
        if sign_in_result['status'] == "success":
            print("Sign in successful")
            self.assertTrue(True)
        else:
            print("Sign in failed")
            print(sign_in_result)
            self.assertTrue(False)

        time.sleep(5)
        youtube.close()
