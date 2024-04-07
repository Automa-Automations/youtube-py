import unittest
from youtube_selenium_py.classes import Youtube
from dotenv import load_dotenv
import os

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestGetMyChannelStats(unittest.TestCase):

    def test_get_my_channel_stats(self):
        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_channel_stats()
        if result:
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Problem getting my channel stats, result is None")

        youtube.close()

