import unittest
import os
from classes import Youtube
import time
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestListAllChannels(unittest.TestCase):

    def test_list_all_channels_success(self):
        if not test_email or not test_password:
            self.skipTest("Test email and password not provided")

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.list_all_channels()

        if result:
            print(result)
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Channel listing failed, result is None")
        
        time.sleep(5)
        youtube.close()
