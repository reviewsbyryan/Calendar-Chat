import pandas as pd
from Google import create_service


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def create_taskList(taskList_title):
    AI_taskList = service.tasklists().insert(body={'title': taskList_title}).execute()
    print(AI_taskList['id'])

def delete_taskList(taskList_id):
    service.tasklists().delete(tasklist=taskList_id).execute()

def get_taskList(taskList_id):
    taskList = service.tasklists().get(tasklist=taskList_id).execute()
    print(taskList['title'])

def print_taskListsPD():
    taskLists = service.tasklists().list().execute()
    items_list = taskLists.get('items')
    nextPageToken = taskLists.get('nextPageToken')

    while nextPageToken:
        taskLists = taskLists.list(
            maxResults=100,
            pageToken = nextPageToken
        ).execute()
        items_list.extend(taskLists.get('items'))
        nextPageToken = taskLists.get('nextPageToken')

    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.min_rows', 500)
    pd.set_option('display.max_colwidth', 150)
    pd.set_option('display.width', 120)
    pd.set_option('display.expand_frame_repr', True)

    print(pd.DataFrame(items_list).head())

def print_taskLists_IDs():
    taskLists = service.tasklists().list().execute()
    items_list = taskLists.get('items')
    nextPageToken = taskLists.get('nextPageToken')

    while nextPageToken:
        taskLists = taskLists.list(
            maxResults=100,
            pageToken = nextPageToken
        ).execute()
        items_list.extend(taskLists.get('items'))
        nextPageToken = taskLists.get('nextPageToken')

    for item in items_list:
        print(item['id'])

def print_taskLists_titles():
    taskLists = service.tasklists().list().execute()
    items_list = taskLists.get('items')
    nextPageToken = taskLists.get('nextPageToken')

    while nextPageToken:
        taskLists = taskLists.list(
            maxResults=100,
            pageToken = nextPageToken
        ).execute()
        items_list.extend(taskLists.get('items'))
        nextPageToken = taskLists.get('nextPageToken')

    for item in items_list:
        print(item['title'])