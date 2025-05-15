from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

SCOPES = ['https://www.googleapis.com/auth/drive.file']

class DriveService:
    @staticmethod
    def get_credentials():
        flow = InstalledAppFlow.from_client_secrets_file(
            'resources/credentials.json', SCOPES)
        return flow.run_local_server(port=8888)

    @staticmethod
    def upload_file(file_path, mime_type, drive_name):
        creds = DriveService.get_credentials()
        service = build('drive', 'v3', credentials=creds)
        
        file_metadata = {'name': drive_name}
        media = MediaFileUpload(file_path, mimetype=mime_type)
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id,name'
        ).execute()
        
        return file