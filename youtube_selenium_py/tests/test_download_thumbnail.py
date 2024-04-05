import unittest
from classes import YoutubeData
import os

class TestDownloadThumbnail(unittest.TestCase):

    def test_download_thumbnail_success(self):
        youtube_data = YoutubeData()
        path = "./tests/assets"
        absolute_path = os.path.abspath(path)
        result = youtube_data.download_thumbnail("vEf2z1YeXws", absolute_path, "video_thumbnail_test")
        print(f"Result: {result}")

        if result:
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Video thumbnail download failed, result is None")
