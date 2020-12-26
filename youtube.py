from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

# Register the drive
chrome_browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=options)  # Change the path as per your local dir.
chrome_browser.get('https://www.youtube.com/')

content = chrome_browser.find_element_by_id("content")
videos = content.find_elements_by_id("style-scope ytd-rich-grid-renderer")

for video in videos:
    video_text = video.find_element_by_id("video-title-link")
    print(video_text.text)