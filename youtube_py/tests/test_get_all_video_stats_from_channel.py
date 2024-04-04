import unittest
from classes import YoutubeData

class TestGetAllVideoStatsFromChannel(unittest.TestCase):

    def get_all_video_stats_success(self):

        youtubeData = YoutubeData()
        result = youtubeData.get_all_video_stats_from_channel(
            "@Hamza97"
        )
        if result:
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["all_video_stats"])
        else:
            raise Exception("Getting all video stats failed, result is None")
