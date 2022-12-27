import json
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, session, url_for

import settings

application = app = Flask('app')
app.secret_key = settings.APP_SECRET_KEY

oauth = OAuth(app)

oauth.register(
  "auth0",
  client_id=settings.AUTH0_CLIENT_ID,
  client_secret=settings.AUTH0_CLIENT_SECRET,
  client_kwargs={
    "scope": "openid profile email",
  },
  server_metadata_url=
  f'https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration')


@app.route('/')
def hello_world():
  username = session.get('user', {}).get('userinfo', {}).get('name')
  if username:
    return f'Hello, {username}!'
  return 'Hello, world!'


@app.route("/login")
def login():
  print(url_for("callback", _external=True))
  return oauth.auth0.authorize_redirect(
    redirect_uri=url_for("callback", _external=True))


@app.route("/callback", methods=["GET", "POST"])
def callback():
  token = oauth.auth0.authorize_access_token()
  session["user"] = token
  print(token)
  return redirect("/")


@app.route("/logout")
def logout():
  session.clear()
  return redirect("https://" + settings.AUTH0_DOMAIN + "/v2/logout?" +
                  urlencode(
                    {
                      "returnTo": url_for("home", _external=True),
                      "client_id": settings.AUTH0_CLIENT_ID,
                    },
                    quote_via=quote_plus,
                  ))


@app.route('/athletes', methods=['GET'])
def athletes():
  pass


@app.route('/meets', methods=['GET'])
def meets():
  pass


@app.route('/teams', methods=['GET'])
def teams():
  pass


@app.route('/seasons', methods=['GET'])
def seasons():
  pass


@app.route('/results', methods=['GET'])
def results():
  pass


@app.route('/athlete', methods=['GET', 'POST', 'DELETE'])
def athlete():
  pass


@app.route('/meet', methods=['GET', 'POST', 'DELETE'])
def meet():
  pass


@app.route('/team', methods=['GET', 'POST', 'DELETE'])
def team():
  pass


@app.route('/season', methods=['GET', 'POST', 'DELETE'])
def season():
  pass


@app.route('/result', methods=['GET', 'POST', 'DELETE'])
def result():
  pass


app.run(host='0.0.0.0', port=5000)
