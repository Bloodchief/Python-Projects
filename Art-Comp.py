# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import search_google.api


#Defines link to grab data from
link = "http://www.foxnews.com/politics/2017/11/06/democrat-walks-out-moment-silence-for-texas-massacre-victims.html"
r = requests.get(link)

#Assigns page to 'data'
data = r.text

#soups the entire webpage
soup = (BeautifulSoup(data, "lxml"))

#sets <p> wrapped data to variable paragraphs
paragraphs = str((soup.find_all('p')))

#Stores the title of the article for searching
aTitle = soup.title.string

try:
	from google import search
except ImportError:
	print("No google module")

#search google

query = aTitle


for i in search(query, tld="co.in", num=10, stop=1, pause=2):
	print(i)
	
#Writes paragraphs to file
#file=open("NewFile.txt", "w")
#file.write(paragraphs)
#file.close()


#keeps window open
input("Press enter to quit.")