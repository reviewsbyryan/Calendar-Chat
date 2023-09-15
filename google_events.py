import json
from Google import create_service

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

calendar_id = "primary"

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""
To create an event, you need to provide a calendar id, event name, start time, and end time.
"""
def create_event(summary, start_time, end_time, description = None):
    event = {
        'summary': summary,
        'description': description,
        'start': {
          'dateTime': start_time,
          'timeZone': 'America/Los_Angeles',
        },
        'end': {
          'dateTime': end_time,
          'timeZone': 'America/Los_Angeles',
        },
    }
    
    service.events().insert(calendarId=calendar_id, body=event).execute()
    return json.dumps(event)

"""
To delete an event, you need to provide a calendar id and event id.
"""
def delete_event(event_id):
    service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
    return json.dumps(event_id)

def list_events():
    
    response = service.events().list(
        calendarId=calendar_id,
        showDeleted=False
        ).execute()
    
    events = response['items']

    filtered_events = []

    for event in events:
        filtered_events.append({'id': event['id'], 'summary': event['summary'],})
        print(filtered_events)

    return json.dumps(filtered_events)

list_events()