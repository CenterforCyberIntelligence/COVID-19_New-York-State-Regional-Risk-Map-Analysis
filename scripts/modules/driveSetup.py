import helper_functions
import csv
import os


def drive_executeInitialFolderSetup():
    # TODO: Establish error checking that will prevent this function from re-creating folders with pre-existing names

    print("+" * 35)
    print("Initial Google Drive Setup Starting")
    print("+" * 35)
    service = helper_functions.driveService()
    csv_data = []

    # Create a parent folder for all New York COVID-19 Analysis Projects
    parentFolder_metadata = {
        'name': 'New York COVID-19 Analysis Projects',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    parentFolder = service.files().create(body=parentFolder_metadata, fields='id').execute()
    parentFolderID = parentFolder.get('id')
    csv_data.append(['0', 'Parent Folder', parentFolderID])
    print("[*] SUCCESS | Parent Folder Created --> Folder ID: %s" % parentFolderID)

    # Create a folder for the ICU Risk Analysis Project
    icuRiskAnalysisFolder_metadata = {
        'name': 'Regional ICU Risk Analysis',
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parentFolderID]
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
