import pickle
import os
import base64
import random

import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


# Get the path to the pickle file


# Create a message
def send_email(user, my_email, my_subject, msgPlain, url):
    # home_dir = os.path.expanduser('~')
    # pickle_path = os.path.join(home_dir, 'gmail.pickle')
    pickle_path = 'gmail.pickle'
    # Load our pickled credentials
    creds = pickle.load(open(pickle_path, 'rb'))
    # Build the service
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

    with open('static/database.json', 'r+') as f:
        data = json.load(f)
        email_id = random.randint(1, 9999999999)
        if user in data.keys():
            data[user].append(
                {"id": email_id, "email": my_email, "subject": my_subject, "content": msgPlain,
                 "opened": False, "reply": False, "clickthrough": False})
        else:
            data[user] = [
                {"id": email_id, "email": my_email, "subject": my_subject, "content": msgPlain,
                 "opened": False, "reply": False, "clickthrough": False}]

        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part
    html = """\
    <html>
      <head></head>
      <body>
        <p>""" + msgPlain + """
        </p>
        <img src='""" + url+"/image/" + str(email_id) + """' width="500" height="600">
      </body>
    </html>
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = my_subject
    msg['From'] = f'{my_email}'
    msg['To'] = f'{my_email}'

    # msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    message1 = body
    message = (
        service.users().messages().send(
            userId="me", body=message1).execute())


if __name__ == "__main__":
    send_email("edwin.s.hou@gmail.com", "edwin.s.hou@gmail.com", "testing", "testing")
