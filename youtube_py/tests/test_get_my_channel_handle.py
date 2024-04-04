import unittest
from classes import Youtube
from dotenv import load_dotenv
import os

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestGetMyChannelHandle(unittest.TestCase):

    def test_edit_channel_success(self):

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_channel_handle()
        if result:
            # Assert that the channel was created successfully
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Getting channel handle, result is None")

        youtube.close()
