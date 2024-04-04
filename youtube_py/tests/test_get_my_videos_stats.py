import unittest
from classes import Youtube
from dotenv import load_dotenv
import os

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestGetMyVideosStats(unittest.TestCase):

    def test_edit_channel_success(self):

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_videos_stats()
        if result:
            # Assert that the channel was created successfully
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["all_video_stats"])
        else:
            raise Exception("Channel edit failed, result is None")
