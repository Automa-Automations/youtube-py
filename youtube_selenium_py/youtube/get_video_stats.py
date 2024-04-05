from typing import Any, Dict
import requests

def get_video_stats(video_id: str):
    try:
        url=f"https://yt.lemnoslife.com/noKey/videos?part=snippet,statistics&id={video_id}"

        response = requests.get(url)
        response_json = response.json()
        video_stats : Dict[Any, Any] = response_json['items'][0]
        print("Successfully fetched video statistics.")

        return {
            "video_stats": video_stats,
            "status": "success"
        }

    except Exception as e:
        print(f"Error: {e}")

        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": "Error getting video stats.",
            "error": str(e),
        }
