from bs4 import BeautifulSoup
import json, requests, datetime

base = 'http://libgen.io/search.php?&phrase=1&view=simple&req='

def getHTML(url):
	response = requests.get(url)
	source = response.content
	return source

def getContent(url):
	html = getHTML(url)
	soup = BeautifulSoup(html, 'html5lib')
	return soup

keyword = "harry potter"
keyword_slug = keyword.replace(" ","+")
my_url = base + keyword_slug

# print(getContent(my_url))