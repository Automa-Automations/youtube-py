from utils import sign_into_youtube_channel
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import find_element, scroll_to_bottom, sign_into_youtube_channel, set_element_innertext
import time

print("1. Instantiating driver...")
options = uc.ChromeOptions()
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-popup-blocking")  # Disable popup blocking
driver = uc.Chrome(options=options)

