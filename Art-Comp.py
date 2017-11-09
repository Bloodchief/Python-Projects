# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import search_google.api


#Defines link to grab data from
link = "http://thehill.com/policy/technology/359474-justice-att-trade-accusations-over-cnn-sale"
r = requests.get(link)

#Assigns page to 'data'
data = r.text

#soups the entire webpage
soup = (BeautifulSoup(data, "lxml"))

#sets <p> wrapped data to variable paragraphs
paragraphs = str((soup.find_all('p')))

#Stores the title of the article for searching
aTitle = soup.title.string

#bullshit that doesn't seem to narrow sites down, instead it just gives like 30 thehill.com links
#+ "sites: www.foxnews.com, www.cnn.com, abcnews.go.com, www.yahoo.com/news, www.thehill.com, www.huffingtonpost.com"

print(aTitle)

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