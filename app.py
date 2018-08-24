from bottle import route, get, post, error, template, run, request, static_file
import helper as hlp


@route('/')
def index():
	return template('index')


@get('/search')
def search():
	keyword = request.query['keyword']
	my_url = hlp.key['base'] + keyword
	# return template('results', data=hlp.parseBooks(my_url))
	return hlp.parseBooks(my_url)

@get('/download')
def download():
	keyword = request.query['md5']


# Access static files
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080, debug=True, reloader=True)