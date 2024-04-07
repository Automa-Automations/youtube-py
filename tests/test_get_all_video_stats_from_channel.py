import unittest
from youtube_selenium_py.classes import YoutubeData 

class TestGetAllVideoStatsFromChannel(unittest.TestCase):

    def test_get_all_video_stats(self):

        youtubeData = YoutubeData()
        result = youtubeData.get_all_video_stats_from_channel("@Hamza97")

        if result:
            self.assertEqual(result["status"], "success")
            self.assertIsNotNone(result["all_video_stats"])
        else:
            raise Exception("Getting channel ID, result is None")
