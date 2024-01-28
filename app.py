from flask import Flask, redirect, request, session, url_for
import os
import requests
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

# Use environment variables for LinkedIn client ID and client secret
CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")

LINKEDIN_AUTHORIZATION_URL = 'https://www.linkedin.com/oauth/v2/authorization'
LINKEDIN_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_USERINFO_URL = 'https://api.linkedin.com/v2/userinfo'

@app.route('/')
def home():
    return 'Welcome! <a href="/login">Login with LinkedIn</a>'

@app.route('/login')
def login():
    # Generate a unique session state value
    state = uuid.uuid4().hex
    session['state'] = state

    # Parameters for LinkedIn authorization URL
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': url_for('auth', _external=True),
        'state': state,
        'scope': 'openid profile email'
    }
    # Redirect user to LinkedIn for authorization
    return redirect(f"{LINKEDIN_AUTHORIZATION_URL}?{requests.compat.urlencode(params)}")

@app.route('/auth')
def auth():
    # Validate state value
    if request.args.get('state') != session['state']:
        return 'State value mismatch', 401

    # Exchange authorization code for access token
    code = request.args.get('code')
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': url_for('auth', _external=True)
    }
    token_response = requests.post(LINKEDIN_TOKEN_URL, data=data).json()
    access_token = token_response['access_token']

    # Retrieve user info
    user_info = requests.get(
        LINKEDIN_USERINFO_URL,
        headers={'Authorization': f'Bearer {access_token}'}
    ).json()

    # You can now use the user_info for your application purposes
    return f"User Info: {user_info}"

if __name__ == '__main__':
    app.run(debug=True, port=8080)

