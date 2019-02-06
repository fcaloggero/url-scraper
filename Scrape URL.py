# -*- coding: utf-8 -*-
import json ##import all code from the Python standard library called json
from urllib.request import urlopen ##import only the urlopen function from the standard urllib library
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" ##assign a YouTube URL to the variable url
response = urlopen(url) ##connect to the web server at that URL and request a particular web service
contents = response.read() ##get the response data and assign to the variable contents
text = contents.decode('utf8') ##decode contents to a text string in JSON format, and assign to the variable text
data = json.loads(text) ##convert text to data—Python data structures about videos
for video in data['feed']['entry'][0:6]: ##get the information about one video at a time into the variable video, use a two-level Python dictionary (data['feed']['entry']) and a slice ([0:6])
    print(video['title']['$t']) ##use the print function to print only the title of the video
    
##Or, a shorter, externally authored code
import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])