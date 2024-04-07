import unittest
from youtube_selenium_py.classes import YoutubeData

class TestGetChannelStats(unittest.TestCase):
    def test_get_channel_stats_success(self):
        youtube_data = YoutubeData()
        print("in get_channel_stats_success")
        channel_id_result = youtube_data.get_channel_id("@Hamza97")
        if channel_id_result['status'] == 'success':
            result = youtube_data.get_channel_stats(channel_id_result['channel_id'])
            print(result)
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Getting channel id, result is None")
