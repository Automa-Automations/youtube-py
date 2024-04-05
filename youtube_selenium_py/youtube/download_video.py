from pytube import YouTube

def download_video(video_id: str, absolute_path :str, filename: str):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(url)
       
        # Filter streams to get those with video and audio, sorted by resolution
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        
        # Find the highest resolution stream that is less than or equal to 1080p
        stream = None
        for s in streams:
            if s.resolution and int(s.resolution.split('p')[0]) <= 1080:
                stream = s
                break
        
        if stream:
            # Download the video with the specified filename
            stream.download(output_path=absolute_path, filename=filename)
            print("Download completed successfully.")
            return {
                "status": "success",
                "message": "Video downloaded successfully.",
            }
        else:
            print("No suitable streams found.")
            return {
                "status": "error",
                "message": "No suitable streams found.",
                "error:": "No suitable streams found.",
            }
    except Exception as e:
        print("An error occurred while downloading the video.")

        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": "Error downloading video.",
            "error": str(e),
        }
