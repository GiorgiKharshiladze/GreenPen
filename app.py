from bs4 import BeautifulSoup
import pandas as pd
import json, requests, datetime

base = 'http://libgen.io/search.php?&phrase=1&open=0&res=100&view=simple&req='

def getHTML(url):
	response = requests.get(url)
	source = response.content
	return source

def getContent(url):
	html = getHTML(url)
	soup = BeautifulSoup(html, 'html5lib')
	return soup

def getInfo(url):
	content = getContent(url)
	tables = content.findAll('table')
	return tables

def getBooks(url):
	library = getInfo(url)[2]
	books = library.findAll('tr')[1:]
	return books

def parseBooks(books):
	columns = ['author', 'title', 'publisher', 'year', 'pages', 'lang', 'size', 'extension']
	df = pd.DataFrame(columns=columns)

	for book in books:
		bookInfo = book.findAll('td')
		id = bookInfo[0].text
		author = bookInfo[1].text
		title = bookInfo[2].text
		publisher = bookInfo[3].text
		year = bookInfo[4].text
		pages = bookInfo[5].text
		lang = bookInfo[6].text
		size = bookInfo[7].text
		extension = bookInfo[8].text
		mirrors = bookInfo[9:]
		row = {'author':author, 'title':title, 'publisher':publisher, 'year':year, 'pages':pages, 'lang':lang, 'size':size, 'extension':extension}
		df = df.append(row, ignore_index=True)

	return df


keyword = "harry potter"
keyword_slug = keyword.replace(" ","+")
my_url = base + keyword_slug

print(parseBooks(getBooks(my_url)))