import unittest
from youtube_selenium_py.classes import YoutubeData
import os

class TestDownloadVideo(unittest.TestCase):

    def test_download_video_success(self):
        youtube_data = YoutubeData()
        path = "./tests/assets"
        absolute_path = os.path.abspath(path)
        result = youtube_data.download_video("vEf2z1YeXws", absolute_path, "test_download_video.mp4")

        if result:
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Video download failed, result is None")
