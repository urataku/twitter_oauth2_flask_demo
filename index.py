import os
from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, request, session
from services.twitter.api import TwitterApi
from services.twitter.auth import TwitterOauth
from services.twitter.me_fetcher import MeFetcher
from services.token_code_manager import TokenCodeManager

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token:
        api = TwitterApi(access_token)
        me_fetcher = MeFetcher(api)
        response = me_fetcher.exec()
        return render_template('home.html', content=response)
    oauth = TwitterOauth()
    TokenCodeManager.create_code(session)
    token_code = TokenCodeManager.fetch_code(session)
    login_url = oauth.get_url(token_code)
    return redirect(login_url)

@app.route('/callback', methods=['GET'])
def callback():
    args = request.args
    if not 'code' in args:
        return

    code = args.get('code')
    oauth = TwitterOauth()
    code_verifier = TokenCodeManager.fetch_code(session)
    auth = oauth.fetch_token(code, code_verifier)
    session['access_token'] = auth['access_token']
    return redirect(url_for('index'))
