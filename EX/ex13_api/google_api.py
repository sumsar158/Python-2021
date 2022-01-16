"""Google APui."""
from __future__ import print_function
import pickle
from googleapiclient.discovery import build
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# The ID and range of a sample spreadsheet.
id = '1PChepQDduHsZlbMXPuJmLm21wu1woagkQV6vssiLi74'
RANGE = 'A:A'

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

pik = []
creds = None
token = 'Sheet1!'

# The file token.pickle stores the user's access and refresh tokens, and is
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """Should get a list of strings from the first column of a Google Spreadsheet with the given ID."""
    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    token = str(token) + RANGE
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=token).execute()
    values = result.get('values', [])

    for items in values:
        for val in items:
            pik.append(str(val))

    print(pik)
    return pik


def get_links_from_playlist():
    """Should get a list of links to songs in the Youtube playlist with the given address."""
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId="PLBCF2DAC6FFB574DE"
    )
    response = request.execute()
    return response
