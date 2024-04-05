import unittest
from classes import YoutubeData 

class TestGetChannelID(unittest.TestCase):

    def test_get_channel_id_success(self):

        youtubeData = YoutubeData()
        result = youtubeData.get_channel_id("@Hamza97")
        if result:
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["channel_id"])
        else:
            raise Exception("Getting channel ID, result is None")
