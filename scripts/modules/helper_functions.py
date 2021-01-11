import csv
import os
import pandas as pd
import pickle
import pytz
from datetime import datetime
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
    try:
        HistoricData = pd.read_csv(
            f"https://api.covidactnow.org/v2/counties.timeseries.csv?apiKey={apiKey}")
        HistoricData = HistoricData[HistoricData['state'] == "NY"]
        HistoricData = HistoricData.fillna(0)
        save_HistoricData(HistoricData)
        return HistoricData
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve time series data. See the get_HistoricData() function.")
        print(f"Exception: {e}")


def get_currentSummary():
    try:
        todaySummary = pd.read_json(f"https://api.covidactnow.org/v2/counties.json?apiKey={apiKey}")
        todaySummary = todaySummary[todaySummary['state'] == "NY"]
        todaySummary = todaySummary.fillna(0)
        save_SummaryData(todaySummary)
        return todaySummary
    except Exception as e:
        print("\nThe script encountered an unhandled exception while attempting to retrieve today's summary data. See the get_currentSummary() function.")
        print(f"Exception: {e}")


def save_SummaryData(data):
    df = data
    cwd = os.getcwd()
    today = get_Date()
    try:
        print("[*] Saving collected daily summary data...")
        fileName = today + "_covid-act-now_summary_data.csv"
        filePath = os.path.join(cwd, 'Script_Collected_Data', fileName)
        df.to_csv(filePath)
    except Exception as e:
        print(f"[!] An error occurred while attempting to save the historic data collected for today: {e}\n")


def save_HistoricData(data):
    df = data
    cwd = os.getcwd()
    today = get_Date()
    try:
        print("[*] Saving collected historic time-series data...")
        fileName = today + "_covid-act-now_timeseries_data.csv"
        filePath = os.path.join(cwd, 'Script_Collected_Data', fileName)
        df.to_csv(filePath)
    except Exception as e:
        print(f"[!] An error occurred while attempting to save collected time-series data: {e}\n")


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


def drive_get_ICUImageFolderID():
    print("*** Verifying ICU Analysis Images Folder Setup ***\n")
    print("[**] Looking up the Analysis Images folder ID...")
    cwd = os.getcwd()
    filename = os.path.join(cwd, 'scripts', 'helper_files', 'file_ids.csv')
    file_ids = pd.read_csv(filename)
    imagesFolderID = file_ids.loc[file_ids['File Name'] == "ICU Risk Analysis Images Folder"]['File ID'].item()
    return imagesFolderID


def drive_get_DataManagementFolderID():
    print("*** Verifying Data Management Folder Setup ***\n")
    print("[**] Looking up the Historic Data Management folder ID...")
    cwd = os.getcwd()
    filename = os.path.join(cwd, 'scripts', 'helper_files', 'file_ids.csv')
    file_ids = pd.read_csv(filename)
    historicDataFolderID = file_ids.loc[file_ids['File Name'] == "Historic Data Management"]['File ID'].item()
    return historicDataFolderID


def drive_get_PowerPointFolderID():
    print("*** Verifying PowerPoint Folder Setup ***\n")
    print("[**] Looking up the PowerPoint folder ID...")
    cwd = os.getcwd()
    filename = os.path.join(cwd, 'scripts', 'helper_files', 'file_ids.csv')
    file_ids = pd.read_csv(filename)
    powerPointFolderID = file_ids.loc[file_ids['File Name'] == "ICU Risk Analysis PowerPoint Folder"]['File ID'].item()
    return powerPointFolderID


def drive_create_TodayFolder_Images():
    cwd = os.getcwd()
    filename = os.path.join(cwd, 'scripts', 'helper_files', 'file_ids.csv')
    today = get_Date()
    service = driveService()
    print("-"*62)
    print("*** Starting Google Drive Function | Write Images to Drive ***\n")

    # Find the ICU Images Folder ID (saved during the initial creation of the folder in file_ids.csv under helper_files
    imagesFolderID = drive_get_ICUImageFolderID()

    # Check to see if there is a in Google Drive for today
    print("[**] Checking to see if a folder for today already exists...\n")
    page_token = None
    response = service.files().list(
        q="mimeType='application/vnd.google-apps.folder' and parents in '{}'".format(imagesFolderID),
        spaces='drive',
        fields='nextPageToken, files(name)',
        pageToken=page_token).execute()

    if not response['files']:
        # It appears the Google Drive API (V3) retains the relationship between a parent file and a child file even when
        # a file is moved to the Drive Trash. In a scenario where "today's" folder is deleted, you must also delete it
        # from the Google Drive Trash to recreate today's folder.
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
                print("[**] Found an images folder for today...\n")
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


def drive_write_ICUImagesToFolder():

    drive_imagesFolderID = drive_create_TodayFolder_Images()
    if drive_imagesFolderID is None:
        print("[!] Image Folder Generation Failed...")
        print("[**] Either the images folder for today is in the Google Drive Trash, or it already exists and no action is needed.\n")
        pass
    else:
        print(f"Today's Image Folder ID: {drive_imagesFolderID}")
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


def drive_write_ICUPowerPointToFolder(powerPointFilePath):
    today = get_Date()
    folderID = drive_get_PowerPointFolderID()
    if folderID is None:
        print("[!] Something bad happened while attempting to find the PowerPoint folder ID...")
        pass
    else:
        print(f"PowerPoint Folder ID: {folderID}")
        service = driveService()
        fileName = today + "_ICU-Risk-Analysis-Slides.pptx"
        file_metaData = {'name': fileName, 'parents': [folderID]}
        media = MediaFileUpload(powerPointFilePath)
        file = service.files().create(body=file_metaData,
                                      media_body=media,
                                      fields='id').execute()
        print(f"--> PowerPoint File Uploaded to GDrive | FileName: {fileName} | GDrive File ID: {file.get('id')}\n")


def drive_write_DataToFolder():
    folderID = drive_get_DataManagementFolderID()
    today = get_Date()
    if folderID is None:
        print("[!] Something bad happened while attempting to find the data management folder ID...")
        pass
    else:
        print(f"Data Management Folder ID: {folderID}")
        service = driveService()
        cwd = os.getcwd()
        folderPath = os.path.join(cwd, 'Script_Collected_Data')
        for filename in os.listdir(folderPath):
            if today in filename:
                filePath = os.path.join(folderPath, filename)
                file_metaData = {'name': filename, 'parents': [folderID]}
                media = MediaFileUpload(filePath, mimetype='file/csv')
                file = service.files().create(body=file_metaData,
                                              media_body=media,
                                              fields='id').execute()
                print(f"--> Data File Uploaded to GDrive | FileName: {filename} | GDrive File ID: {file.get('id')}")
            else:
                pass
        print("\n--> All Data Files Uploaded to Google Drive <--\n")