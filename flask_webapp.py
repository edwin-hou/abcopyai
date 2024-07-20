from flask_socketio import SocketIO, emit
from flask import Flask, render_template, jsonify, request, send_file
from send_email import send_email
from authenticate import authenticate
from copy_ai import generate_copies
import json
import google_auth_oauthlib
import flask
import os
import pickle
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = 'superfi secret key'

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@app.route('/mailer')
def mailer():
    return render_template('mailer.html')


@app.route('/dashboard')
def dashboard():
    print('dashboard loaded')
    return render_template('dashboard.html')


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/email_open', methods=['POST', 'GET'])
def email_open():
    data = eval(list(request.form)[0])
    print(eval(list(request.form)[0])['ip'])
    return "aa"


@app.route('/image/<path:id>')
def spy_pixel(id):
    with open('static/database.json', 'r+') as f:
        data = json.load(f)
        for user in data.keys():
            for email in data[user]:
                if email["id"] == int(id):
                    email["opened"] = True

        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part

    return send_file("static/spy.gif", mimetype="image/png")

SCOPES = ['https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.modify']

@app.route('/authorize')
def authorize():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow
    # steps.

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "credentials.json", scopes=SCOPES)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True, code="4/0AcvDMrBRScxC--tBzsMjH8YYvx2KC_E6RXvPDUCH8J4jchTWHvuCOc0857um6q9D9XQsrA")
    #"4/0AcvDMrBRScxC--tBzsMjH8YYvx2KC_E6RXvPDUCH8J4jchTWHvuCOc0857um6q9D9XQsrA"
    authorization_url, state = flow.authorization_url(
        # This parameter enables offline access which gives your application
        # both an access and refresh token.
        access_type='offline',
        # This parameter enables incremental auth.
        include_granted_scopes='true')

    # Store the state in the session so that the callback can verify that
    # the authorization server response.
    print(state)
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    home_dir = os.path.expanduser('~')
    # Specify the state when creating the flow in the callback so that it can
    # verify the authorization server response.
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "credentials.json", scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True, code="4/0AcvDMrBRScxC--tBzsMjH8YYvx2KC_E6RXvPDUCH8J4jchTWHvuCOc0857um6q9D9XQsrA")

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    pickle_path = os.path.join(home_dir, 'gmail.pickle')
    print(credentials)
    print('==================')
    with open(pickle_path, 'wb') as token:
        pickle.dump(credentials, token)
    # flask.session['credentials'] = {
    #     'token': credentials.token,
    #     'refresh_token': credentials.refresh_token,
    #     'token_uri': credentials.token_uri,
    #     'client_id': credentials.client_id,
    #     'client_secret': credentials.client_secret,
    #     'scopes': credentials.scopes
    # }
    return flask.redirect("http://54.172.23.104/")


# @socketio.on('login')
# def handle():
#     auth = authenticate()
#     auth_url = next(auth)
#     print('aaaaa')
#     emit("login_url", auth_url)
#     # print(next(auth))
#     # response = ""
#     # response = jsonify({'source_url': source_url, "author": author, "source": source, "date": date, "credibility": credibility})
#     # response.headers.add('Access-Control-Allow-Origin', '*')
#     # print(source_url)


@socketio.on('get_data')
def handle(user):
    print('getting data')
    # emit("data", "aaaa")
    with open('static/database.json', 'r') as f:
        data = json.load(f)
        emit("data", data[user])


@socketio.on('mail')
def handle(stuff):
    # copies = generate_copies(stuff['subject'])
    copies = [stuff['subject']]
    copies.append(stuff['subject'])
    print(copies)
    print(stuff["url"])
    mailing_list = stuff['mailing_list'].split(',')
    i = 0
    for email in mailing_list:

        send_email("edwin.s.hou@gmail.com", email, copies[i % 4], stuff['content'], stuff['url'])
        print("LETSGOOO we just emailed: " + email)
        i += 1


if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    pickle_path = os.path.join(home_dir, 'gmail.pickle')
    print(pickle_path)
    socketio.run(app, port=8000, debug=True, log_output=True, allow_unsafe_werkzeug=True)
