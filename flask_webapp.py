from flask_socketio import SocketIO, emit
from flask import Flask, render_template, jsonify, request, send_file
from send_email import send_email
from authenticate import authenticate
from copy_ai import generate_copies
import json
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

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


@socketio.on('login')
def handle():
    auth = authenticate()
    auth_url = next(auth)
    emit("login_url", auth_url)
    print(next(auth))
    # response = ""
    # response = jsonify({'source_url': source_url, "author": author, "source": source, "date": date, "credibility": credibility})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # print(source_url)


@socketio.on('get_data')
def handle(user):
    print('getting data')
    # emit("data", "aaaa")
    with open('./static/database.json', 'r') as f:
        data = json.load(f)
        emit("data", data[user])


@socketio.on('mail')
def handle(stuff):
    copies = generate_copies(stuff['subject'])
    copies.append(stuff['subject'])
    print(copies)
    mailing_list = stuff['mailing_list'].split(',')
    i = 0
    for email in mailing_list:
        print("LETSGOOO we just emailed: " + email)
        send_email("edwin.s.hou@gmail.com", email, copies[i % 4], stuff['content'], stuff['url'])
        i += 1


if __name__ == "__main__":
    socketio.run(app, port = 80, debug=True, log_output=True)
