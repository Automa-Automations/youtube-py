from youtube_selenium_py.youtube.list_all_channels import list_all_channels

def get_my_channel_handle(driver):
    try:
        result = list_all_channels(driver)
        if result["status"] == "success":
            channel_handle = result["channels_list"][0]['channel_handle']
        else:
            raise Exception("Error: channel listing not successful.")
        
        print(f"My Channel Handle: {channel_handle}")
        return {
            "status": "success",
            "message": "Channel ID found.",
            "channel_handle": channel_handle,
            "driver": driver
        }
    except Exception as e:
        print("Error: " + str(e))

        with open("error.txt", "a") as error_file:
            error_file.write(str(e) + "\n")

        return {
            "status": "error",
            "message": "Channel ID not found.",
            "driver": driver
        }
