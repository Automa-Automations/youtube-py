from typing import Optional
import channel

class YoutubeClass:
    def __init__(
        self,
        channel_cookies: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        chrome_driver_path: Optional[str] = None,
    ):
        self.channel_cookies = channel_cookies
        self.email = email
        self.password = password
        self.chrome_driver_path = chrome_driver_path
    
    def create_channel(
        self, 
        channel_name: str,
        channel_handle: str,
        channel_description: str,
        email: str,
        password: str,
        profile_picture_path: str,
        banner_picture_path: str,
        watermark_picture_path: str,
        contact_email_path: str,
        links: list,
    ):
        channel.create_channel(
            channel_name,
            channel_handle,
            channel_description,
            email,
            password,
            profile_picture_path,
            banner_picture_path,
            watermark_picture_path,
            contact_email_path,
            links
        )
