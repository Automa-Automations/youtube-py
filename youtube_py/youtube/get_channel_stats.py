import requests
        
def get_channel_stats(channel_id: str):
    print("Getting channel stats...")
    try:
        url = f"https://yt.lemnoslife.com/noKey/channels?id={channel_id}&part=snippet,statistics"
        response = requests.get(url)
        channel_stats = response.json()['items'][0]
            
        print("Successfully got channel stats.")
        return {
            "status": "success",
            "channel_stats": channel_stats
        }

    except Exception as e:
        print("Error getting channel stats...")

        with open("error.txt", "w") as f:
            f.write(f"Error getting channel stats: {str(e)}\n")

        return {
            "status": "error",
            "messsage": "Error getting channel stats.",
            "error": str(e),
        }

