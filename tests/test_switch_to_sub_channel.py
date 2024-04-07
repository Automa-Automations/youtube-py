import unittest
from youtube_selenium_py.classes import Youtube
import os
from dotenv import load_dotenv

load_dotenv()
test_email = os.getenv("TEST_EMAIL") or ""
test_password = os.getenv("TEST_PASSWORD") or ""


class TestSwitchToSubChannel(unittest.TestCase):

    def test_switch_to_sub_channel_success(self):
        # Calling the create_video function with valid parameters

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.switch_to_sub_channel(
            "Adonis Here"
        )

        if result:
            # Asserting that the result is a success
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Channel switching failed, result is None")

        youtube.close()
