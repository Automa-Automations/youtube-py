import unittest
from classes import YoutubeData

class TestGetAllVideoStatsFromChannel(unittest.TestCase):

    def test_edit_channel_success(self):

        youtubeData = YoutubeData()
        result = youtubeData.get_all_video_stats_from_channel(
            "@Hamza97"
        )
        if result:
            # Assert that the channel was created successfully
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["all_video_stats"])
        else:
            raise Exception("Channel edit failed, result is None")
