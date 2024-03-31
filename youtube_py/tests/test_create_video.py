import unittest
from youtube import create_video
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

test_video_path = os.path.abspath("./tests/assets/test_vid.mp4")

class TestCreateVideo(unittest.TestCase):

    def test_create_video_success(self):
        # Calling the create_video function with valid parameters
        result = create_video(
            absolute_video_path=test_video_path,
            email=test_email,
            password=test_password,
        )

        # Asserting that the result is a success
        self.assertEqual(result["status"], "success")
