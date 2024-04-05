import unittest
import os
from classes import Youtube
import time
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestCreateChannel(unittest.TestCase):

    def test_create_channel_success(self):
        if not test_email or not test_password:
            self.skipTest("Test email and password not provided")

        youtube = Youtube(email=test_email, password=test_password)
        # Test the create_channel function with valid inputs
        result = youtube.create_channel()

        if result:
            print(result)
            # Assert that the channel was created successfully
            self.assertEqual(result["message"], "Channel created successfully")
            self.assertIsNotNone(result["channel_id"])
            self.assertIsNotNone(result["cookies"])
            self.assertIsNotNone(result["cookies"])
            self.assertIsNotNone(result["channel_name"])
            self.assertIsNotNone(result["channel_handle"])
        else:
            raise Exception("Channel creation failed, result is None")
        
        time.sleep(5)
        youtube.close()
