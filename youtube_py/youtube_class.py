from typing import Optional
import youtube 
from dataclasses import dataclass

@dataclass
class YoutubeClass:
    
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
        youtube.create_channel(
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
    def create_video(
        self,
        absolute_video_path: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
        cookies: Optional[str] = None,
        absolute_chromium_profile_path: Optional[str] = None,
    ):
        youtube.create_video(
            absolute_video_path,
            email,
            password,
            cookies,
            absolute_chromium_profile_path,
        )
