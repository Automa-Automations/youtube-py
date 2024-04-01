import unittest
from youtube import create_community_post
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

test_image_1 = os.path.abspath("./tests/assets/channel_banner.png")
test_image_2 = os.path.abspath("./tests/assets/channel_logo.jpg")

class TestCreateCommunityPost(unittest.TestCase):

    def test_text_post(self):
        result = create_community_post(
            community_post_title="Hello everyone, how is it going?",
            community_post_configuration_object={
                "type": "text"
            },
            schedule={
                "date": "Apr 5, 2024",
                "time": "6:45 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT-7" # Timezone of the schedule (GMT only)
            },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')

    def test_image_post(self):
        result = create_community_post(
            community_post_title="Hope it is going good...",
            community_post_configuration_object={
                "type": "image",
                "images_absolute_path": [
                    test_image_1, 
                    test_image_2, 
                ], # If you only want to upload one image, you can just provide a string instead of a list.
            },
            schedule={
                "date": "Apr 8, 2024",
                "time": "7:00 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT-8" # Timezone of the schedule (GMT only)
            },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')

    def test_image_poll_post(self):
        result = create_community_post(
            community_post_title="Doing great everybody...",
            community_post_configuration_object={
                "type": "image_poll",
                "options": [
                    {
                        "text": "My Option 1",
                        "image_absolute_path": test_image_1,
                    },
                    {
                        "text": "Another Option 2",
                        "image_absolute_path": test_image_2, 
                    },
                    {
                        "text": "Another one Option 3",
                        "image_absolute_path": test_image_1,
                    },
                ]
            },
            schedule={
                "date": "Apr 11, 2024",
                "time": "3:00 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT-5" # Timezone of the schedule (GMT only)
            },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')

    def test_text_poll_post(self):
        result = create_community_post(
            community_post_title="What option do you choose?",
            community_post_configuration_object={
                "type": "text_poll",
                "options": [
                    "This option",
                    "Or this option",
                    "Or the last Option?"
                ]
            },
            schedule={
                "date": "Apr 5, 2024",
                "time": "1:00 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT-6" # Timezone of the schedule (GMT only)
            },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')

    def test_quiz_post(self):
        result = create_community_post(
            community_post_title="What is the hardest thing there is?",
            community_post_configuration_object={
                "type": "quiz",
                "options": [
                    {
                        "text": "Eating a frog?",
                    },
                    {
                        "text": "Fighting a dragon", # Incorrect answer 
                        "reason_answer": "Reason for answer 1", # This means that this is the correct answer. There may only be one correct answer
                    },
                    {
                        "text": "Stepping on an ant", # Incorrect answer 
                    },
                    ...
                ],
            },
            schedule={
                "date": "Apr 7, 2024",
                "time": "9:30 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT+9" # Timezone of the schedule (GMT only)
            },
            email=test_email,
            password=test_password,
        )
        self.assertEqual(result['status'], 'success')
