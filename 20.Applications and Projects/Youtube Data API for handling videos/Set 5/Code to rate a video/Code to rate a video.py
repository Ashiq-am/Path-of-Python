import argparse
import os
import re
import urllib.request
import urllib.error
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)

    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION,
                 credentials=credentials)


def like_video(youtube):
    youtube.videos().rate(id='ZmtLzRJh8n8',
                          rating='like').execute()


# Driver Code
if __name__ == '__main__':

    youtube = get_authenticated_service()

    try:
        like_video(youtube)
    except urllib.error.HttpError as e:
        print('An HTTP error %d occurred:\n % s'
              % (e.resp.status, e.content))
    else:
        print('The rating has been added')
