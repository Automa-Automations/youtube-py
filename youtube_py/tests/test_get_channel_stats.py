import unittest
from classes import Youtube

class TestGetMyChannelHandle(unittest.TestCase):

    def get_my_channel_handle_success(self):

        youtube = Youtube(email=test_email, password=test_password)
        result = youtube.get_my_channel_handle()
        if result:
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Getting channel handle, result is None")

        youtube.close()
