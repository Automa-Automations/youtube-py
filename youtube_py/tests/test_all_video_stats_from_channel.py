import unittest
from classes import YoutubeData

class TestAllVideoStatsFromChannel(unittest.TestCase):

    def all_video_stats_from_channel_success(self):

        youtubeData = YoutubeData()
        result = youtubeData.all_video_stats_from_channel(
            "@Hamza97"
        )
        if result:
            # Assert that the channel was created successfully
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["all_video_stats"])
        else:
            raise Exception("Channel edit failed, result is None")
