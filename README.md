# youtube_selenium_py

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/) [![PyPI Version](https://img.shields.io/pypi/v/youtube_selenium_py.svg)](https://discord.gg/hBufFtWQmy) ![Discord](https://img.shields.io/discord/1225776155626307594)

**youtube_selenium_py** is a Python package that simplifies interactions with YouTube using Selenium.

(Video iframe, title: "Youtube Selenium Py | Automate Youtube with Selenium and Python)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Examples](#examples)
6. [Documentation](#documentation)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

This package provides functionalities to perform various actions on YouTube, such as creating channels, uploading videos, managing community posts, retrieving channel statistics, and more. It mostly uses Selenium to automate interactions with the YouTube platform. The package has two main classes at this moment, the `Youtube` class, and the `YoutubeData` class. The `Youtube` class is used for creating and getting information for the specific YouTube channel that is signed in, and the `YoutubeData` class is used to get some basic information from a YouTube channel and YouTube videos.

---

## Installation

1. **Install package via pip:**

   ```bash
   pip install youtube_selenium_py
   ```

2. **Upgrade setuptools (required for undetected chromedriver to work):**

   ```bash
   pip install --upgrade setuptools
   ```

3. **Make sure you have Chromium browser installed on your operating system:**

   ### Windows:

   - [Download Chromium](https://www.chromium.org/getting-involved/download-chromium/)

   ### macOS:

   ```bash
   brew install chromium
   ```

   ### Linux:

   #### Debian/Ubuntu-based:

   ```bash
   sudo apt update
   sudo apt install chromium-browser
   ```

   #### Arch Linux:

   ```bash
   sudo pacman -S chromium
   ```

---

## Usage

After installation, import the package and utilize its classes and methods. Detailed usage instructions and examples are provided in the [documentation](https://docs.agnostica.site).

Here is a quick video I recorded, of me going through the source code of the package, explaining each method, and also testing out the package:

(youtube video href)

---

## Features

- Create and edit YouTube channels
- Upload videos to channels
- Manage community posts
- Retrieve channel and video statistics
- Delete channels and sub-channels
- Download videos and thumbnails
- And more (read documentation)

---

## Examples

```python
from youtube_selenium_py.classes import Youtube

# Initialize the Youtube object
yt = Youtube(email="your_email@example.com", password="your_password")

# There is a 20 second implicit sleep after signing in, because maybe you have 2 step authentication enabled, or it will send confirmation code to your phone. We suggest using a brand new google account, then this won't happen, everything will be automatic.

# Example: Create a channel
channel_creation_result = yt.create_channel()
print(channel_creation_result)

# Example: Upload a video
video_upload_result = yt.create_video(
    absolute_video_path="/path/to/video.mp4",
    video_title="My Video Title",
    video_description="Description of my video"
)
print(video_upload_result)

# Close the driver when done
yt.close()
```

---

## Documentation

Refer to the provided documentation for detailed usage instructions, method descriptions, and return formats.

---

## Contributing

Contributions are welcome! Please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## License

This project is licensed under the [MIT License](LICENSE).
