import unittest
from youtube_selenium_py.classes import Youtube
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

test_video_path = os.path.abspath("./tests/assets/test_vid.mp4")

class TestCreateVideo(unittest.TestCase):

    def test_create_video_success(self):
        # Calling the create_video function with valid parameters
        youtube = Youtube(email=test_email, password=test_password)

        result = youtube.create_video(
            absolute_video_path=test_video_path,
            video_title="Test Title",
            video_description="Test video description",
            video_thumbnail_absolute_path=os.path.abspath("./tests/assets/channel_banner.png"),
            video_schedule_date="Apr 5, 2024",
            video_schedule_time="6:45 PM", # 24-hour format, only 15 minute increments alowed (hour:15, hour:30: hour:45: hour:00)
        )

        # Asserting that the result is a success
        self.assertEqual(result["status"], "success")
        youtube.close()
