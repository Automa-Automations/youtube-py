import unittest
from youtube_selenium_py.classes import Youtube
import os
from dotenv import load_dotenv

load_dotenv()
test_email = os.getenv("TEST_EMAIL") or ""
test_password = os.getenv("TEST_PASSWORD") or ""

class TestDeleteChannel(unittest.TestCase):

    def test_delete_channel_success(self):

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.delete_channel(
            test_email
        )

        if result:
            # Asserting that the result is a success
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Channel deletion failed, result is None")

        youtube.close()
