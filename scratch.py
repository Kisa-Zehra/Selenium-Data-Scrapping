import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'

# does not used javascript
response = requests.get(url)
print('Status', response)

#print('Output', response.text)

with open('scrapfile.html', 'w') as f:
  f.write(response.text)


doc = BeautifulSoup(response.text, 'html.parser')

print('Page title: ', doc.title.text)

#find all the video divs
video_divs = doc.find_all('div', class_='ytd-video-render')
print(f'Found {len(video_divs)} videos')