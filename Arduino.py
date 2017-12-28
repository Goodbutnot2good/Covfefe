from __future__ import print_function
from apiclient import discovery
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import apiclient.discovery
import os
import io


file_id = '1TqWj5M-2m-S6l1mixHLtgiNy_tc4qURlVSg7m4w25Ug'
API_KEY = 'AIzaSyCk26Q0nYfODWVkiwiJM1NfoNpr8OKH9Mk'


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
drive_service = build('drive', 'v2', http=creds.authorize(Http()))

file_id = '1TqWj5M-2m-S6l1mixHLtgiNy_tc4qURlVSg7m4w25Ug'
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print ("Download %d%%." % int(status.progress() * 100))