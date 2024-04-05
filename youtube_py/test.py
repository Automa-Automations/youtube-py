import tests 
import unittest

tests = {
    "test_create_channel": tests.TestCreateChannel,
    "test_create_sub_channels": tests.TestCreateSubChannels,
    "test_edit_channel": tests.TestEditChannel,
    "test_edit_sub_channel": tests.TestEditSubChannel,
    "test_create_video": tests.TestCreateVideo,
    "test_create_video_sub_channel": tests.TestCreateVideoSubChannel,
    "test_create_community_post": tests.TestCreateCommunityPost,
    "test_create_community_post_sub_channel": tests.TestCreateCommunityPostSubChannel,
    "test_delete_channel": tests.TestDeleteChannel,
    "test_delete_sub_channel": tests.TestDeleteSubChannel,
    "test_switch_to_sub_channel": tests.TestSwitchToSubChannel,
    "test_list_all_channels": tests.TestListAllChannels,
    "test_get_my_videos_stats": tests.TestGetMyVideosStats,
    "test_get_all_video_stats_from_channel": tests.TestGetAllVideoStatsFromChannel,
    "test_get_video_stats": tests.TestGetVideoStats,
    "test_get_my_channel_handle": tests.TestGetMyChannelHandle,
    "test_get_my_channel_id": tests.TestGetMyChannelID,
    "test_get_channel_id": tests.TestGetChannelID,
    "test_get_my_channel_stats": tests.TestGetMyChannelStats,
    "test_get_channel_stats": tests.TestGetChannelStats,
    "test_download_video": tests.TestDownloadVideo,
    "test_download_thumbnail": tests.TestDownloadThumbnail,
}

def main():
    # Option 0: Run all tests
    print("0. Run all tests")
    for index, test in enumerate(tests):
        print(f"{index+1}. {test}")
    choice = int(input("Enter the number of the test you want to run: "))
    if choice == "0":
        # run all tests
        suite = unittest.TestSuite()
        # continue
        suite.addTests([unittest.TestLoader().loadTestsFromTestCase(test) for test in tests.values()])
        unittest.TextTestRunner().run(suite)
    test = list(tests.values())[choice-1]
    test = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner().run(test)

main()
