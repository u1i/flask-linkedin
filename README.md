# flask-linkedin

### Simple Python Flask application that uses LinkedIn login


#### 1 – Create up LinkedIn app

Use [LinkedIn developer](https://www.linkedin.com/developers) to:

* create your new app
* activate the "Sign in with LinkedIn using OpenID Connect" product for the app
* get client ID and secret
* add http://127.0.0.1:8080/auth as authorized redirect URL

#### 2 - Set environment variables

Create a new Python 3 environment (I used 3.11.1) and install requirements:

* pip install -r requirements.txt

#### 3 - Set environment variables

export LINKEDIN_CLIENT_ID="XXXXXXX"
export LINKEDIN_CLIENT_SECRET="XXXXXXXXX"

#### 4 - Run the app

python3 app.py

#### 5 - Use the app in the browser

http://127.0.0.1:8080

`User Info: {'sub': 'ZwaXebY24_', 'email_verified': True, 'name': 'John Doe', 'locale': {'country': 'US', 'language': 'en'}, 'given_name': 'John', 'family_name': 'Doe', 'email': 'jd@gmail.com', 'picture': 'https://media.licdn.com/dms/image/D5603331EhM-QA6w/profile-displayphoto-shrink_100_100/0/1676627944871?e=1712188800&v=beta&t=W1dXTODZR7StPHzTQsxz7MaE_-Uq0tzf-qSwahyOz3s'}`
