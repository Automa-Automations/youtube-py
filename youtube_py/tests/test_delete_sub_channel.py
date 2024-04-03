import unittest
from classes import Youtube
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL") or ""
test_password = os.getenv("TEST_PASSWORD") or ""

class TestDeleteSubChannel(unittest.TestCase):

    def test_create_video_success(self):
        # Calling the create_video function with valid parameters

        youtube = Youtube(email=test_email, password=test_password)
        youtube.switch_to_sub_channel("Jack S")

        result = youtube.delete_channel(
            "Adonis Jamal"
        )

        if result:
            # Asserting that the result is a success
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Channel deletion failed, result is None")

        youtube.close()
