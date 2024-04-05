from youtube.get_all_video_stats_from_channel import get_all_video_stats_from_channel
from youtube.get_my_channel_handle import get_my_channel_handle

def get_my_videos_stats(driver):
    try:
        result = get_my_channel_handle(driver)
        if result['status'] == "success":
            channel_handle = result['channel_handle']
            driver = result['driver']
        else:
            driver = result['driver']
            raise Exception("Error: channel ID not found.")

        video_stats = get_all_video_stats_from_channel(channel_handle)
        return {
            "status": "success",
            "message": "Video stats found.",
            "video_stats": video_stats,
            "driver": driver,
        }
    
    except Exception as e:
        print("Error: " + str(e))

        with open("error.txt", "a") as error_file:
            error_file.write(str(e) + "\n")

        return {
            "status": "error",
            "message": "Video stats not found.",
            "driver": driver,
            "error": str(e),
        }
