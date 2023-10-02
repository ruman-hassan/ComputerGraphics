import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set the path to your credentials JSON file
credentials_file = 'credentials.json'

# Set the path to the folder you want to upload
folder_path = 'output_xlsx'

# Authenticate with Google Drive using the credentials
creds = None
if os.path.exists(credentials_file):
    creds = service_account.Credentials.from_service_account_file(
        filename=credentials_file,
        scopes=['https://www.googleapis.com/auth/drive']
    )

# Create a Google Drive API service instance
drive_service = build('drive', 'v3', credentials=creds)

# Define the folder name and create the folder
folder_name = 'computergraphics'
folder_metadata = {
    'name': folder_name,
    'mimeType': 'application/vnd.google-apps.folder'
}
created_folder = drive_service.files().create(
    body=folder_metadata,
    fields='id'
).execute()

# Get the ID of the created folder
folder_id = created_folder.get('id')

# Iterate through the files in the folder and upload each one
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, resumable=True)
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print(f'File ID: {file.get("id")} - File uploaded successfully: {filename}')

print(f'Folder ID: {folder_id} - Folder uploaded successfully to {folder_name}!')
