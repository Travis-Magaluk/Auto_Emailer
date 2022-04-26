import os
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = [ 'https://www.googleapis.com/auth/spreadsheets' ]

sercice = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
