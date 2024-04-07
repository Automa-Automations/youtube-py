import unittest
from youtube_selenium_py.classes import Youtube
from dotenv import load_dotenv
import os

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestGetMyVideosStats(unittest.TestCase):

    def get_my_videos_stats_success(self):

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_videos_stats()
        if result:
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["video_stats"])
        else:
            raise Exception("Getting my video stats failed, result is None")

        youtube.close()
