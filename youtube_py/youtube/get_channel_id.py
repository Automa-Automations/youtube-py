import requests

def get_channel_id(channel_handle: str):
    try:
        print(f"Converting handle '{channel_handle}' to channel id...")
        channel_handle = channel_handle.replace("@", "")
        request_url = f"https://yt.lemnoslife.com/channels?handle=@{channel_handle}"
        response = requests.get(request_url)
        channel_id = response.json()['items'][0]['id']
        
        print(f"Successfully converted handle '{channel_handle}' to channel id: {channel_id}.")

        return {
            "status": "success",
            "channel_id": channel_id,
        }

    except Exception as e:
        print(f"Error while converting handle '{channel_handle}' to channel id.")
        with open("error.txt", "w") as f:
            f.write(str(e))

        return {
            "status": "error",
            "message": "An error occurred while converting handle to channel id.",
            "error": str(e),
        }
