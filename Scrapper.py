#  SELENUIM IS A PYTHON API WHICH USES THE DRIVER TO INTERACT WITH THE WEB BROWSER

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


video_url = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  
  driver = webdriver.Chrome(options = chrome_options)

  return driver

def get_videos(driver):
  print(1)
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  print(2)
  driver.get(video_url)
  print(3)
  videos = driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)
  print(5)
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text

  return{
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel_name': channel_name,
    'description': description
  }

def send_email():
  pass

if __name__=="__main__":
  print("Creating driver")
  driver = get_driver()

  #This is the web browser tab the url is loaded & execute the javascript

  print("Fetching trending videos")
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

  print('Parsing top 10 videos')
  # title, url, thumbnail_url, channel, views, uploaded, discription
  videos_data =[parse_video(video) for video in videos[:10]]

  print(videos_data)
  # video = videos[0]
  

  # print('Title: ', title)
  # print('URL: ', url)
  # print('Thumbnail URL: ', thumbnail_url)
  # print('Channel Name: ', channel_name)
  # print('Description: ', description)

  print('Save the data in CSV')
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv', index=None)
  
  print("sending an email")
  send_email()
