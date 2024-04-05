import requests
from youtube_selenium_py.youtube import get_video_stats

def download_thumbnail(video_id, export_path, thumbnail_name):
    try:
        result = get_video_stats(video_id)
        if result["status"] == "success":
            video_data = result["video_stats"]
        else:
            print("Error: Unable to fetch video data.")
            return result 

        snippet = video_data["snippet"]
        thumbnail_url = snippet["thumbnails"]["maxres"]["url"]

        response = requests.get(thumbnail_url)
        with open(f"{export_path}/{thumbnail_name}.jpg", 'wb') as file:
            file.write(response.content)
        print(f"Thumbnail '{thumbnail_name}.jpg' downloaded at {export_path}")

        return {
            "status": "success",
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
