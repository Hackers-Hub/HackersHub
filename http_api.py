__author__ = 'Samuel Marks <samuelmarks@gmail.com>'
__version__ = '0.1.0'

try:
    from urllib.parse import urlparse
except ImportError:
    from urllib.parse import urlparse

from socketserver import ThreadingTCPServer
from http.server import SimpleHTTPRequestHandler

from webbrowser import open_new_tab
from json import dumps
from os import environ


from linkedin.linkedin import LinkedInAuthentication, LinkedInApplication, PERMISSIONS

PORT = 8080

def get_environ(name):
    if name not in environ:
        raise KeyError(f"Environment variable {name} is not set")
    return environ.get(name)

class LinkedInWrapper(object):
    """ Simple namespacing """
    API_KEY = get_environ('LINKEDIN_API_KEY')
    API_SECRET = get_environ('LINKEDIN_API_SECRET')
    RETURN_URL = f'http://localhost:{PORT}/code'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, list(PERMISSIONS.enums.values()))
    application = LinkedInApplication(authentication)


liw = LinkedInWrapper()
run_already = False
params_to_d = lambda params: {
    l[0]: l[1] for l in [j.split('=') for j in urlparse(params).query.split('&')]
}


class CustomHandler(SimpleHTTPRequestHandler):
    def json_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        global run_already
        parsedurl = urlparse(self.path)
        authed = liw.authentication.token is not None

        if parsedurl.path == '/code':
            self.json_headers()

            liw.authentication.authorization_code = params_to_d(self.path).get('code')
            self.wfile.write(dumps({'access_token': liw.authentication.get_access_token(),
                                    'routes': list([d for d in dir(liw.application) if not d.startswith('_')])}).encode('utf8'))
        elif parsedurl.path == '/routes':
            self.json_headers()

            self.wfile.write(dumps({'routes': list([d for d in dir(liw.application) if not d.startswith('_')])}).encode('utf8'))
        elif not authed:
            self.json_headers()

            if not run_already:
                open_new_tab(liw.authentication.authorization_url)
            run_already = True
            self.wfile.write(dumps({'path': self.path, 'authed': type(liw.authentication.token) is None}).encode('utf8'))
        elif authed and len(parsedurl.path) and parsedurl.path[1:] in dir(liw.application):
            self.json_headers()
            self.wfile.write(dumps(getattr(liw.application, parsedurl.path[1:])()).encode('utf8'))
        else:
            self.json_headers(501)
            self.wfile.write(dumps({'error': 'NotImplemented'}).encode('utf8'))


if __name__ == '__main__':
    httpd = ThreadingTCPServer(('localhost', PORT), CustomHandler)

    print(f'Server started on port:{PORT}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
