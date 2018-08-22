from bottle import route, get, post, error, template, run, request, static_file
import json, helper as hlp


key = json.load(open('keys.json', 'r'))

@route('/')
def index():
	return template('index')


@post('/search')
def search():
	keyword = request.forms.get('keyword')
	keyword_slug = keyword.replace(" ","+")
	my_url = key['base'] + keyword_slug
	# return template('results', data=hlp.parseBooks(my_url))
	return hlp.parseBooks(my_url)


# Access static files
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080, debug=True, reloader=True)