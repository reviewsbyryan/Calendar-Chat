import json
from Google import create_service

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

calendar_id = "primary"

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""
To create a calendar, you need to provide a calendar name.
"""
def create_calendar(calendar_name):
   calendar = {
        "summary": calendar_name,
        "timeZone": "America/Los_Angeles"
    }
   
   created_calendar = service.calendars().insert(body=calendar).execute(
   print(created_calendar["id"]))

"""
To delete a calendar, you need to provide a calendar id.
"""
def delete_calendar(calendar_id):
    service.calendars().delete(calendarId=calendar_id).execute()

"""
To list all calendars, you don"t need to provide any parameters.
"""
def list_calendars():
    page_token = None
    while True:
      calendar_list = service.calendarList().list(
         pageToken=page_token,
         maxResults=10,
         showHidden=False,
         showDeleted=False
         ).execute()
      for calendar_list_entry in calendar_list["items"]:
        print({"name": calendar_list_entry["summary"], "id": calendar_list_entry["id"]})
      page_token = calendar_list.get("nextPageToken")
      if not page_token:
        break