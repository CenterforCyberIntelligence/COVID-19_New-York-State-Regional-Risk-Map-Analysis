import csv
import os
import pickle
import time

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def driveService():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(os.path.join('../helper_files/credentials.json')):
        with open(os.path.join('../helper_files/token.pickle'), 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join('../helper_files/credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join('../helper_files/token.pickle'), 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    return service


def drive_executeInitialFolderSetup():

    print("-" * 35)
    print("Initial Google Drive Setup Starting")
    print("-" * 35)
    print("[!] WARNING: Running this setup more than once will overwrite any existing file references on your Google Drive [!]\n")
    time.sleep(10)
    service = driveService()
    csv_data = []

    # Create a parent folder for all New York COVID-19 Analysis Projects
    parentFolder_metadata = {
        'name': 'New York COVID-19 Analysis Projects',
        'mimeType': 'application/vnd.google-apps.folder',
        'folderColorRgb': "#ff7537"
    }
    parentFolder = service.files().create(body=parentFolder_metadata, fields='id').execute()
    parentFolderID = parentFolder.get('id')
    csv_data.append(['0', 'Parent Folder', parentFolderID])
    print("[*] SUCCESS | Parent Folder Created --> Folder ID: %s" % parentFolderID)

    # Create a folder for the ICU Risk Analysis Project
    icuRiskAnalysisFolder_metadata = {
        'name': 'Regional ICU Risk Analysis',
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parentFolderID],
        'folderColorRgb': "ffad46"
    }
    icuRiskAnalysisFolder = service.files().create(body=icuRiskAnalysisFolder_metadata, fields='id').execute()
    icuRiskAnalysisFolderID = icuRiskAnalysisFolder.get('id')
    csv_data.append(['1', 'ICU Risk Analysis Folder', icuRiskAnalysisFolderID])
    print("[*] SUCCESS | ICU Risk Analysis Project Folder Created --> Folder ID: %s" % icuRiskAnalysisFolderID)

    # Create a folder for the ICU Risk Analysis Images
    icuRiskAnalysisImagesFolder_metadata = {
        'name': 'Analysis Images',
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [icuRiskAnalysisFolderID]
    }
    icuRiskAnalysisImagesFolder = service.files().create(body=icuRiskAnalysisImagesFolder_metadata, fields='id').execute()
    icuRiskAnalysisImagesFolderID = icuRiskAnalysisImagesFolder.get('id')
    csv_data.append(['2', 'ICU Risk Analysis Images Folder', icuRiskAnalysisImagesFolderID])
    print("[*] SUCCESS | ICU Risk Analysis Images Folder Created --> Folder ID: %s" % icuRiskAnalysisImagesFolderID)

    # Create a folder for the ICU Risk Analysis PowerPoint files
    icuRiskAnalysisPowerPointFolder_metadata = {
        'name': 'Analysis PowerPoint Files',
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [icuRiskAnalysisFolderID]
    }
    icuRiskAnalysisPowerPointFolder = service.files().create(body=icuRiskAnalysisPowerPointFolder_metadata, fields='id').execute()
    icuRiskAnalysisPowerPointFolderID = icuRiskAnalysisPowerPointFolder.get('id')
    csv_data.append(['3', 'ICU Risk Analysis PowerPoint Folder', icuRiskAnalysisPowerPointFolderID])
    print("[*] SUCCESS | ICU Risk Analysis PowerPoint Folder Created --> Folder ID: %s" % icuRiskAnalysisPowerPointFolderID)

    # Write File IDs to a CSV File so we can use them later
    header = ['File ID Index', 'File Name', 'File ID']
    filename = os.path.join('../helper_files', 'file_ids.csv')
    print("[*] Saving folder IDs...\n")
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write Header
        csv_writer.writerow(header)
        # Add File ID Data
        csv_writer.writerows(csv_data)
        # Close the file
        csv_file.close()
        print('---> Google Drive Initial Folder Setup Complete <---\n')


def setup_CreateLocalFolders():
    print("-"*34)
    print("Setting up needed local folders...\n")
    cwd = os.getcwd()
    try:
        print("[*] Creating the Daily Slides folder...")
        os.mkdir(os.path.join(cwd, '../../Daily Slides'))
    except FileExistsError:
        print("{*} Daily Slides Folder already exists...")
        pass
    except Exception as e:
        print(f"[!] An unhandled exception occurred while trying to create needed local folders: {e}")

    try:
        print("[*] Creating the Risk Map Images folder...")
        os.mkdir(os.path.join(cwd, '../../Risk_Map_Images'))
    except FileExistsError:
        print("{*} Risk Map Images folder already exists...")
    except Exception as e:
        print(f"[!] An unhandled exception occurred while trying to create needed local folders: {e}")

    print("-" * 34)
    print("--> All Needed Local Folders Created <--\n")


def main():
    setup_CreateLocalFolders()
    drive_executeInitialFolderSetup()


main()
