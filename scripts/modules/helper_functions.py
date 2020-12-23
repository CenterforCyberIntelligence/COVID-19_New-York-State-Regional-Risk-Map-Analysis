import os
import pytz
import pandas as pd
from datetime import datetime


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
        timeNow = convert_Time_NYTimeZone()
        todayDate = timeNow.strftime("%m-%d-%Y")
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