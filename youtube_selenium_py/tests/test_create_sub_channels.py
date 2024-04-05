import unittest
from youtube_selenium_py.classes import Youtube
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestCreateSubChannels(unittest.TestCase):

    def test_create_video_success(self):
        # Calling the create_video function with valid parameters
        youtube = Youtube(email=test_email, password=test_password)

        result = youtube.create_sub_channels(
            sub_channels_names=["John C", "Jack S", "Lupepe T"]
        )

        # Asserting that the result is a success
        self.assertEqual(result["status"], "success")
        youtube.close()

