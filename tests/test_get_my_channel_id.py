import unittest
from youtube_selenium_py.classes import Youtube
from dotenv import load_dotenv
import os

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestGetMyChannelID(unittest.TestCase):

    def test_get_my_channel_id(self):
        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_channel_id()
        if result:
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Getting channel ID, result is None")

        youtube.close()
