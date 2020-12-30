import csv
import os
import pickle
from datetime import datetime

import pandas as pd
import pytz
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# API Key required by COVID Act Now
apiKey = "4d04a4db2e1945659ec528545143acd1"


def convert_Time_NYTimeZone():
    """
    # This snippet uses the pytz python library to easily ensure we are using EST time
    # (probably could do this with datetime.timedelta)
    # This is likely only needed if you are working on this script while it is located on a remote server.
    """
    try:
        utc = pytz.utc.localize(datetime.utcnow())
        ny_time = utc.astimezone(pytz.timezone("America/New_York"))
        return ny_time
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to convert the system time to Eastern Standard time. See the convert_Time_NYTimeZone() function.")
        print(f"Exception: {e}")


def set_ImageSavePath(cwd):
    try:
        todayDate = get_Date()
        folderPath = os.path.join(cwd, 'Risk_Map_Images', todayDate)
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to verify the path to save figure images. See the set_ImageSavePath() function.")
        print(f"Exception: {e}")


def get_Date():
    try:
        timeNow = convert_Time_NYTimeZone()
        todayDate = timeNow.strftime("%m-%d-%Y")
        return todayDate
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve today's date. See the get_Date() function.")
        print(f"Exception: {e}")


def get_FigureDateTime():
    try:
        timeNow = convert_Time_NYTimeZone()
        figureDate = timeNow.strftime("%m-%d-%Y %H:%M")
        return figureDate
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve the current date/time. See the get_FigureDateTime() function.")
        print(f"Exception: {e}")


def get_HistoricData():
    # TODO: Update this to use JSON
    try:
        HistoricData = pd.read_csv(
            f"https://api.covidactnow.org/v2/counties.timeseries.csv?apiKey={apiKey}")
        HistoricData = HistoricData[HistoricData['state'] == "NY"]
        HistoricData = HistoricData.fillna(0)
        return HistoricData
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve time series data. See the get_HistoricData() function.")
        print(f"Exception: {e}")


def get_currentSummary():
    try:
        todaySummary = pd.read_json(f"https://api.covidactnow.org/v2/counties.json?apiKey={apiKey}")
        todaySummary = todaySummary[todaySummary['state'] == "NY"]
        todaySummary = todaySummary.fillna(0)
        return todaySummary
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve today's summary data. See the get_currentSummary() function.")
        print(f"Exception: {e}")


def driveService():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    cwd = os.getcwd()
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(os.path.join(cwd, 'scripts', 'helper_files', 'credentials.json')):
        with open(os.path.join(cwd, 'scripts', 'helper_files', 'token.pickle'), 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join(cwd, 'scripts', 'helper_files', 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join(cwd, 'scripts', 'helper_files', 'token.pickle'), 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    return service


def drive_createTodayFolder():
    cwd = os.getcwd()
    today = get_Date()
    service = driveService()
    filename = os.path.join(cwd, 'scripts', 'helper_files', 'file_ids.csv')
    print("-"*66)
    print("*** Starting Google Drive Functions ***\n")
    print("*** Verifying ICU Analysis Images Folder Setup ***\n")
    # Find the ICU Images Folder ID (saved during the initial creation of the folder in file_ids.csv under helper_files

    print("[**] Looking up the Analysis Images folder ID...")
    file_ids = csv.reader(open(filename, 'r'))
    for row in file_ids:
        if row[0] == '2':
            folderData = row
            imagesFolderID = folderData[2]
            print(f"    --> Found ID: {imagesFolderID}\n")

            # Check to see if there is a in Google Drive for today
            print("[**] Checking to see if a folder for today already exists...\n")
            page_token = None
            response = service.files().list(
                q="mimeType='application/vnd.google-apps.folder' and parents in '{}'".format(imagesFolderID),
                spaces='drive',
                fields='nextPageToken, files(name)',
                pageToken=page_token).execute()

            if not response['files']:
                print("[!] There are no folders here... I can fix that!")
                print("[+] Creating an Images Folder for today...")
                gdrive_todayImagesFolder_metadata = {
                    'name': today,
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [imagesFolderID]
                }
                gdrive_todayImagesFolder = service.files().create(body=gdrive_todayImagesFolder_metadata,
                                                                  fields='id').execute()
                gdrive_TodayImagesFolderID = gdrive_todayImagesFolder.get('id')

                # Get "File ID Index" of last row in file_ids csv file
                indexedCSVFile = pd.read_csv(filename)
                csvRecord_todayFolderIndexValue = indexedCSVFile['File ID Index'].iloc[-1] + 1

                csvRecord_todayFolderName = "ICU_Analysis_Images_" + today
                csv_data = [csvRecord_todayFolderIndexValue, csvRecord_todayFolderName, gdrive_TodayImagesFolderID]

                with open(filename, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(csv_data)
                    csv_file.close()

                print(f"[++] SUCCESS | Google Drive Folder ID for {today}: %s\n" % gdrive_TodayImagesFolderID)
                return gdrive_TodayImagesFolderID
            else:
                for folderName in response['files']:
                    if folderName['name'] == today:
                        print("[**] Found an images folder for today! Skipping the rest of this function...\n")
                        pass
                    else:
                        # If no folder for today exists, create an images folder for today
                        print("[*] No folder for today found...\n")
                        print("[+] Creating an Images Folder for today...")
                        gdrive_todayImagesFolder_metadata = {
                            'name': today,
                            'mimeType': 'application/vnd.google-apps.folder',
                            'parents': [imagesFolderID]
                        }
                        gdrive_todayImagesFolder = service.files().create(body=gdrive_todayImagesFolder_metadata, fields='id').execute()
                        gdrive_TodayImagesFolderID = gdrive_todayImagesFolder.get('id')

                        # Get "File ID Index" of last row in file_ids csv file
                        indexedCSVFile = pd.read_csv(filename)
                        csvRecord_todayFolderIndexValue = indexedCSVFile['File ID Index'].iloc[-1] + 1

                        csvRecord_todayFolderName = "ICU_Analysis_Images_" + today
                        csv_data = [csvRecord_todayFolderIndexValue, csvRecord_todayFolderName, gdrive_TodayImagesFolderID]

                        with open(filename, 'a+', newline='') as csv_file:
                            csv_writer = csv.writer(csv_file)
                            csv_writer.writerow(csv_data)
                            csv_file.close()

                        print(f"[++] SUCCESS | Google Drive Folder ID for {today}: %s\n" % gdrive_TodayImagesFolderID)
                        return gdrive_TodayImagesFolderID


def drive_writeImagesToFolder():
    # TODO: Check to see if files for today already exist in folder

    drive_imagesFolderID = drive_createTodayFolder()
    service = driveService()
    cwd = os.getcwd()
    todayDate = get_Date()
    folderPath = os.path.join(cwd, 'Risk_Map_Images', todayDate)

    for filename in os.listdir(folderPath):
        filePath = os.path.join(folderPath, filename)
        image_metaData = {'name': filename, 'parents': [drive_imagesFolderID]}
        media = MediaFileUpload(filePath, mimetype='image/png')
        file = service.files().create(body=image_metaData,
                                      media_body=media,
                                      fields='id').execute()
        print(f"--> Image File Uploaded to GDrive | FileName: {filename} | GDrive File ID: {file.get('id')}")
    print("\n--> All Images Uploaded to Google Drive <--\n")

