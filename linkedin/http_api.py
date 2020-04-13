from os import environ
import requests
from flask import Flask, request

from linkedin.linkedin import LinkedInAuthentication, LinkedInApplication, PERMISSIONS

def get_environ(name):
    if name not in environ:
        raise KeyError(f"Environment variable {name} is not set")
    return environ.get(name)

PORT = get_environ("PORT")

class LinkedInWrapper(object):
    """ Simple namespacing """
    CLIENT_ID = get_environ('LINKEDIN_CLIENT_ID')
    CLIENT_SECRET = get_environ('LINKEDIN_CLIENT_SECRET')
    RETURN_URL = f'http://localhost:{PORT}/code'
    authentication = LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, RETURN_URL, ["r_liteprofile", "r_emailaddress"])
    application = LinkedInApplication(authentication)

liw = LinkedInWrapper()

app = Flask(__name__)
@app.route('/')
def root():
    authed = liw.authentication.token is not None
    return {'authed': type(liw.authentication.token) is None, 'auth_url': liw.authentication.authorization_url}

@app.route("/code")
@app.route("/auth")
def auth():
    liw.authentication.authorization_code = code = request.args.get('code')
    access_token = liw.authentication.get_access_token()
    routes = [d for d in dir(liw.application) if not d.startswith('_')]
    print(f"code {code}, access token: {access_token}")
    return {'access_token': access_token, 'routes': routes, 'profile': liw.application.get_profile()}
