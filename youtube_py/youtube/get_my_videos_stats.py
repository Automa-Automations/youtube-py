from youtube.list_all_channels import list_all_channels
from youtube.get_all_video_stats_from_channel import get_all_video_stats_from_channel

def get_my_videos_stats(driver):
    result = list_all_channels(driver)
    if result["status"] == "success":
        channel_handle = result["channels_list"][0]['channel_handle']
    else:
        raise Exception("Failed to get my video stats, channel listing not successful.")

    video_stats = get_all_video_stats_from_channel(channel_handle)
    return video_stats
