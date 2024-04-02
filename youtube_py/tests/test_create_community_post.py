import unittest
from youtube import create_community_post
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

class TestCreateCommunityPost(unittest.TestCase):

    def test_text_post(self):
        result = create_community_post(
            community_post_title="Hello everyone, how is it going?",
            # schedule={
            #     "date": "Apr 5, 2024",
            #     "time": "6:45 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
            #     "GMT_timezone": "GMT-7" # Timezone of the schedule (GMT only)
            # },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')
