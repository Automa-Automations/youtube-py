from typing import Optional
import youtube 
from utils import sign_into_youtube_channel, new_driver

class Youtube:
    def __init__(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        absolute_chromium_profile_path: Optional[str] = None,
        cookies: Optional[list] = None,
    ):
        # if none is specified, throw error 
        if email is None and password is None and absolute_chromium_profile_path is None and cookies is None:
            raise Exception("Please provide either email and password or cookies or chromium profile path.")
        
        self.driver = new_driver() 
        self.email = email
        self.password = password
        self.absolute_chromium_profile_path = absolute_chromium_profile_path
        self.cookies = cookies
        
        self.sign_in()

    def sign_in(self):
        driver = sign_into_youtube_channel(self.driver, self.email, self.password, self.cookies, self.absolute_chromium_profile_path)
        # Set class driver to driver
        self.driver = driver

    
    def create_channel(
        self, 
        channel_name: str,
        channel_handle: str,
        channel_description: str,
        profile_picture_path: str,
        banner_picture_path: str,
        watermark_picture_path: str,
        contact_email_path: str,
        links: list,
    ):
        """
        Function to create a Youtube channel. 

        Parameters:
        channel_name (str): name of the channel.
        channel_handle (str): channel handle/username.
        channel_description (str): description of the channel.
        profile_picture_path (str): path of the profile picture of the channel.
        banner_picture_path (str): path of the banner picture of the channel.
        watermark_picture_path (str): path of the watermark picture of the channel.
        contact_email_path (str): path of the contact email of the channel.
        links (list): list of links to be added to the channel.
        
        Returns:
        - example success return object: {
            "status": "success",
            "channel_id": channel_id, 
            "message": "Channel created successfully", 
            "cookies": driver.get_cookies()
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while creating channel."
            "error": error_message
        }
        """
        result = youtube.create_channel(
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
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while uploading video.",
            "error": error_message
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
        }
        - example error return object: {
            "status": "error",
            "message": "An error occurred while creating community post."
            "error": error_message
        }
        """
        result = youtube.create_community_post(
            self.driver,
            community_post_title,
            schedule,
        )
        self.driver = result['driver'] 

    def delete_channel(
        self,
        email: str,
    ):
        result = youtube.delete_channel(self.driver, email)
        self.driver = result['driver']

    def close(self):
        if self.driver:
            self.driver.quit()
        else:
            raise Exception("Driver not found")
