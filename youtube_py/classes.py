from typing import Optional, List
import youtube 
from utils import new_driver
from dataclasses import dataclass

@dataclass
class Youtube:
    email: Optional[str] = None
    password: Optional[str] = None
    absolute_chromium_profile_path: Optional[str] = None
    cookies: Optional[list] = None
    
    def __post_init__(self):
        if self.email is None and self.password is None and self.absolute_chromium_profile_path is None and self.cookies is None:
            raise Exception("Please provide either email and password or cookies and absolute_chromium_profile_path.")
        self.driver = new_driver()  # Assuming new_driver() is defined somewhere
        self.sign_in()

    def sign_in(self):
        driver = youtube.sign_into_youtube_channel(self.driver, self.email, self.password, self.cookies, self.absolute_chromium_profile_path)
        # Set class driver to driver
        self.driver = driver
    
    def create_channel(
        self, 
    ):
        """
        Function to create a Youtube channel. 
        Returns:
        - example success return object: {
            "status": "success",
            "channel_id": channel_id, 
            "channel_name": default_channel_name,
            "channel_handle": default_channel_handle,
            "message": "Channel created successfully", 
            "cookies": driver.get_cookies(),
            "driver": driver
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while creating channel."
            "error": error_message,
            "driver": driver
        }
        """
        result = youtube.create_channel(
            self.driver,
        )
        self.driver = result['driver']

        print(result)

        return result

    def edit_channel(
        self,
        channel_name: str,
        channel_handle: str,
        channel_description: str,
        profile_picture_path: str,
        banner_picture_path: str, watermark_picture_path: str,
        contact_email_path: str,
        links: list,
    ):
        """
        Function to edit channel

        Parameters:
        - channel_name (str): name of the channel.
        - channel_handle (str): channel handle/username.
        - channel_description (str): description of the channel.
        - profile_picture_path (str): path of the profile picture of the channel.
        - banner_picture_path (str): path of the banner picture of the channel.
        - watermark_picture_path (str): path of the watermark picture of the channel.
        - contact_email_path (str): path of the contact email of the channel.
        - links (list[dict]): list of links to be added to the channel.
            - Format of links:
            [
                {
                    "title": str,
                    "url": str,
                },
                {
                    "title": str,
                    "url": str,
                },
                ...
            ]
        Returns:
        - example success return object: {
            "status": "success",
            "message": "Channel edited successfully",
            "channel_id": channel_id,
            "channel_name": channel_name,
            "channel_handle": channel_handle, # if channel_handle is unavailable, it will use a random string as the new channel handle.
            "driver": driver
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while editing channel.",
            "error": str(e),
            "driver": driver,
        }
        """
        result = youtube.edit_channel(
            self.driver,
            channel_name,
            channel_handle,
            channel_description,
            profile_picture_path,
            banner_picture_path,
            watermark_picture_path,
            contact_email_path,
            links
        )
        self.driver = result['driver']
        return result


    def create_video(
        self,
        absolute_video_path: str,
        video_title: str,
        video_description: str,
        video_thumbnail_absolute_path: Optional[str] = None,
        video_schedule_date: Optional[str] = None,
        video_schedule_time: Optional[str] = None,
    ):
        """
        Function to upload a video to a Youtube channel. 

        Parameters:
        - absolute_video_path (str): absolute path of video to be uploaded.
        - video_title (str): title of the video.
        - video_description (str): description of the video.
        - video_thumbnail_absolute_path (Optional[str]): absolute path of the thumbnail of the video.
        - video_schedule_date (Optional[str] -> format: 'Apr 5, 2024'): date to schedule the video.
        - video_schedule_time (Optional[str] -> format: '6:45 PM'): time to schedule the video.
        
        Returns:
        - example success return object: {
            "status": "success",
            "channel_id": channel_id,
            "video_id": video_id,
            "message": "Video uploaded successfully",
            "driver": driver,
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while uploading video.",
            "error": error_message,
            "driver": driver,
        }
        """
        result = youtube.create_video(
            self.driver,
            absolute_video_path,
            video_title,
            video_description,
            video_thumbnail_absolute_path,
            video_schedule_date,
            video_schedule_time,
        )
        self.driver = result['driver']
        return result

    def create_community_post(
        self, 
        community_post_title: str,
        schedule: Optional[dict] = None,
    ):
        """
        Function to create a community post on a Youtube channel.

        Parameters:
        - community_post_title (str): title of the community post.
        - schedule (Optional[dict]): time to schedule the post.
            The schedule object must follow the example below:
            {
                "date": "Apr 5, 2024",
                "time": "6:45 PM", # Only 15 minute increments (hour:0, hour:15, hour: 30, hour: 45)
                "GMT_timezone": "GMT+11" # Timezone of the schedule (GMT only)
            }

        Returns:
        - example success return object: {
            "status": "success", 
            "message": "Community post created successfully", 
            "driver": driver,
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while creating community post."
            "error": error_message,
            "driver": driver
        }
        """
        result = youtube.create_community_post(
            self.driver,
            community_post_title,
            schedule,
        )
        self.driver = result['driver'] 
        return result

    def delete_channel(
        self,
        email: str,
    ):
        """
        Function to delete youtube channel permanently.

        Parameters:
        email (str): email of the channel.
        
        Returns:
        - example success return object: {
            "status": "success",
            "driver": driver,
            "message": "Channel deletion successful"
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while deleting channel",
            "driver": driver,
            "error": str(e)
        }
        """
        result = youtube.delete_channel(self.driver, email)
        self.driver = result['driver']
        return result

    def delete_sub_channel(
        self,
        channel_name: str,
    ):
        """
        Function to delete sub youtube channel permanently.

        Parameters:
        channel_name (str): channel name of the channel.
        
        Returns:
        - example success return object: {
            "status": "success",
            "driver": driver,
            "message": "Channel deletion successful"
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while deleting channel",
            "driver": driver,
            "error": str(e)
        }
        """
        result = youtube.delete_channel(self.driver, channel_name)
        self.driver = result['driver']
        return result

    def close(self):
        """
        Function to close Chromium driver. Call this function when you want the driver to be closed.

        Parameters:
        - None

        Returns (no errors):
        {
            "status": "success",
            "message": "Driver closed successfully"
        }
        """
        if self.driver:
            self.driver.quit()

            return {
                "status": "success",
                "message": "Driver closed successfully"
            }
        else:
            raise Exception("Driver not found")

    def create_sub_channels(
        self,
        sub_channels_names: List[str],
        ):
        """
        Function to create sub channels. This function will only work if the channel is already verified.

        Parameters:
        - sub_channels_names (List[str]): list of sub channels names to be created.
        """
        result = youtube.create_sub_channels(self.driver, sub_channels_names)

        if result:
            self.driver= result['driver']
            return result
        else:
            raise Exception("An error occurred while creating sub channels. Result is None.")

    def switch_to_sub_channel(
        self,
        channel_name: str, # You can also put the channel handle as the value for channel_name, will still work. That way, it will be more accurate if there is multiple channels with the same name.
    ):
        """
        Function to switch to a sub channel.
        Parameters:
        - channel_name (str): channel name or handle of the sub channel to switch to.
        Returns:
        - example success return object: {
            "status": "success",
            "message": "Switched to sub channel successfully.",
            "driver": driver
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while switching to sub channel.",
            "error": str(e),
            "driver": driver
        }
        """
        result = youtube.switch_to_sub_channel(self.driver, channel_name)
        self.driver = result['driver']
        return result
    
    def list_all_channels(
        self
    ):
        """
        Function to list all channels for account.

        Parameters:
        - None

        Returns:
        - example success return object: {
            "channels_list": channels_list,
            "status": "success",
            "message": "Channels listed successfully",
        }
        - example error return object: {
            "status": "error",
            "message": str(e),
            "driver": driver
        }
        """
        result = youtube.list_all_channels(self.driver)
        self.driver = result['driver']
        return result

    def get_my_videos_stats(self):
        """
        Function to get all video stats of the channel.
        Parameters:
        - None
        Returns:
        - example success return object: {
            "status": "success",
            "message": "Video stats found.",
            "video_stats": video_stats,
            "driver": driver,
        }
        # Format of all_video_stats:
        [
            {
                "kind": "youtube#video",
                "etag": "eAGZdVWxoBjCKRPIjFKF64WuM7Q",
                "id": "0P1FGtdg8o8",
                "snippet": {
                    "publishedAt": "2024-04-03T17:00:02Z",
                    "channelId": "UCWsslCoN3b_wBaFVWK_ye_A",
                    "title": "What happened in Vegas",
                    "description": "Email list: https://hamza-ahmed.co.uk/UnfilteredWisdom\nThe only product I sell: https://www.skool.com/adonis\nInstagram: https://www.instagram.com/cultleaderhamza\nTwitter: https://twitter.com/HamzaAdonis",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "Hamza Ahmed",
                    "tags": [
                        "hamza ahmed",
                        "hamza",
                        "hamza97",
                        "self improvement",
                        "entrepreneur",
                        "entrepreneurship",
                        "beginners business",
                        "business",
                        "youtube subscribers",
                        "masculinity"
                    ],
                    "categoryId": "27",
                    "liveBroadcastContent": "none",
                    "defaultLanguage": "en-US",
                    "localized": {
                        "title": "What happened in Vegas",
                        "description": "Email list: https://hamza-ahmed.co.uk/UnfilteredWisdom\nThe only product I sell: https://www.skool.com/adonis\nInstagram: https://www.instagram.com/cultleaderhamza\nTwitter: https://twitter.com/HamzaAdonis"
                    },
                    "defaultAudioLanguage": "en-US"
                },
                "statistics": {
                    "viewCount": "31662",
                    "likeCount": "2255",
                    "favoriteCount": "0",
                    "commentCount": "582"
                }
            },
            ...
        ]
        - example error return object: {
            "status": "error",
            "message": "Video stats not found.",
            "driver": driver,
            "error": str(e),
        }
        """
        result = youtube.get_my_videos_stats(self.driver)
        self.driver = result['driver']
        return result
    
    def get_my_channel_handle(self):
        """
        Function to get channel handle of the channel.
        Parameters:
        - None
        Returns:
        - example success return object: {
            "status": "success",
            "message": "Channel ID found.",
            "channel_handle": channel_handle,
            "driver": driver
        }
        - example error return object: {
            "status": "error",
            "message": "Channel ID not found.",
            "driver": driver
        }
        """
        result = youtube.get_my_channel_handle(self.driver)
        self.driver = result['driver']
        return result

    def get_my_channel_id(self):
        """
        Function to get your channel id

        Parameters:
        - None

        Returns:
        - example success return object: {
            "status": "success",
            "channel_id": channel_id,
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while converting handle to channel id.",
            "error": str(e),
        }
        """
        result = self.get_my_channel_handle()
        if result['status'] == 'success':
            channel_id_result = youtube.get_channel_id(result['channel_handle'])
            if channel_id_result['status'] == 'success':
                return channel_id_result
            else:
                return channel_id_result
        else:
            return result

    def get_my_channel_stats(self):
        """
        Function toe get your channel stats.

        Parameters:
        - None

        Returns:
        - example success return object: {
            "status": "success",
            "message": "Channel stats found.",
            "channel_stats": channel_stats,
            "driver": driver
        }
        - example error return object: {
            "status": "error",
            "message": "Channel stats not found.",
            "driver": driver
        }
        """
        channel_id_result = self.get_my_channel_id()
        if channel_id_result['status'] == 'success':
            result = youtube.get_channel_stats(channel_id_result['channel_id'])
            print(f"Channel stats: {result}")
            return result

