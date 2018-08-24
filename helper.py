from bs4 import BeautifulSoup
import requests, datetime, json

key = json.load(open('keys.json', 'r'))

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

def parseBooks(url):
	books = getBooks(url)
	data = {}

	for i in range(len(books)):
		bookInfo = books[i].findAll('td')
		id = bookInfo[0].text
		author = bookInfo[1].text
		title = bookInfo[2].text
		publisher = bookInfo[3].text
		year = bookInfo[4].text
		pages = bookInfo[5].text
		lang = bookInfo[6].text
		size = bookInfo[7].text
		extension = bookInfo[8].text
		url = bookInfo[10].a['href'] # bookInfo[9:] are all the mirrors for book download
		row = {'author':author, 'title':title, 'publisher':publisher, 'year':year, 'pages':pages, 'lang':lang, 'size':size, 'extension':extension, 'url':url}
		data[i+1] = row

	return data

def getDownload(md5):
	url = key['download'] + md5
	content = getContent(url)
	link = content.table.tbody.tr.findAll('td')[2].a['href']
	return link