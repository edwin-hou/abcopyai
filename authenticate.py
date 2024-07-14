import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Specify permissions to send and read/write messages
# Find more information at:
# https://developers.google.com/gmail/api/auth/scopes
def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.modify']


    home_dir = os.path.expanduser('~')

    json_path = "credentials.json"

    flow = InstalledAppFlow.from_client_secrets_file(json_path, SCOPES)
    print("a")
    creds = flow.run_local_server(port=0, open_browser=False)
    yield next(creds)
    pickle_path = os.path.join(home_dir, 'gmail.pickle')
    with open(pickle_path, 'wb') as token:
        pickle.dump(next(creds), token)
    yield "complete"
if __name__ == "__main__":
    authenticate()