@dataclass
class YoutubeData:
    def get_all_video_stats_from_channel(
        self,
        channel_handle: str,
    ):
        """
        Function to get all video stats and some extra information about the video, from a specific channel.

        Parameters:
        - channel_handle (str): channel handle of the channel to get all video stats from.

        Returns:
        - example success return object: {
            "all_video_stats": all_videos_with_stats,
            "status": "success",
            "message": "All video stats fetched successfully."
        }
        # Format of all_video_stats:
        [
            {
                "kind": "youtube#video",
                "etag": "eAGZdVWxoBjCKRPIjFKF64WuM7Q",
                "id": "0P1FGtdg8o8",
                "snippet": {
                    "publishedAt": "2024-04-03T17:00:02Z",
                    "channelId": "UCWsslCoN3b_wBaFVWK_ye_A",
                    "title": "What happened in Vegas",
                    "description": "Email list: https://hamza-ahmed.co.uk/UnfilteredWisdom\nThe only product I sell: https://www.skool.com/adonis\nInstagram: https://www.instagram.com/cultleaderhamza\nTwitter: https://twitter.com/HamzaAdonis",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        },
                        "standard": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/sddefault.jpg",
                            "width": 640,
                            "height": 480
                        },
                        "maxres": {
                            "url": "https://i.ytimg.com/vi/0P1FGtdg8o8/maxresdefault.jpg",
                            "width": 1280,
                            "height": 720
                        }
                    },
                    "channelTitle": "Hamza Ahmed",
                    "tags": [
                        "hamza ahmed",
                        "hamza",
                        "hamza97",
                        "self improvement",
                        "entrepreneur",
                        "entrepreneurship",
                        "beginners business",
                        "business",
                        "youtube subscribers",
                        "masculinity"
                    ],
                    "categoryId": "27",
                    "liveBroadcastContent": "none",
                    "defaultLanguage": "en-US",
                    "localized": {
                        "title": "What happened in Vegas",
                        "description": "Email list: https://hamza-ahmed.co.uk/UnfilteredWisdom\nThe only product I sell: https://www.skool.com/adonis\nInstagram: https://www.instagram.com/cultleaderhamza\nTwitter: https://twitter.com/HamzaAdonis"
                    },
                    "defaultAudioLanguage": "en-US"
                },
                "statistics": {
                    "viewCount": "31662",
                    "likeCount": "2255",
                    "favoriteCount": "0",
                    "commentCount": "582"
                }
            },
            ...
        ]
        - example error return object: {
            "status": "error",
            "message": "An error occurred. Please check errorr.txt for more details.",
            "error": str(e),
        }
        """
        result = youtube.get_all_video_stats_from_channel(channel_handle)
        return result

    def get_channel_id(
        self,
        channel_handle: str,
    ):
        """
        Function to get channel ID of the channel.

        Parameters:
        - channel_handle (str): channel handle of the channel to get channel ID from.

        Returns:
        - example success return object: {
            "status": "success",
            "channel_id": channel_id,
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while converting handle to channel id.",
            "error": str(e),
        }
        """
        result = youtube.get_channel_id(channel_handle)
        return result

    def get_video_stats(
        self,
        video_id: str,
    ):
        """
        Function to get individual video stats

        Parameters:
        - video_id (str): video id for the video you want to get stats for.

        Returns:
        - example success return object: {
            "video_stats": video_stats,
            "status": "success"
        }
        - example error return object: {
            "status": "error",
            "message": "Error getting video stats.",
            "error": str(e),
        }
        """
        result = youtube.get_video_stats(video_id)
        return result
    
    def get_channel_stats(
        self,
        channel_id: str,
    ):
        """
        Function to get channel stats of the channel.

        Parameters:
        - channel_id (str): channel id of the channel to get stats from.

        Returns:
        - example success return object: {
            "status": "success",
            "channel_stats": channel_stats
        }
        - example error return object: {
            "status": "error",
            "messsage": "Error getting channel stats.",
            "error": str(e),
        }
        """

        result = youtube.get_channel_stats(channel_id)
        return result

    def download_video(
        self,
        video_id: str,
        absolute_path: str,
        filename: str
    ):
        """
        Function to download video from youtube.
        Parameters:
        - video_id (str): video id of the video to download.
        - absolute_path(str): absolute path to where you want to save the downloaded video.
        - filename(str): filename of the downloaded video.
        Returns:
        - example success return object: {
            "status": "success",
            "message": "Video downloaded successfully.",
        }
        - example error return object: {
            "status": "error",
            "message": "Error downloading video.",
            "error": str(e),
        }
        """
        result = youtube.download_video(video_id, absolute_path, filename)
        return result
    
    def download_thumbnail(
        self,
        video_id: str, 
        export_path: str, 
        thumbnail_name: str
    ):
        """
        Function to download thumbnail of a video from youtube, and save to specified absolute path.

        Parameters:
        - video_id (str): video id of the video to download thumbnail from.
        - export_path (str): absolute path to save the downloaded thumbnail.
        - thumbnail_name (str): name of the thumbnail to save as.

        Returns:
        - example success return object: {
            "status": "success",
            "message": "Thumbnail downloaded successfully.",
        }
        - example error return object: {
            "status": "error",
            "message": "Error downloading thumbnail.",
            "error": str(e),
        }
        """
        # # Download thumbnail and save to absolute path
        result = youtube.download_thumbnail(video_id, export_path, thumbnail_name)
        return result


