import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_FILE = "user.json"
SCOPES = ["https://www.googleapis.com/calendar/v3"]

creds = None

if os.path.exists("token.json"):
    credit = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
    if creds and  creds.expired and cred.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    with.open
