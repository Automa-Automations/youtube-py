import unittest
from youtube_selenium_py.classes import Youtube 
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestCreateCommunityPostSubChannel(unittest.TestCase):

    def test_text_post(self):

        youtube = Youtube(email=test_email, password=test_password)
        youtube.switch_to_sub_channel(
            "Adonis Jamal"
        )
        result = youtube.create_community_post(
            community_post_title="Hello everyone, how is it going?",
            schedule={
                "date": "Apr 5, 2024",
                "time": "6:45 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT-7" # Timezone of the schedule (GMT only)
            },
        )
        self.assertEqual(result['status'], 'success')
        youtube.close()
